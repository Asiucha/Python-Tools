# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 10:19:35 2022

@author: joanna.bednarska

script converts svg files to png formant and saves them in the same folder where svg files are
"""

import os
from html2image import Html2Image

from PIL import Image

# provide  a folder containing sgv files
root= "C:/Users/SVGs_Icons/svgs/"

svg_list =os.listdir(root)

for svg in svg_list:
    path=root+svg
    hti = Html2Image()
    hti.output_path = root
    hti.screenshot(other_file=path,save_as= ".".join([svg[:len(svg) - 4], "png"]))

    
#crop png 
root_png= "C:/Users/SVGs_Icons/png/"
png_list =os.listdir(root_png)

for png in png_list:
    im = Image.open(root_png + png)
    im1 = im.crop((0, 0, 20, 20))
    im1.save(root_png + png)
