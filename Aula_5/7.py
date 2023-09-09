from fileinput import filename
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


imagem_folha = cv2.imread("images/imagemFolha.jpg")

# (a) 
hls_image = cv2.cvtColor(imagem_folha, cv2.COLOR_BGR2HLS)

# (b) 
h_channel, l_channel, s_channel = cv2.split(hls_image)

# (c) 
l_equalized = cv2.equalizeHist(l_channel)

# (d)
equalized_hls_image = cv2.merge((h_channel, l_equalized, s_channel))

# (e) 
equalized_rgb_image = cv2.cvtColor(equalized_hls_image, cv2.COLOR_HLS2BGR)

#  imagens e histogramas
plt.figure(figsize=(12, 6))

plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(imagem_folha, cv2.COLOR_BGR2RGB))
plt.title("Imagem Original")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(equalized_rgb_image, cv2.COLOR_BGR2RGB))
plt.title("Imagem Equalizada")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.plot(cv2.calcHist([l_channel], [0], None, [256], [0, 256]), color="blue")
plt.title("Histograma Canal L (Original)")

plt.subplot(2, 3, 4)
plt.plot(cv2.calcHist([l_equalized], [0], None, [256], [0, 256]), color="blue")
plt.title("Histograma Canal L (Equalizado)")

plt.subplot(2, 3, 5)
plt.plot(cv2.calcHist([l_channel], [0], None, [256], [0, 256]), color="blue")
plt.plot(cv2.calcHist([l_equalized], [0], None, [256], [0, 256]), color="red", alpha=0.5)
plt.title("Comparação Histogramas Canal L")
plt.legend(["Original", "Equalizado"])

plt.tight_layout()
plt.show()
