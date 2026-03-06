import os
import numpy as np
from PIL import Image

# -------- Build dataset --------

dataset = {}

for file in os.listdir("."):

    if file.startswith("resized_") and file.endswith(".png"):

        img = Image.open(file)

        matrix = np.array(img)

        vector = vector = (matrix > 200).astype(int).flatten()

        digit = file.split("Group ")[1][0]

        if digit not in dataset:
            dataset[digit] = []

        dataset[digit].append(vector)

# -------- Load test image --------

img = Image.open("test_1.png")

# convertir en grayscale
img = img.convert("L")

# normaliser la taille
img = img.resize((28, 28))

# transformer en matrice
matrix = np.array(img)

# inverser les couleurs (noir/blanc)
matrix = 255 - matrix

# binarisation + vecteur
vector = (matrix > 100).astype(int).flatten()

# -------- Comparison --------

distances = []

for digit in dataset:
    for example in dataset[digit]:

        distance = np.sum(np.abs(vector - example))
        distances.append((distance, digit))

# trier les distances
distances.sort()

# prendre les 3 plus proches
top3 = distances[:3]

# vote
votes = {}

for _, digit in top3:
    votes[digit] = votes.get(digit, 0) + 1

best_digit = max(votes, key=votes.get)

print("Digit reconnu :", best_digit)