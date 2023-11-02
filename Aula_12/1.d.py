import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread("Aula_12/img1.png", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("Aula_12/img2.png", cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread("Aula_12/img3.png", cv2.IMREAD_GRAYSCALE)


kernel_retangular = np.ones((5, 5), np.uint8)  # Tamanho 5x5 com 1

erosion1 = cv2.erode(image1, kernel_retangular, iterations=1)
erosion2 = cv2.erode(image2, kernel_retangular, iterations=1)
erosion3 = cv2.erode(image3, kernel_retangular, iterations=1)

dilation1 = cv2.dilate(image1, kernel_retangular, iterations=1)
dilation2 = cv2.dilate(image2, kernel_retangular, iterations=1)
dilation3 = cv2.dilate(image3, kernel_retangular, iterations=1)

plt.figure(figsize=(12, 4))

plt.subplot(2, 3, 1)
plt.imshow(image1, cmap='gray')
plt.title('Original 1')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(erosion1, cmap='gray')
plt.title('Erosão 1')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(dilation1, cmap='gray')
plt.title('Dilatação 1')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(image2, cmap='gray')
plt.title('Original 2')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(erosion2, cmap='gray')
plt.title('Erosão 2')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(dilation2, cmap='gray')
plt.title('Dilatação 2')
plt.axis('off')

plt.show()

plt.figure(figsize=(9, 3))

plt.subplot(1, 3, 1)
plt.imshow(image3, cmap='gray')
plt.title(' Original 3')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(erosion3, cmap='gray')
plt.title('Erosão 3')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(dilation3, cmap='gray')
plt.title('Dilatação 3')
plt.axis('off')

plt.show()