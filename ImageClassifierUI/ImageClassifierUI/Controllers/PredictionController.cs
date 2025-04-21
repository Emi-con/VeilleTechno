using ImageClassifierUI.Models;
using Microsoft.AspNetCore.Mvc;
using System.Net.Http.Headers;
using System.Text.Json;

namespace ImageClassifierUI.Controllers
{
    public class PredictionController : Controller
    {
        private readonly IHttpClientFactory _httpClientFactory;

        public PredictionController(IHttpClientFactory httpClientFactory)
        {
            _httpClientFactory = httpClientFactory;
        }

        [HttpGet]
        public IActionResult Predict()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> Predict(IFormFile fichierImage)
        {
            if (fichierImage == null || fichierImage.Length == 0)
            {
                ModelState.AddModelError("", "Veuillez choisir une image.");
                return View();
            }

            using var client = _httpClientFactory.CreateClient();
            using var content = new MultipartFormDataContent();
            using var stream = fichierImage.OpenReadStream();
            using var streamContent = new StreamContent(stream);
            streamContent.Headers.ContentType = new MediaTypeHeaderValue(fichierImage.ContentType);
            content.Add(streamContent, "file", fichierImage.FileName);

            var response = await client.PostAsync("http://127.0.0.1:8000/predict", content);
            if (!response.IsSuccessStatusCode)
            {
                ModelState.AddModelError("", "Erreur lors de la prédiction.");
                return View();
            }

            var json = await response.Content.ReadAsStringAsync();
            var resultat = JsonSerializer.Deserialize<Dictionary<string, float>>(json);

            var predictions = resultat.Select(item => new ResultatPrediction
            {
                Label = item.Key,
                Probabilite = item.Value
            }).OrderByDescending(item => item.Probabilite).ToList();

            return View(predictions);
        }
    }
}
