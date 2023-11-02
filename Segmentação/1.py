import cv2
import numpy as np
import matplotlib.pyplot as plt

def aplicar_limiar_otsu(image):
    _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

image_harewood = cv2.imread("Segmentação/harewood.jpg", cv2.IMREAD_GRAYSCALE)
image_nuts = cv2.imread("Segmentação/nuts.jpg", cv2.IMREAD_GRAYSCALE)
image_snow = cv2.imread("Segmentação/snow.jpg", cv2.IMREAD_GRAYSCALE)

otsu_harewood = aplicar_limiar_otsu(image_harewood)
otsu_nuts = aplicar_limiar_otsu(image_nuts)
otsu_snow = aplicar_limiar_otsu(image_snow)

plt.figure(figsize=(12, 9))

plt.subplot(4, 2, 1)
plt.imshow(image_harewood, cmap='gray')
plt.title('Imagem Harewood Original')
plt.axis('off')

plt.subplot(4, 2, 2)
plt.imshow(otsu_harewood, cmap='gray')
plt.title('Limiarização de Otsu')
plt.axis('off')

plt.subplot(4, 2, 3)
plt.imshow(image_nuts, cmap='gray')
plt.title('Imagem Nuts Original')
plt.axis('off')

plt.subplot(4, 2, 4)
plt.imshow(otsu_nuts, cmap='gray')
plt.title('Limiarização de Otsu')
plt.axis('off')

plt.subplot(4, 2, 5)
plt.imshow(image_snow, cmap='gray')
plt.title('Imagem Snow Original')
plt.axis('off')

plt.subplot(4, 2, 6)
plt.imshow(otsu_snow, cmap='gray')
plt.title('Limiarização de Otsu')
plt.axis('off')


plt.tight_layout()
plt.show()