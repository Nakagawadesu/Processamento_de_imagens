from IPython.display import Image
import os

output_path = '/content/yolov5/runs/detect/exp/image (1).jpg'

if os.path.exists(output_path):
    display(Image(filename=output_path))
else:
    print("Output image not found. Ensure the path is correct.")