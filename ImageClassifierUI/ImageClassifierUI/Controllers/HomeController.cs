using System.Diagnostics;
using System.Net.Http;
using System.Net.Http.Headers;
using ImageClassifierUI.Models;
using Microsoft.AspNetCore.Mvc;

namespace ImageClassifierUI.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly HttpClient _httpClient;

        public HomeController(ILogger<HomeController> logger, HttpClient httpClient)
        {
            _logger = logger;
            _httpClient = httpClient;
            _httpClient.BaseAddress = new Uri("http://127.0.0.1:8000");
        }

        public IActionResult Index()
        {
            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }

        [HttpPost]
        public async Task<IActionResult> Predict(IFormFile imageFile)
        {
            if (imageFile == null || imageFile.Length == 0)
            {
                ViewBag.Prediction = "Aucun fichier sélectionné.";
                return View("Index");
            }

            string base64Image = null;
            string imageType = null;

            using (var memoryStream = new MemoryStream())
            {
                await imageFile.CopyToAsync(memoryStream);
                base64Image = Convert.ToBase64String(memoryStream.ToArray());
                imageType = imageFile.ContentType;
            }

            ViewBag.Base64Image = base64Image;
            ViewBag.ImageType = imageType;

            using var content = new MultipartFormDataContent();
            var streamContent = new StreamContent(imageFile.OpenReadStream());
            streamContent.Headers.ContentType = new MediaTypeHeaderValue(imageFile.ContentType);

            content.Add(streamContent, "file", imageFile.FileName);

            var response = await _httpClient.PostAsync("/predict", content);

            if (response.IsSuccessStatusCode)
            {
                var jsonString = await response.Content.ReadAsStringAsync();
                var jsonDoc = System.Text.Json.JsonDocument.Parse(jsonString);
                var prediction = jsonDoc.RootElement.GetProperty("prediction").GetString();
                ViewBag.Prediction = prediction;

                // Récupérer l'objet JSON contenant les probabilités
                var probabilitiesElement = jsonDoc.RootElement.GetProperty("probabilities");

                // Créer un dictionnaire pour stocker les pourcentages
                var probabilities = new Dictionary<string, float>();
                foreach (var prop in probabilitiesElement.EnumerateObject())
                {
                    probabilities[prop.Name] = prop.Value.GetSingle();
                }

                ViewBag.Probabilite = probabilities;
            }
            else
            {
                ViewBag.Prediction = "Erreur lors de la prédiction.";
            }

            return View("Index");
        }
    }
}
