import cv2
import numpy as np
import matplotlib.pyplot as plt

image4 = cv2.imread("Aula_12/img4.png", cv2.IMREAD_GRAYSCALE)

kernel_erosion = np.ones((3, 3), np.uint8)

erosion = cv2.erode(image4, kernel_erosion, iterations=1)

plt.figure(figsize=(9, 3))

plt.subplot(1, 2, 1)
plt.imshow(image4, cmap='gray')
plt.title(' Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(erosion, cmap='gray')
plt.title('Erosion ')
plt.axis('off')

plt.show()