import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg

from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnchoredOffsetbox

import cv2
import extcolors

from colormap import rgb2hex

input_path = './static/uploads/'
input_name = "2022-06-28_12.51.43.png"
output_width = 900                   #set the output size
img = Image.open(input_path+input_name)
wpercent = (output_width/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((output_width,hsize), Image.ANTIALIAS)

#save
resize_name = 'resize_' + input_name  #the resized image name
img.save(input_path+resize_name)                 #output location can be specified before resize_name

#read
plt.figure(figsize=(9, 9))
img_url = input_path+resize_name
img = plt.imread(img_url)
plt.imshow(img)
plt.axis('off')
# plt.show()

colors_x = extcolors.extract_from_path(img_url, tolerance=12, limit=12)
colors_pre_list = str(colors_x).replace('([(','').split(', (')[0:-1]
df_rgb  = [i.split('), ')[0] + ')' for i in colors_pre_list]
df_percent = [i.split('), ')[1].replace(')', '') for i in colors_pre_list]
df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(","")),
                          int(i.split(", ")[1]),
                          int(i.split(", ")[2].replace(")",""))) for i in df_rgb]
print("colors_x\n",colors_x)
print("colors_pre_list\n",colors_pre_list)
print("df_rgb\n",df_rgb)
print("df_percent\n",df_percent)
print("df_color_up\n",df_color_up)
# def color_df(input):
#     colors_pre_list = str(input).replace('([(','').split(', (')[0:-1]
#     df_rgb  = [i.split('), ')[0] + ')' for i in colors_pre_list]
#     df_percent = [i.split('), ')[1].replace(')', '') for i in colors_pre_list]
