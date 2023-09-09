from fileinput import filename
import os
import cv2
import numpy as np


input_directory = "/home/matheus/Desktop/Proessamento de imagens/images"
output_directory = "/home/matheus/Desktop/Proessamento de imagens/outPath"

def apply_log(input_dir ,output_dir):

    output_dir = output_dir + "_log"
    c = 30 

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    Image_files = os.listdir(input_dir)

    for file in Image_files:
        if file.lower().endswith( ('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir,file)
            output_path = os.path.join(output_dir,file)

            color_image = cv2.imread(input_path)

            if color_image is not None:

                gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
                logarithmic_image = c * np.log1p(gray_image)

                logarithmic_image = np.array(logarithmic_image, dtype=np.uint8)

                cv2.imwrite(output_path, logarithmic_image)

                print(f"image {file}convertida para negativo")

apply_log(input_directory,output_directory)                