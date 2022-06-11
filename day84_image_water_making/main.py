# come from Jonathan Lopez's code
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np

def upload_file(text_):
    file = filedialog.askopenfilename()
    #fob = open(file, 'r')
    im = Image.open(file)
    watermark_image = im.copy()
    draw = ImageDraw.Draw(watermark_image)
    font = ImageFont.load_default()

    draw.text((50, 300), str(text_),
              (255, 255, 255), font=font)
    watermark_image.show()

# Window
window = Tk()
window.title("Watermark Editor")
window.minsize(width=400, height=200)
window.config(padx = 100, pady = 50)

#labels
label_text = Label(text ="Put your text:",font=("Arial", 18, "normal"))
label_text.grid(column = 0, row = 1)

text_ = Entry(width=10)
text_.grid(column=0, row=2)

label_upload = Label(text="Upload your image:", font=("Arial", 18, "normal"))
label_upload.grid(column=0, row= 3)

b1 = Button(window, text="Upload File", width=20, command = lambda:upload_file(text_.get()))
b1.grid(row=4,column=0)

window.mainloop()
