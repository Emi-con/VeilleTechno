from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from tensorflow import keras
from .utils import preprocess_image

import numpy as np

app = FastAPI()

#Charger le modèle
model = keras.models.load_model('model/model.h5')

#Définir les classes CIFAR-10
noms_classes = ['avion', 'automobile', 'oiseau', 'chat', 'cerf', 'chien', 'grenouille', 'cheval', 'bateau', 'camion']

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    #Lire l'image
    image_bytes = await file.read()

    #Prétraiter l'image
    image = preprocess_image(image_bytes)
    
    #Faire la prédiction
    prediction = model.predict(image)[0]

    # Classe prédite
    predicted_class = noms_classes[np.argmax(prediction)]

    # Probabilités arrondies
    prediction_percentages = {class_name: float(f"{prob*100:.2f}") for class_name, prob in zip(noms_classes, prediction)}

    return {
            "prediction": predicted_class,
            "probabilities": prediction_percentages
        }
