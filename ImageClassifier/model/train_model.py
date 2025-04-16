#import des librairies
import tensorflow as tf
import os
import numpy as np

#Charger le dataset CIFAR-10
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()

#Afficher les dimensions des données
print(f"training_images is of type {type(train_images)}.\ntraining_labels is of type {type(train_labels)}\n")

# Inspect shape of the data
data_shape = train_images.shape

print(f"There are {data_shape[0]} examples with shape ({data_shape[1]}, {data_shape[2]})")

def reshape_and_normalize(images):

    # Normalize pixel values
    images = images / 255.0

    return images

train_images = reshape_and_normalize(train_images)
test_images = reshape_and_normalize(test_images)

print(f"Maximum pixel value after normalization: {np.max(train_images)}\n")
print(f"Shape of training set after reshaping: {train_images.shape}\n")
print(f"Shape of one image after reshaping: {train_images[0].shape}")

#Créer le modèle
model = tf.keras.models.Sequential([
    tf.keras.Input(shape=(32, 32, 3)),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

#Compiler le modèle
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#Entraîner le modèle
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

#Enregistrer le modèle
model.save('model/model.h5')

print("✅ Modèle entraîné et sauvegardé avec succès dans model/model.h5")
