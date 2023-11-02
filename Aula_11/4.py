
import cv2
import numpy as np
import matplotlib.pyplot as plt

input_directory1 = "images/img_aluno1.jpeg"
input_directory2 = "images/img_aluno2.jpg"

image1 = cv2.imread(input_directory1, cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread(input_directory2, cv2.IMREAD_GRAYSCALE)

laplacian1 = cv2.Laplacian(image1, cv2.CV_64F)
laplacian2 = cv2.Laplacian(image2, cv2.CV_64F)

laplacian1 = np.uint8(np.absolute(laplacian1))
laplacian2 = np.uint8(np.absolute(laplacian2))

plt.subplot(1, 2, 1)
plt.imshow(image1)
plt.title(' Original1')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(laplacian1)
plt.title(' Laplaciana1')
plt.axis('off')

plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title('Original2')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(laplacian2)
plt.title(' Laplaciana2')
plt.axis('off')
plt.show()
