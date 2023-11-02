
import cv2
import numpy as np
import matplotlib.pyplot as plt

input_directory1 = "images/img_aluno1.jpeg"
input_directory2 = "images/img_aluno2.jpg"

image1 = cv2.imread(input_directory1, cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread(input_directory2, cv2.IMREAD_GRAYSCALE)



kernel_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
kernel_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)


roberts_x1 = cv2.filter2D(image1, -1, kernel_x)
roberts_y1 = cv2.filter2D(image1, -1, kernel_y)

roberts_x2 = cv2.filter2D(image2, -1, kernel_x)
roberts_y2 = cv2.filter2D(image2, -1, kernel_y)

roberts_combined1 = cv2.addWeighted(roberts_x1, 0.5, roberts_y1, 0.5, 0)
roberts_combined2 = cv2.addWeighted(roberts_x2, 0.5, roberts_y2, 0.5, 0)

plt.subplot(1, 2, 1)
plt.imshow(image1)
plt.title('Original 1')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(roberts_combined1)
plt.title(' Roberts 1')
plt.axis('off')

plt.subplot(3, 4, 3)
plt.imshow(image2)
plt.title('Original 2')
plt.axis('off')

plt.subplot(3, 4, 4)
plt.imshow(roberts_combined2)
plt.title('Roberts 2')
plt.axis('off')
plt.show()