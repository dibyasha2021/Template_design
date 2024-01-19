import cv2
import numpy as np
from PIL import Image,ImageDraw, ImageFilter
import matplotlib.pyplot as plt


# Load the image
img = cv2.imread("Input_images\images (1).jpg")
cv2.imshow('Image', img)

# Split the image into RGB channels
b, g, r = cv2.split(img)

# Display the individual channels
cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)



# Converting color mode to Grayscale
# as thresholding requires a single channeled image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Apply thresholding to each channel
_, blue_thresholded = cv2.threshold(b, 127, 255, cv2.THRESH_BINARY)
_, green_thresholded = cv2.threshold(g, 127, 255, cv2.THRESH_BINARY)
_, red_thresholded = cv2.threshold(r, 127, 255, cv2.THRESH_BINARY)

# Combine the thresholded channels into a single image
thresholded_image = cv2.merge((blue_thresholded, green_thresholded, red_thresholded))
thresholded_image = cv2.cvtColor(thresholded_image, cv2.COLOR_BGR2RGB)
cv2.imshow('Thresholded_image',thresholded_image )


#cv2.imwrite("output\bags_gray.jpg", img)

#cv2.imshow('Image', th1)


# Waits for a keystroke
cv2.waitKey(0)
 
# Destroys all the windows created
cv2.destroyAllwindows() 