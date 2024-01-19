# Necessary imports

from PIL import Image, ImageDraw, ImageFont,ImageFilter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


import os

class BannerCreator:
    def __init__(self, background_image_path, coords):
        # Open the background image
        try:
            self.background_image = Image.open(background_image_path)
        except FileNotFoundError:
            print(f"Error: Background image file not found at '{background_image_path}'.")
            raise

        # Validate and store coordinates
        if not isinstance(coords, dict):
            raise TypeError("Invalid argument type for `coords`. Expected a dictionary.")
        for key in ("logo_area", "image_area", "content_area", "clickable_area"):
            if key not in coords or not isinstance(coords[key], tuple):
                raise ValueError(f"Missing or invalid entry for '{key}' in `coords`.")
        self.coords = coords

    def attach_logo(self, logo_path):
        def erode(cycles, image):
            for _ in range(cycles):
                image = image.filter(ImageFilter.MinFilter(3))
            return image
        def dilate(cycles, image):
            for _ in range(cycles):
                image = image.filter(ImageFilter.MaxFilter(3))
            return image
        
        if logo_path == "DEMO\Product_suscreen\joy-logo.png":
            # Open the logo image
            
            try:
                logo = Image.open(logo_path).convert("RGB")
            except FileNotFoundError:
                print(f"Error: Logo image file not found at '{logo_path}'.")
                raise

            red, green,blue = logo.split()
            threshold = 30
            img_th2 = blue.point(lambda x: 255 if x < threshold else 0)
            img_th2= img_th2.convert("1")
            step_1 = erode(1, img_th2)
            step_1 = step_1.point(lambda x: 0 if x == 255 else 255)
            mask = erode(2, step_1)
            mask = mask.convert("L")
            mask = mask.filter(ImageFilter.BoxBlur(5))
            # Resize the logo based on area definition
            resize_image = logo.resize((logo.width // 7, logo.height // 7))
            resize_mask = mask.resize((mask.width // 7, mask.height // 7))

        elif logo_path == r"DEMO\Product_suscreen\nivea_logo.png":
            # Open the logo image
            
            try:
                logo = Image.open(logo_path).convert("RGB")
            except FileNotFoundError:
                print(f"Error: Logo image file not found at '{logo_path}'.")
                raise
            logo = logo.crop((70,40,190,160))
            red, green,blue = logo.split()
            threshold = 100
            img_th2 = red.point(lambda x: 255 if x > threshold else 0)
            img_th2= img_th2.convert("1")
            step_1 = erode(1, img_th2)
            step_1 = step_1.point(lambda x: 0 if x == 255 else 255)
            step_2 = dilate(3,step_1)
            mask = erode(2, step_2)
            mask = mask.convert("L")
            mask = mask.filter(ImageFilter.BoxBlur(5))
            # Resize the logo based on area definition
            resize_image = logo.resize((logo.width// 2, logo.height // 2))
            resize_mask = mask.resize((mask.width // 2, mask.height // 2)) 
        
        # Paste the logo at specified coordinates with offset
        x, y = self.coords["logo_area"][0], self.coords["logo_area"][1]
        self.background_image.paste(resize_image,(x+10, y+10),resize_mask)

    def attach_image(self, image_path):

        # fuctions for Erode and Dilate
        def erode(cycles, image):
            for _ in range(cycles):
                image = image.filter(ImageFilter.MinFilter(3))
            return image
        def dilate(cycles, image):
            for _ in range(cycles):
                image = image.filter(ImageFilter.MaxFilter(3))
            return image



        if image_path == r"DEMO\Product_suscreen\product_sunscreen.jpg" or r"DEMO\Product_suscreen\product_sunscreen.png" :
            # Open the original image 
            image = Image.open(image_path).convert('RGB')
            red, green,blue = image.split()
            threshold = 150
            img_th2 = blue.point(lambda x: 255 if x > threshold else 0)
            img_th2= img_th2.convert("1")


            step_1 = erode(18, img_th2)
            step_1 = step_1.point(lambda x: 0 if x == 255 else 255)
            step_2 = dilate(30,step_1)
            mask = erode(45, step_2)
            mask = mask.convert("L")
            mask = mask.filter(ImageFilter.BoxBlur(15))
            blank = image.point(lambda _: 0)
            segmented = Image.composite(image, blank,mask)
            resize_image = image.resize((image.width // 2, image.height // 2))
            resize_mask = mask.resize((mask.width // 2, mask.height // 2))

        elif image_path == r"DEMO\Product_suscreen\sunscreen_nivea02.png" :
            # Open the original image 
            image = Image.open(image_path).convert('RGB')
            # Crop the image if needed
            #image = image.crop((390,80,610,610))
            # resize the image
            #image = image.resize((image.width // 2, image.height // 2))
            red, green,blue = image.split()
            threshold = 250
            img_th2 = green.point(lambda x: 255 if x < threshold else 0)
            img_th2= img_th2.convert("1")


            step_1 = erode(5, img_th2)
            step_2 = dilate(15,step_1)
            mask = erode(6, step_2)
            mask = mask.convert("L")
            mask = mask.filter(ImageFilter.BoxBlur(20))

            resize_image = image.resize((image.width// 2, image.height // 2))
            resize_mask = mask.resize((mask.width // 2, mask.height // 2))
        
        elif image_path == r"DEMO\Product_suscreen\Product_sunscreen03.jpg" :
            # Open the original image 
            image = Image.open(image_path).convert('RGB')
            # Crop the image if needed
            image = image.crop((300,60,700,940))
            # split the colors RGB
            red, green,blue = image.split()
            threshold = 250
            img_th2 = green.point(lambda x: 255 if x < threshold else 0)
            img_th2= img_th2.convert("1")


            step_1 = erode(3, img_th2)
            step_2 = dilate(12,step_1)
            mask = erode(3, step_2)
            mask = mask.convert("L")
            mask = mask.filter(ImageFilter.BoxBlur(20))

            resize_image = image.resize((image.width// 3, image.height // 3))
            resize_mask = mask.resize((mask.width // 3, mask.height // 3))

        else:
            print("Image not found!")


        
        
        # Paste the image at specified coordinates


        x, y = self.coords["image_area"][0], self.coords["image_area"][1]
        self.background_image.paste(resize_image,(x,y),resize_mask,)

    def attach_content(self, text, text_font_path, size_font ,text_color=(0, 0, 0)):
        # Validate text and font path
        if not isinstance(text, str):
            raise TypeError("Invalid type for `text`. Expected a string.")
        if not os.path.isfile(text_font_path):
            raise FileNotFoundError(f"Font file not found at '{text_font_path}'.")

        # Load the font and draw the text
        font_size = size_font
        font = ImageFont.truetype(text_font_path, size= font_size)
        x, y = self.coords["content_area"][0], self.coords["content_area"][1]
        draw = ImageDraw.Draw(self.background_image)
        draw.text((x, y), text, font=font, fill=text_color)

    def attach_clickable_area(self,text_font_path, text=u"Shop Now", text_color=(0,0,0)):
        # Validate text and font path
        if not isinstance(text, str):
            raise TypeError("Invalid type for `text`. Expected a string.")
        if not os.path.isfile(text_font_path):
            raise FileNotFoundError(f"Font file not found at '{text_font_path}'.")

        # Define area and rectangle properties
        x, y, = self.coords["clickable_area"]
        w, h = 170, 50
        draw = ImageDraw.Draw(self.background_image)
        draw.rectangle([(x, y), (x + w, y + h)], outline=(0, 0, 0), width=2)

        # Load the font and draw the text inside the rectangle
        font = ImageFont.truetype(text_font_path, size=30)
        draw.text((x + 5, y + 5), text, fill=text_color, font=font)

    def create_banner(self, filename):
        # Save the banner to a file
        self.background_image.save(filename)

    # Display the banner to a file (if desired)
    def display_canvas(self):
        plt.imshow(self.background_image)
        plt.title("Final Product")
        plt.axis()
        plt.show()
      