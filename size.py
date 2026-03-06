import os
from PIL import Image

size = (28, 28)

for file in os.listdir("."):

    # ignorer les fichiers déjà traités
    if file.startswith("gray_") or file.startswith("binary_") or file.startswith("resized_"):
        continue

    if file.endswith(".png") or file.endswith(".jpg"):

        img = Image.open(file)

        # grayscale
        gray = img.convert("L")

        # resize
        resized = gray.resize(size)

        # sauvegarde
        output_name = "resized_" + file
        resized.save(output_name)

        print(f"{file} -> {output_name}")