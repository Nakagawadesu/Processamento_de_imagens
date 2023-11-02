import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Aula_12/img4.png", cv2.IMREAD_GRAYSCALE)

kernel_dilation = np.ones((3, 3), np.uint8)

dilation = cv2.dilate(image, kernel_dilation, iterations=1)

plt.figure(figsize=(9, 3))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(dilation, cmap='gray')
plt.title('Dilation (3x3)')
plt.axis('off')

plt.show()