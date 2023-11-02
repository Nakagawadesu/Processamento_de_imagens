import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregue as duas imagens
input_directory1 = "images/img_aluno1.jpeg"
input_directory2 = "images/img_aluno2.jpg"

image1 = cv2.imread(input_directory1)
image2 = cv2.imread(input_directory2)

# Defina o tamanho da janela da vizinhança
window_size = 3

# Aplique o filtro da mediana em ambas as imagens
median_filtered1 = cv2.medianBlur(image1, window_size)
median_filtered2 = cv2.medianBlur(image2, window_size)

# Exiba as imagens originais e as imagens filtradas pela mediana
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(median_filtered1, cv2.COLOR_BGR2RGB))
plt.title('Mediana')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(median_filtered2, cv2.COLOR_BGR2RGB))
plt.title('Mediana ')
plt.axis('off')

plt.show()