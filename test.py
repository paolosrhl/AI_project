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
    if file.startswith("binary") and file.endswith(".png"):
        vector = preprocess_image(file)
        print(f"\nImage : {file}")

        digit = file.split("Group_")[1].split(".")[0]

        if digit not in dataset:
            dataset[digit] = []

        dataset[digit].append(vector)

# -------- Load test image --------

vector = preprocess_image("BTest_3.png")

# -------- Comparison --------

distances = []

for digit in dataset:
    for example in dataset[digit]:
        distance = np.sum(np.abs(vector - example))
        distances.append((distance, digit))

distances.sort()
top3 = distances[:3]

votes = {}
for _, digit in top3:
    votes[digit] = votes.get(digit, 0) + 1

best_digit = max(votes, key=votes.get) # type: ignore

print("Digit reconnu :", best_digit)
print("Top 3 :", top3)