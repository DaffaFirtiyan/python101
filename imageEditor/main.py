from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'imageEditor/image'
pathOut = 'imageEditor/editedImage'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    # other filters are: BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SHARPEN, SMOOTH, SMOOTH_MORE
    edit = img.filter(ImageFilter.SMOOTH).convert("L")
    factor = 1.5
    enchancer = ImageEnhance.Contrast(edit)
    edit = enchancer.enhance(factor)

    cleanName = os.path.splitext(filename)[0]
    edit.save(f'{pathOut}/{cleanName}_edited.jpg')