#!/usr/bin/env python
# coding: utf-8

# In[2]:

from PIL import Image
import os
import sys


# Resize Function
def resize_image(width=800,hieght=600,path_to_images=os.getcwd(),working_dir=os.getcwd()):
    

    '''
    Args:
    path_to_images: string, path to images directory
    working_dir: path to the working directory if working directory differs than images directory
    size: new images size
    
    '''
    for img in os.listdir(path_to_images):
        directory = path_to_images + img
        image = Image.open(directory)
        image = image.resize((int(width),int(hieght)))
        if path_to_images == working_dir:
            image.save(img)
        else:
            os.chdir(path_to_images)
            image.save(img)
            os.chdir(working_dir)
            
if __name__ == '__main__':
    # Map command line arguments to function arguments.
    resize_image(*sys.argv[1:])



