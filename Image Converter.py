from PIL import Image

# TODO: Figure out what the heck this is, add comments, create window

image = Image.open('default.png')

def get_info(image_obj):
    i_filename = image_obj.filename
    i_format = image_obj.format.lower()
    i_mode = image_obj.mode
    i_width, i_height = image_obj.size
    
    return image_obj.filename, image.format.lower(), image_obj.mode, i_width, i_height

def to_jpg(image_obj):
    n_name, n_format, n_mode, n_height, n_width = get_info(image_obj)
    n_name = n_name.replace(n_format, 'jpg')
    new_img = image_obj.convert('RGB')
    new_img.save(n_name)
    
def to_png(image_obj):
    pass

to_jpg(image)