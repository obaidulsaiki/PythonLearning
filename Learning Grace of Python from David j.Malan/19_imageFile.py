# Description: Image file processing
# pillow.readthedocs.io - documentation of image processing library
# pip install pillow
# there is 2 static pictude in the folder
# we are going to make animation with them
import sys
from PIL import Image  # import image library


def imagev1():
    images = []
    # started from 1 because 0 is the name of the file and to the end
    for arg in sys.argv[1:]:
        image = Image.open(arg)
        images.append(image)
    images[0].save(
        "19_imageFile.gif",  # name of the file
        save_all=True,  # save all of the frames
        # loop = 0 means infinte loop
        append_images=images[1:], duration=200, loop=0
    )


imagev1()
