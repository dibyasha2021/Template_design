from PIL import Image, ImageDraw, ImageFont,  ImageColor, ImageTk
import numpy as np
import matplotlib.pyplot as plt


im = Image.open(r"output\95.25_01.png")
draw = ImageDraw.Draw(im)
font = ImageFont.truetype(r'assets\fonts\AlumniSansCollegiateOne-Italic.ttf', 70) 
text = 'DO NOT DRINK AND \nDRIVE'
text_size_x,text_size_y = draw.getsize(text, font=font)
text_x = x + (w - text_size_x) // 2
text_y = y + (h - text_size_y) // 2
draw.text((text_x, text_y), text, fill=(26, 110, 129), font=font)

draw.text((10, 20), text, font = font)
im.save(r"output\95.25_01_demo.png")