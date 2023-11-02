import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Aula_12/img4.png", cv2.IMREAD_GRAYSCALE)

kernel_abertura = np.ones((3, 3), np.uint8)

abertura = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel_abertura)

plt.figure(figsize=(9, 3))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')
plt.axis ('off')

plt.subplot(1, 2, 2)
plt.imshow(abertura, cmap='gray')
plt.title('Abertura ')
plt.axis  ('off')

plt.show()
