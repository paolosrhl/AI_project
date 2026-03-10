import os
import numpy as np
from PIL import Image

def preprocess_image(path):
    img = Image.open(path)
    img = img.convert("L")
    img = img.resize((28, 28))   # important si tailles différentes
    matrix = np.array(img)

    # choisis soit avec inversion, soit sans inversion
    matrix = 255 - matrix

    vector = (matrix > 128).astype(int).flatten()
    return vector

# -------- Build dataset --------

dataset = {}

for file in os.listdir("."):
    if file.startswith("binary") :
        vector = preprocess_image(file)
        print(f"\nImage : {file}")

        digit = file.split("Group_")[1].split(".")[0]

        if digit not in dataset:
            dataset[digit] = []

        dataset[digit].append(vector)

# -------- Load test image --------

vector = preprocess_image("TTest_3.PNG")

# -------- Comparison --------

# Liste qui va contenir toutes les distances calculées
# Chaque élément aura la forme : (distance, chiffre)
distances = []

# On parcourt chaque chiffre du dataset
# Par exemple "1", "2", "3", etc.
for digit in dataset:

    # Pour ce chiffre, on parcourt tous les exemples associés
    for example in dataset[digit]:

        # On calcule la distance entre l'image test (vector)
        # et l'image du dataset (example)
        #
        # vector - example : différence pixel par pixel
        # np.abs(...)      : valeur absolue de chaque différence
        # np.sum(...)      : somme totale des différences
        #
        # Plus la distance est petite, plus les deux images se ressemblent
        distance = np.sum(np.abs(vector - example))

        # On stocke la distance calculée avec le chiffre correspondant
        distances.append((distance, digit))

# On trie toutes les distances par ordre croissant
# Les images les plus proches de l'image test seront au début de la liste
distances.sort()

# On garde les 3 exemples les plus proches
# C'est le principe du k-NN avec k = 3
top3 = distances[:3]

# Dictionnaire pour compter le nombre de votes de chaque chiffre
votes = {}

# On parcourt les 3 voisins les plus proches
for _, digit in top3:

    # votes.get(digit, 0) :
    # - si le chiffre existe déjà dans votes, on récupère sa valeur
    # - sinon on prend 0
    #
    # Ensuite on ajoute 1 vote à ce chiffre
    votes[digit] = votes.get(digit, 0) + 1

# On choisit le chiffre qui a le plus de votes
# C'est le résultat final de la reconnaissance
best_digit = max(votes, key=votes.get)  # type: ignore

# Affiche le chiffre reconnu
print("Digit reconnu :", best_digit)

# Affiche les 3 voisins les plus proches avec leurs distances
print("Top 3 :", top3)