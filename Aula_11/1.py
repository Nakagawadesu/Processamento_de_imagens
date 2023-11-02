from fileinput import filename
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

input_directory1 = "images/img_aluno1.jpeg"
input_directory2 = "images/img_aluno2.jpg"

def suavizar(image):
    smoothed_image = np.zeros_like(image)
    neighborhood_size = 3

    # metade do tamanho da vizinhança
    half_size = neighborhood_size // 2

    # pixels da imagem
    for y in range(half_size, image.shape[0] - half_size):
        for x in range(half_size, image.shape[1] - half_size):
            # vizinhança do pixel
            neighborhood = image[y - half_size:y + half_size + 1, x - half_size:x + half_size + 1]

            # média da vizinhança
            average_value = np.mean(neighborhood)

            # média ao pixel suavizado
            smoothed_image[y, x] = average_value

    return smoothed_image


# gray_scale
img_aluno1 = cv2.imread(input_directory1, cv2.IMREAD_GRAYSCALE)
img_aluno2 = cv2.imread(input_directory2, cv2.IMREAD_GRAYSCALE)

# Apply the smoothing filter to the images
smoothed_img_aluno1 = suavizar(img_aluno1)
smoothed_img_aluno2 = suavizar(img_aluno2)

# Save the smoothed images with the same file names
plt.imshow(smoothed_img_aluno1)
plt.title("Smoothed  1")
plt.axis('off')  # Hide axis
plt.show()

plt.imshow(smoothed_img_aluno2)
plt.title("Smoothed  2")
plt.axis('off')  # Hide axis
plt.show()