# FrequencyDecypher

This project implements a ciphertext-only attack against a custom image
"encryption" script that applies a **random permutation** to pixel intensity
values (0–255). Because a new permutation is generated for every encryption,
keys cannot be reused across images, and direct decryption is impossible.

However, permutation ciphers preserve the **frequency** of each value.  
If a plaintext pixel value appears *X* times, its encrypted counterpart also
appears *X* times.  
This property allows a histogram-based frequency attack.

## Attack Overview

1. Two plaintext demo images (`demo1`, `demo2`) are used to build an approximate
   **reference plaintext histogram**, representing how often each intensity
   typically appears.

2. The ciphertext image's histogram is computed and both histograms are sorted
   from **rarest → most common**.

3. Intensities are paired **by frequency rank**:
`inverse_mapping[ ciphertext_rank[k] ] = plaintext_rank[k]\`

4. This produces an estimated inverse permutation, which is applied to the
ciphertext to recover a visually meaningful image.

The recovery is not perfect—fine gradients or similar intensity ranges may be
misaligned—but the decrypted output retains enough structure to reveal the
content of the image (e.g., flags or text).

## Files

- `decrypt.py` — performs the histogram-based decryption.
- `encrypt.py` — original encryption script (provided for reference).
- Demo images (`demo1.bmp`, `demo2.bmp`, etc.) can be used to compute the
reference histogram.

## Usage

Place your encrypted BMP image in the same directory and run:
```
python3 decrypt.py <image_name>
```


## Notes

- Works on grayscale or RGB BMPs (each channel is treated independently).
- The approach relies purely on **frequency analysis**, not key reuse.
- Designed for educational cryptography purposes only.

