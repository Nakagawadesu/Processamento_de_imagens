from fileinput import filename
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt



unequalized_image = cv2.imread("images/unequalized.jpg")
imagem_folha = cv2.imread("images/imagemFolha.jpg")
img_aluno = cv2.imread("images/img_aluno.jpeg")


gray_image = cv2.cvtColor(unequalized_image, cv2.COLOR_BGR2GRAY)
gray_hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# histograma para cada camada
b, g, r = cv2.split(img_aluno)
b_hist = cv2.calcHist([b], [0], None, [256], [0, 256])
g_hist = cv2.calcHist([g], [0], None, [256], [0, 256])
r_hist = cv2.calcHist([r], [0], None, [256], [0, 256])

# histograma para cada camada 
b, g, r = cv2.split(imagem_folha)
b_hist_folha = cv2.calcHist([b], [0], None, [256], [0, 256])
g_hist_folha = cv2.calcHist([g], [0], None, [256], [0, 256])
r_hist_folha = cv2.calcHist([r], [0], None, [256], [0, 256])

# histogramas
plt.figure(figsize=(10, 8))

plt.subplot(3, 3, 1)
plt.imshow(cv2.cvtColor(unequalized_image, cv2.COLOR_BGR2RGB))
plt.title("Imagem Original")
plt.axis("off")

plt.subplot(3, 3, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Imagem em Tons de Cinza")
plt.axis("off")

plt.subplot(3, 3, 3)
plt.plot(gray_hist, color="black")
plt.title("Histograma - Tons de Cinza")

plt.subplot(3, 3, 4)
plt.imshow(cv2.cvtColor(img_aluno, cv2.COLOR_BGR2RGB))
plt.title("img_aluno")
plt.axis("off")

plt.subplot(3, 3, 5)
plt.plot(b_hist, color="blue")
plt.title("Histograma - Canal Azul")

plt.subplot(3, 3, 6)
plt.plot(g_hist, color="green")
plt.title("Histograma - Canal Verde")

plt.subplot(3, 3, 7)
plt.plot(r_hist, color="red")
plt.title("Histograma - Canal Vermelho")

plt.subplot(3, 3, 8)
plt.imshow(cv2.cvtColor(imagem_folha, cv2.COLOR_BGR2RGB))
plt.title("imagem_folha")
plt.axis("off")

plt.subplot(3, 3, 9)
plt.plot(b_hist_folha, color="blue")
plt.title("Histograma - Canal Azul")

plt.tight_layout()
plt.show()
