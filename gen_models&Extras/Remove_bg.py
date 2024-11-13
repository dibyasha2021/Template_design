
from PIL import Image,ImageDraw,ImageFont
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import cv2 as cv
from rembg import remove
import os 
# %matplotlib inline

"""width = 600


height = 600


img  = Image.new( mode = "RGB", size = (width, height) , color = (255,255,255) )

img.save("output\canvas.png")
#img.show()

# img = """

def removeBackground(in_path):
    out_path_folder = "/kaggle/working/"
    
    # Store path of the image in the variable input_path 
    input_path =  in_path
    
    # Store path of the output image in the variable output_path 
    output_path = out_path_folder + "outre_" + os.path.basename(input_path).split('/')[-1]
    output_path = output_path.replace("jpg", "png")
    
    # Processing the image 
    input = Image.open(input_path) 

    # Removing the background from the given Image 
    output = remove(input) 
    
    #Saving the Output 
    output.save(output_path)
    
    return output_path

output_path = removeBackground("/kaggle/input/input-data/olay04.jpg")


filename = output_path
with Image.open(filename) as img:
     img.load()

plt.imshow(img)
plt.axis()   # "off"
plt.show()