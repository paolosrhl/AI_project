import os
import numpy as np
from PIL import Image

dataset = {}#création dictionnaire
for file in os.listdir("."): #prends tout lees fichier qui ont un "."
    if file.startswith("binary") and file.endswith(".png"): #filtre les bons fichiers 
        img = Image.open(file) #ouvre l'image 
        matrix = np.array(img) #converti l'image en tableau numpy
        vector = (matrix > 10).astype(int) #compare chaque pixel à 10 transforme la matrice 2D en un seul vecteur 1D
        # récupérer le chiffre
        print(f"\nImage : {file}")
        print("Shape :", vector.shape)
        for row in vector:
            digit = file.split("Group_")[1].split(".")[0] #découpe la chaîne pour seulement garder le nombre 
            print(" ".join(map(str, row)))
            if digit not in dataset:
                dataset[digit] = []#si c'est la première fois qu'on rencontre ce chiffre on crée une liste vide 
                dataset[digit].append(" ".join(map(str, row)))#on ajoute le vecteur dans l'image du bon chiffre

print("Dataset construit :")

for digit in sorted(dataset):
    print(digit, "->", len(dataset[digit]), "exemples")
print(dataset)