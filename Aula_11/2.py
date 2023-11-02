import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

input_directory1 = "images/img_aluno1.jpeg"
input_directory2 = "images/img_aluno2.jpg"
output_directory = "outPath"

def suavizar(image, k):
    smoothed_image = np.zeros_like(image)

    height, width = image.shape

    for y in range(height):
        for x in range(width):
            neighborhood = []

            for i in range(max(0, y - k), min(height, y + k + 1)):
                for j in range(max(0, x - k), min(width, x + k + 1)):
                    neighborhood.append(image[i, j])

            average_value = np.mean(neighborhood)

            smoothed_image[y, x] = average_value

    return smoothed_image

output_dir = output_directory

# gray_scale
img_aluno1 = cv2.imread(input_directory1, cv2.IMREAD_GRAYSCALE)
img_aluno2 = cv2.imread(input_directory2, cv2.IMREAD_GRAYSCALE)

k = 3

smoothed_img_aluno1 = suavizar(img_aluno1, k)
smoothed_img_aluno2 = suavizar(img_aluno2, k)

plt.imshow(smoothed_img_aluno1)
plt.title("Smoothed 1")
plt.axis('off') 
plt.show()

plt.imshow(smoothed_img_aluno2)
plt.title("Smoothed 2")
plt.axis('off')  
plt.show()