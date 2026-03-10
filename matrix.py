import os
import numpy as np
from PIL import Image

for file in os.listdir("."):

    # ne prendre que les images déjà normalisées
    if file.startswith("binary") :

        img = Image.open(file)
        img = img.convert("L")
        img = img.resize((28, 28))

        matrix = np.array(img)

        # binarisation
        binary_matrix = (matrix > 100).astype(int)

        print(f"\nImage : {file}")
        print("Shape :", binary_matrix.shape)

        # afficher la matrice 28x28
        for row in binary_matrix:
            print(" ".join(map(str, row)))