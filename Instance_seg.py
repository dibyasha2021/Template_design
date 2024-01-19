import cv2
import numpy as np
from PIL import Image,ImageDraw, ImageFilter
import matplotlib.pyplot as plt
import pixellib
from pixellib.instance import instance_segmentation
import tensorflow as tf

segment_image = instance_segmentation()
segment_image.load_model("assets\models\mask_rcnn_coco.h5")



segment_image.segmentImage("Input_images\download.jpg", output_image_name = "output\seg_down01.jpg")

#Display Segmented Image
img = cv2.imread("output\seg_down01.jpg")
cv2.imshow('Segemented Image', img)



#Extraction of Segmented Objects



# Waits for a keystroke
cv2.waitKey(0)
 
# Destroys all the windows created
cv2.destroyAllwindows() 