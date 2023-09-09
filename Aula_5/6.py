from fileinput import filename
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def apply_histogram_equalization(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized_image = cv2.equalizeHist(gray_image)
    return cv2.cvtColor(equalized_image, cv2.COLOR_GRAY2BGR)

lena_image = cv2.imread("images/lena.png")
unequalized_image = cv2.imread("images/unequalized.jpg")
imagem_folha = cv2.imread("images/imagemFolha.jpg")
img_aluno = cv2.imread("images/img_aluno.jpeg")

#equalização de histograma em cada imagem
lena_equalized = apply_histogram_equalization(lena_image)
unequalized_equalized = apply_histogram_equalization(unequalized_image)
imagem_folha_equalized = apply_histogram_equalization(imagem_folha)
img_aluno_equalized = apply_histogram_equalization(img_aluno)

#  originais e equalizadas
plt.figure(figsize=(12, 10))

plt.subplot(4, 2, 1)
plt.imshow(cv2.cvtColor(lena_image, cv2.COLOR_BGR2RGB))
plt.title("lena.png (Original)")
plt.axis("off")

plt.subplot(4, 2, 2)
plt.imshow(cv2.cvtColor(lena_equalized, cv2.COLOR_BGR2RGB))
plt.title("lena.png (Equalizada)")
plt.axis("off")

plt.subplot(4, 2, 3)
plt.imshow(cv2.cvtColor(unequalized_image, cv2.COLOR_BGR2RGB))
plt.title("unequalized.jpg (Original)")
plt.axis("off")

plt.subplot(4, 2, 4)
plt.imshow(cv2.cvtColor(unequalized_equalized, cv2.COLOR_BGR2RGB))
plt.title("unequalized.jpg (Equalizada)")
plt.axis("off")

plt.subplot(4, 2, 5)
plt.imshow(cv2.cvtColor(imagem_folha, cv2.COLOR_BGR2RGB))
plt.title("imagem_folha.jpg (Original)")
plt.axis("off")

plt.subplot(4, 2, 6)
plt.imshow(cv2.cvtColor(imagem_folha_equalized, cv2.COLOR_BGR2RGB))
plt.title("imagem_folha.jpg (Equalizada)")
plt.axis("off")

plt.subplot(4, 2, 7)
plt.imshow(cv2.cvtColor(img_aluno, cv2.COLOR_BGR2RGB))
plt.title("img_aluno.jpg (Original)")
plt.axis("off")

plt.subplot(4, 2, 8)
plt.imshow(cv2.cvtColor(img_aluno_equalized, cv2.COLOR_BGR2RGB))
plt.title("img_aluno.jpg (Equalizada)")
plt.axis("off")

plt.tight_layout()
plt.show()