import cv2
import numpy as np
import matplotlib.pyplot as plt

input_directory = "Aula_12/img2.png"
image = cv2.imread(input_directory, cv2.IMREAD_GRAYSCALE)
  
elemento_estruturante = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0],], dtype=np.uint8)

erosion = cv2.erode(image, elemento_estruturante, iterations=1)

dilation = cv2.dilate(image, elemento_estruturante, iterations=1)

closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, elemento_estruturante)

plt.figure(figsize=(12, 4))

plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(erosion, cmap='gray')
plt.title('Erosão')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(dilation, cmap='gray')
plt.title('Dilatação')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(closing, cmap='gray')
plt.title('Fechamento')
plt.axis('off')
plt.show()