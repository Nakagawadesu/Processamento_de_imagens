import os
import xml.etree.ElementTree as ET

import torch
print(torch.__version__)
print(torch.cuda.is_available())

def convert_annotation(xml_file, output_txt_file, class_names):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)

        if w == 0 or h == 0:
            raise ValueError("Width or height is zero")

        with open(output_txt_file, 'w') as f:
            for obj in root.iter('object'):
                cls = obj.find('name').text
                if cls not in class_names:
                    continue
                cls_id = class_names.index(cls)
                xmlbox = obj.find('bndbox')
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text),
                     float(xmlbox.find('xmax').text), float(xmlbox.find('ymax').text))
                bb = ((b[0] + b[2]) / 2 / w, (b[1] + b[3]) / 2 / h, (b[2] - b[0]) / w, (b[3] - b[1]) / h)
                f.write(f"{cls_id} {bb[0]} {bb[1]} {bb[2]} {bb[3]}\n")
    except ET.ParseError:
        print(f"Parse error in file: {xml_file}")
    except ValueError as e:
        print(f"Value error in file: {xml_file}, {e}")

class_names = ['person', 'person-like']  
archive_folder = '/home/matheus/Downloads/archive' 

for folder in ['Train', 'Val', 'Test']:
    image_dir = os.path.join(archive_folder, folder, folder, 'JPEGImages')
    annotation_dir = os.path.join(archive_folder, folder, folder, 'Annotations')
    output_label_dir = '/home/matheus/dataset/labels/' + folder.lower()

    if not os.path.exists(output_label_dir):
        os.makedirs(output_label_dir)

    for image_file in os.listdir(image_dir):
        if image_file.endswith('.jpg'):
            basename = os.path.splitext(image_file)[0]
            xml_file = os.path.join(annotation_dir, basename + '.xml')
            output_txt_file = os.path.join(output_label_dir, basename + '.txt')
            convert_annotation(xml_file, output_txt_file, class_names)
