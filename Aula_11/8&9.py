import cv2
import numpy as np

import matplotlib.pyplot as plt

input_directory1 = "images/img_aluno1.jpeg"
input_directory2 = "images/img_aluno2.jpg"

image1 = cv2.imread(input_directory1)
image2 = cv2.imread(input_directory2)

image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

image_addition = cv2.add(image1, image2)

image_subtraction = cv2.subtract(image1, image2)

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Imagem 1')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('Imagem 2')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(image_addition, cv2.COLOR_BGR2RGB))
plt.title('Adição')
plt.axis('off')

plt.figure()

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Imagem 1')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(image_subtraction, cv2.COLOR_BGR2RGB))
plt.title('Subtração')
plt.axis('off')

plt.show()