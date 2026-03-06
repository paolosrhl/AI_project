import os
import numpy as np
from PIL import Image

# -------- Build dataset --------

dataset = {}

for file in os.listdir("."):

    if file.startswith("resized_") and file.endswith(".png"):

        img = Image.open(file)

        matrix = np.array(img)

        vector = (matrix > 128).astype(int).flatten()

        digit = file.split("Group ")[1][0]

        if digit not in dataset:
            dataset[digit] = []

        dataset[digit].append(vector)

# -------- Load test image --------

img = Image.open("test_1.png")

img = img.convert("L")
img = img.resize((28, 28))

matrix = np.array(img)

vector = (matrix > 128).astype(int).flatten()

# -------- Comparison --------

best_digit = None
best_score = float("inf")

for digit in dataset:

    for example in dataset[digit]:

        distance = np.sum(np.abs(vector - example))

        if distance < best_score:
            best_score = distance
            best_digit = digit

print("Digit reconnu :", best_digit)