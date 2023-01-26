from PIL import Image
import os

def heic_to_jpg(file_path):
    # Open the HEIC image using PIL
    with Image.open(file_path) as im:
        # Get the file name and extension
        file_name, file_ext = os.path.splitext(file_path)
        # Save the image as JPG
        im.save(f'{file_name}.jpg', 'JPEG')

# Example usage
heic_to_jpg('IMG_3511.HEIC')