import numpy as np
from PIL import Image
from sys import argv

image = Image.open(argv[1] + ".bmp")

# Convert to NumPy array
array = np.array(image)

# Print shape and type
print(f"Array Shape: {array.shape}")
print(f"Data Type: {array.dtype}")

# Generate a random permutation
mapping = np.random.permutation(256).astype(np.uint8)
mapped_array = mapping[array]

# Convert to PIL image and save as BMP
Image.fromarray(mapped_array).save(argv[1] + "_enc.bmp", "BMP")
