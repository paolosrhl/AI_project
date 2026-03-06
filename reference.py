import os
import numpy as np
from PIL import Image

dataset = {}

for file in os.listdir("."):

    if file.startswith("resized_") and file.endswith(".png"):

        img = Image.open(file)

        matrix = np.array(img)

        vector = (matrix > 128).astype(int).flatten()

        # récupérer le chiffre
        digit = file.split("Group ")[1][0]

        if digit not in dataset:
            dataset[digit] = []

        dataset[digit].append(vector)

print("Dataset construit :")

for digit in sorted(dataset):
    print(digit, "->", len(dataset[digit]), "exemples")