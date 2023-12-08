import cv2
import matplotlib.pyplot as plt
from xml.etree import ElementTree as ET

xml_file_path = '/home/matheus/Downloads/archive/Train/Train/Annotations/image (1).xml'

tree = ET.parse(xml_file_path)
root = tree.getroot()

bounding_boxes = []
for member in root.findall('object'):
    bndbox = member.find('bndbox')
    xmin = int(bndbox.find('xmin').text)
    ymin = int(bndbox.find('ymin').text)
    xmax = int(bndbox.find('xmax').text)
    ymax = int(bndbox.find('ymax').text)
    bounding_boxes.append((xmin, ymin, xmax, ymax))

xmin, ymin, xmax, ymax = bounding_boxes[0]

image_file_path = '/home/matheus/Downloads/archive/Train/Train/JPEGImages/image (1).jpg'

image = cv2.imread(image_file_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

plt.figure(figsize=(8, 6))
plt.imshow(image)
plt.axis('off')  
plt.show()