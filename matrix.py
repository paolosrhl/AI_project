import os
import numpy as np
from PIL import Image

for file in os.listdir("."):

    # ne prendre que les images déjà normalisées
    if file.startswith("resized_") and file.endswith(".png"):

        img = Image.open(file)

        # convertir en matrice numpy
        matrix = np.array(img)

        # transformer en vecteur (ligne de pixels)
        vector = (matrix > 128).astype(int).flatten()

        print(f"\nImage : {file}")
        print(vector[:50])  # affiche seulement les 50 premiers pixels