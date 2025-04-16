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
    predictions = model.predict(image)[0]

    #Création de la réponse
    resultats = {noms_classes[i]: float(predictions[i]) for i in range(len(noms_classes))}

    return JSONResponse(content=resultats)