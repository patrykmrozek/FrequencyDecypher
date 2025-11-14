"""
encryption: random permutation of 0-255

cipher_pixel = mapping[plain_pixel] - substitution

frequncy of pixels is preserved in a substitution cipher
so, histogram(cipher) is a shuffle of histogram(plain)

can take the demos as an example and use them to guage how
often some values appear

plain_histogram[i] - how often value i appears in the plaintext
images demo1 and demo2

then we order values by frequency using argsort()

for each k from 0-255:
    take the kth rarest value in the ciphertext
    assign it the kth rarest value in the plaintext
"""

from sys import argv

import numpy as np
from PIL import Image

# load known plaintext and ciphertext
demo1 = np.array(Image.open("demo1.bmp"))
demo1_enc = np.array(Image.open("demo1_enc.bmp"))
demo2 = np.array(Image.open("demo2.bmp"))
demo2_enc = np.array(Image.open("demo2_enc.bmp"))


def build_plain_histogram():
    hist = np.zeros(256, dtype=(np.uint64))
    for arr in [demo1, demo2]:
        hist += np.bincount(arr.flatten(), minlength=256).astype(np.uint64)
    return hist


def decrypt(image, inverse_mapping):
    return inverse_mapping[image]


plain_histogram = build_plain_histogram()
order_plain = np.argsort(plain_histogram)

image = np.array(Image.open(argv[1] + ".bmp"))

cipher_histogram = np.bincount(image.flatten(), minlength=256)
order_cipher = np.argsort(cipher_histogram)

inverse_mapping = np.zeros(256, dtype=np.uint8)
for k in range(256):
    inverse_mapping[order_cipher[k]] = order_plain[k]

dec = decrypt(image, inverse_mapping)

Image.fromarray(dec).save(argv[1] + "_DECRYPT.bmp", "BMP")
