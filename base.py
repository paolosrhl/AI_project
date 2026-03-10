import os
from PIL import Image

threshold = 128

for file in os.listdir("."):
    if file.startswith("RGroup") and file.endswith(".jpg"):
        img = Image.open(file)
        # grayscale
        gray = img.convert("L")

        # binarisation
        binary = gray.point(lambda x: 255 if int(x) > threshold else 0)

        # sauvegarde
        binary.save("binary_" + file)

        print(f"{file} -> binary_{file}")