import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Aula_12/img5.png", cv2.IMREAD_GRAYSCALE)

# Utilizei o operador Canny para detectar bordas
edges = cv2.Canny(image, 100, 200)  # Ajuste os valores de limiar conforme necessário


plt.figure(figsize=(9, 3))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Bordas Detectadas (Canny)')
plt.axis('off')

plt.show()