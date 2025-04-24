from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

app = FastAPI()
model = load_model("model/model.h5")

class_names = ['avion', 'automobile', 'oiseau', 'chat', 'cerf',
               'chien', 'grenouille', 'cheval', 'bateau', 'camion']

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).resize((32, 32)).convert("RGB") #Lit le contenu binaire de l’image envoyée.
    image_array = np.expand_dims(np.array(image) / 255.0, axis=0)

    prediction = model.predict(image_array)[0] 
    predicted_class = class_names[np.argmax(prediction)]
# Associer chaque classe à son pourcentage
    prediction_percentages = {class_name: float(f"{prob*100:.2f}") for class_name, prob in zip(class_names, prediction)}

    return {
        "prediction": predicted_class,
        "probabilities": prediction_percentages
    }