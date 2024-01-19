from PIL import Image, ImageColor,ImageFilter, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import imageio.v3 as iio

# Necessary imports
import numpy as np
import random
import cv2
import plotly.express as px
import plotly.graph_objs as go
import dash
from dash.dependencies import State

from dash import Dash, dcc, html, Input, Output, no_update, callback
import json
import imageio

import base64
import io
import sys,os 
from rembg import remove

# *********************** Function o create blank canvas for banner **************************
class Canvas:
    def __init__(self, width, height, mode, color):
        self.width = width
        self.height = height
        self.mode = mode
        self.color = color

    def create_canvas(self):
        self.img = Image.new(mode=self.mode, size=(self.width, self.height), color=self.color)

    def save_canvas(self, filename):
        self.img.save(filename)

    def display_canvas(self):
        plt.imshow(self.img)
        plt.axis('off')
        plt.show()

### pattern logo area, Image area,Content area, clickable area 
data = [
  {
    "editable": True,
    "visible": True,
    "showlegend": False,
    "legend": "legend",
    "legendgroup": "",
    "legendgrouptitle": {
      "text": ""
    },
    "legendrank": 1000,
    "label": {
      "text": "",
      "texttemplate": ""
    },
    "xref": "x",
    "yref": "y",
    "layer": "above",
    "opacity": 1,
    "line": {
      "color": "#444",
      "width": 4,
      "dash": "solid"
    },
    "fillcolor": "rgba(0,0,0,0)",
    "fillrule": "evenodd",
    "type": "rect",
    "x0": 30.389284106495445,
    "y0": 32.84582882984952,
    "x1": -0.5,
    "y1": -0.5
  },
  {
    "editable": True,
    "visible": True,
    "showlegend": False,
    "legend": "legend",
    "legendgroup": "",
    "legendgrouptitle": {
      "text": ""
    },
    "legendrank": 1000,
    "label": {
      "text": "",
      "texttemplate": ""
    },
    "xref": "x",
    "yref": "y",
    "layer": "above",
    "opacity": 1,
    "line": {
      "color": "#444",
      "width": 4,
      "dash": "solid"
    },
    "fillcolor": "rgba(0,0,0,0)",
    "fillrule": "evenodd",
    "type": "rect",
    "x0": 59.270187597255195,
    "y0": 26.870469486933715,
    "x1": 300.27634776152627,
    "y1": 194.18053108857643
  },
  {
    "editable": True,
    "visible": True,
    "showlegend": False,
    "legend": "legend",
    "legendgroup": "",
    "legendgrouptitle": {
      "text": ""
    },
    "legendrank": 1000,
    "label": {
      "text": "",
      "texttemplate": ""
    },
    "xref": "x",
    "yref": "y",
    "layer": "above",
    "opacity": 1,
    "line": {
      "color": "#444",
      "width": 4,
      "dash": "solid"
    },
    "fillcolor": "rgba(0,0,0,0)",
    "fillrule": "evenodd",
    "type": "rect",
    "x0": 651.8266557697398,
    "y0": 26.870469486933715,
    "x1": 919.7219329771319,
    "y1": 210.11482266968528
  },
  {
    "editable": True,
    "visible": True,
    "showlegend": False,
    "legend": "legend",
    "legendgroup": "",
    "legendgrouptitle": {
      "text": ""
    },
    "legendrank": 1000,
    "label": {
      "text": "",
      "texttemplate": ""
    },
    "xref": "x",
    "yref": "y",
    "layer": "above",
    "opacity": 1,
    "line": {
      "color": "#444",
      "width": 4,
      "dash": "solid"
    },
    "fillcolor": "rgba(0,0,0,0)",
    "fillrule": "evenodd",
    "type": "rect",
    "x0": 393.89031080054065,
    "y0": 79.65281034935671,
    "x1": 533.3153621352428,
    "y1": 131.43925798796042
  }
]

# ********************** Function to get random coordinate for different Elements of banner  *******************
class CoordinateUtils:
    @staticmethod
    def alignmentCoorMid(data):
        mid_coors_point = {}
        Coor_key= ["logo_area","image_area","content_area", "clickable_area"]
        for j in range(len(Coor_key)):
            x0,y0,x1,y1 = data[j]['x0'],data[j]['y0'],data[j]['x1'],data[j]['y1']
            if x0 > x1:
                x0,x1 = x1,x0
            if y0 > y1:
                y0,y1 = y1,y0
            mid_x = (x0 + x1) / 2
            mid_y = (y0 + y1) / 2
            mid_x, mid_y = max(mid_x, 0), max(mid_y, 0)
            mid_x, mid_y = int(mid_x), int(mid_y)
            mid_coors_point[Coor_key[j]] = (mid_x,mid_y)
        return mid_coors_point

    @staticmethod
    def alignmentCoorTopLeft(data):
        topleft_point = {}
        Coor_key= ["logo_area","image_area","content_area", "clickable_area"]
        for j in range(len(Coor_key)):
            x0,y0,x1,y1 = data[j]['x0'],data[j]['y0'],data[j]['x1'],data[j]['y1']
            if x0 > x1:
                x0,x1 = x1,x0
            if y0 > y1:
                y0,y1 = y1,y0
            top_left_x = x0
            top_left_y = y0
            top_left_x,top_left_y = max(top_left_x, 0), max(top_left_y, 0)
            top_left_x,top_left_y = int(top_left_x), int(top_left_y)
            topleft_point[Coor_key[j]] = (top_left_x,top_left_y)
        return topleft_point

    @staticmethod
    def coordinateValues(data):
        coors = {}
        Coor_key= ["logo_area","image_area","content_area", "clickable_area"]
        for j in range(len(Coor_key)):
            x0,y0,x1,y1 = data[j]['x0'],data[j]['y0'],data[j]['x1'],data[j]['y1']
            coors[Coor_key[j]] = {'x0':x0,'y0': y0,'x1':x1, 'y1': y1}
        return coors



# ********************** Function to paste logo into the defined area of banner  *******************

# Background removal 
def process_image(input,filename):
    output= remove(input)
    #output.save('output_bgremoval\{}'.format())
    return output

# Creating function to paste thumbnail logo into the defined area of banner

def logoAreaAttach(random_point,canvas,filename):
    # Open the image
    img = Image.open(r"Input_images\logo.jpg")
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    
    # Resize the image

    img.thumbnail((random.randint(50, 100), random.randint(50, 100)))
    img =img.resize()
    # Paste the image
    xi,yi = int(random_point["logo_area"][0]+2),int(random_point["logo_area"][1]+2)
    canvas.paste(img, (xi,yi))
    # Save the canvas to a file
    canvas.save(filename)
    return canvas



# Creating function to paste Product image into the defined area of banner

def imageAreaAttach(random_point,input_file,filename):
    # Open the image
    img = Image.open(r"Input_images\sunscreen.jpg")
    if img.mode in ("RGBA", "P"):
      img = img.convert("RGB")

    # Resize the image
    fix = 150
    img=img.resize((fix,fix))
   
    # Paste the image
    xi,yi =  int(random_point['image_area'][0]),int(random_point['image_area'][1])
    canvas.paste(img, (xi,yi))

    # Save the canvas to a file
    canvas.save(filename)
    return canvas

# Creating function to paste Text content into the defined area of banner
def contentAreaAttach(random_point,input_file,filename):
    
    # Open the image
    image = Image.open(input_file)

    # Specify the text to be added
    text = " Product \n Content \n Test"

    # Set the font, scale, color, and thickness of the text
    font = ImageFont.truetype(r'assets\fonts\TiltNeon-Regular-VariableFont_XROT,YROT.ttf', size=50)
    color = 'white'  # RGB format
    
    # Generate random coordinates
    x, y = int(random_point['content_area'][0]),int(random_point['content_area'][1])
   
    # Add the text to the image
    draw = ImageDraw.Draw(image)
    draw.text((x, y), text, font=font, fill=(0,0,0))

    # Save the image
    image.save(filename)

    return image


# Creating function to paste Shop now into the defined area of banner
def clickableAreaAttach(random_point, image_path, filename):
    # Open the image
    image = Image.open(image_path)

    # Create a rectangle box
    x, y, w, h = random_point[0], random_point[1], 150, 50
    draw = ImageDraw.Draw(image)
    draw.rectangle([(x, y), (x + w, y + h)], outline=(0, 0, 0), width=1)

    # Add text inside the box
    text = u"Shop Now"
    font = ImageFont.truetype(r"assets\fonts\Lora-Medium.ttf", 30)  # Replace "arial.ttf" with the path to your desired font file
    """    text_size_x,text_size_y = draw.getsize(text, font=font)
    text_x = x + (w - text_size_x) // 2
    text_y = y + (h - text_size_y) // 2"""
    draw.text((x+5,y+5), text, fill=(26, 110, 129), font=font)

    # Save the image
    image.save(filename)

    # Return the modified image
    return image


"""#Creating function to paste Text content into the defined area of banner
## Get input from the user

width = int(input("Enter width: "))
height = int(input("Enter height: "))
#mode = input("Enter mode (e.g. RGB, RGBA, CMYK): ")
#color = tuple(map(int, input("Enter color as three space-separated integers (e.g. 223 227 216): ").split()))
#239 219 176

# Create an instance of the Canvas class
canvas = Canvas(width, height, mode ="RGB", color = (239 219 176))

# Create the canvas
canvas.create_canvas()

# Save the canvas to a file
filename = input("Enter output file name: ") #1.2_01.png
canvas.save_canvas("output\{}".format(filename))

# Display the canvas
canvas.display_canvas()"""


# Usage
coordinate_utils = CoordinateUtils()
mid_coors_point = coordinate_utils.alignmentCoorMid(data)
topleft_point = coordinate_utils.alignmentCoorTopLeft(data)
coors = coordinate_utils.coordinateValues(data)

#canvas =Image.open(r"DEMO\97_25_05.png")
points = topleft_point
print(points)
"""logoAreaAttach(points,canvas,filename="DEMO\97_25_05_l.png")


imageAreaAttach(points,input_file ="DEMO\97_25_05_l.png",filename = "DEMO\97_25_05_li.png")
contentAreaAttach(points,input_file = "DEMO\97_25_05_li.png",filename="DEMO\97_25_05_lic.png")
clickableAreaAttach(random_point=points["clickable_area"],image_path="DEMO\97_25_05_lic.png",filename="DEMO\97_25_05_final.png")

"""