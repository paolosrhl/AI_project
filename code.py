import os
from PIL import Image

# dossier actuel
folder = "."

# parcourir tous les fichiers
for file in os.listdir(folder):

    # vérifier si c'est une image png ou jpg
    if file.endswith(".png") or file.endswith(".jpg"):

        # ouvrir l'image
        img = Image.open(file)

        # convertir en grayscale
        gray = img.convert("L")

        # nom du nouveau fichier
        new_name = "gray_" + file

        # sauvegarder
        gray.save(new_name)

        print(f"{file} convertie en {new_name}")