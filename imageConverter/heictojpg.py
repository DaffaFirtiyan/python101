from PIL import Image
import os

def heic_to_jpg(file_path):
    with Image.open(file_path) as im:
        file_name, file_ext = os.path.splitext(file_path)
        im.save(f'{file_name}.jpg', 'JPEG')

heic_to_jpg('IMG_3511.HEIC')