from PIL import Image
import numpy as np
import io

def preprocess_image(image_bytes):
    #Ouvrir l'image, la redimensionner 32 x 32et la convertir en tableau numpy
    image = Image.open(io.BytesIO(image_bytes)).resize((32, 32))

    #Si l'image a 4 canaux, réduire à 3 canaux(RGBA -> RGB)
    if image.mode == 'RGBA':
        image = image.convert('RGB')

    #Convertir en numpy array et normaliser les valeurs des pixels
    img_array = np.array(image) / 255.0

    #Redimensionner en 32 x 32 x 3
    if img_array.shape != (32, 32, 3):
        raise ValueError("L'image doit être de taille 32x32 et avoir 3 canaux (R, G, B)")

    #Ajouter une dimension pour correspondre à la forme (1, 32, 32, 3)
    return np.expand_dims(img_array, axis=0)
