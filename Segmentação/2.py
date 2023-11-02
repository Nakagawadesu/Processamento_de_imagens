import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

image = cv2.imread('Segmentação/atividades_2/Caso_1_o.png', 0)

#array de uma dimansão
data = image.reshape((-1, 1))

#número de clusters (K) para o K-means
K = 2
# K-means
kmeans = KMeans(n_clusters=K)
kmeans.fit(data)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

segmented_image = centers[labels].reshape(image.shape)


image2 = cv2.imread('Segmentação/atividades_2/Caso_1.png', 1)  


lower_red = np.array([0, 0, 100])
upper_red = np.array([100, 100, 255])

mask = cv2.inRange(image2, lower_red, upper_red)

image2[mask == 255] = [0, 0, 0]  

image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


plt.figure(figsize=(18, 5))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(image2, cmap='gray')
plt.title(' Binarizada')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(segmented_image, cmap='gray')
plt.title('Segmentada')
plt.axis('off')

plt.show()