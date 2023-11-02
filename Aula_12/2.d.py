import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Aula_12/img4.png", cv2.IMREAD_GRAYSCALE)

kernel_fechamento = np.ones((3, 3), np.uint8)

fechamento = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_fechamento)

plt.figure(figsize=(9, 3))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title(' Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(fechamento, cmap='gray')
plt.title('Fechamento ')
plt.axis('off')

plt.show()





