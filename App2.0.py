import streamlit as st
from PIL import Image
from BannerCreator import BannerCreator

st.title("Create your custom banner!")

st.header("Input your banner details below:")

# Prompt for the background image
uploaded_background = st.text_input("Prompt for the banner:")


# Upload product image and logo
uploaded_product_image = st.file_uploader("Product Image:")
uploaded_logo = st.file_uploader("Logo:")

# Generate banner function
def generate_banner():

    # **************** Change the background image path here ****************

    background_image_path =r"DEMO\generated\beach_bannerbg04.jpg"
    coords = {}

    if isinstance(uploaded_background, str) :
        if background_image_path == r"DEMO\generated\beach_bannerbg03.png" or r"DEMO\generated\beach_bannerbg04.jpg":
            
            coords.update ({'logo_area': (0, 0), 
                            'image_area': (470, 130), 
                            'content_area': (28, 125), 
                            'clickable_area': (128, 369)
                            })
            banner_creator = BannerCreator(background_image_path, coords)

            banner_creator.attach_content(text=u"Summer Essentials - \n Get yours now!", text_font_path=r"assets\fonts\Lora-SemiBoldItalic.ttf",size_font= 35)
            banner_creator.attach_clickable_area(text=u"Shop Now", text_font_path=r"assets\fonts\YoungSerif-Regular.ttf")

        elif background_image_path == r"DEMO\generated\beach_bannerbg03_1X1_500.jpg":

            coords.update({'logo_area': (415, 0), 
                            'image_area': (232, 198), 
                            'content_area': (24, 83), 
                            'clickable_area': (33, 327)
                            })
            banner_creator = BannerCreator(background_image_path, coords)

            banner_creator.attach_content(text=u"Summer Essentials - \n Get yours now!", text_font_path=r"assets\fonts\Lora-SemiBoldItalic.ttf",size_font= 35 )
            banner_creator.attach_clickable_area(text=u"Shop Now", text_font_path=r"assets\fonts\YoungSerif-Regular.ttf")

    if uploaded_product_image is not None:
        # Get the uploaded file name
        uploaded_filename = uploaded_product_image.name
        
        if uploaded_filename == "product_sunscreen.png":
            banner_creator.attach_image(r"DEMO\Product_suscreen\product_sunscreen.png")
        elif uploaded_filename == "sunscreen_nivea02_r.png":
            banner_creator.attach_image(r"DEMO\Product_suscreen\sunscreen_nivea02_r.png")
        elif uploaded_filename == "Product_sunscreen03.jpg":
            banner_creator.attach_image(r"DEMO\Product_suscreen\Product_sunscreen03.jpg")

    if uploaded_logo is not None:
        # Get the uploaded file name
        uploaded_filename = uploaded_logo.name
        
        if uploaded_filename == "joy-logo.png":
            banner_creator.attach_logo(r"DEMO\Product_suscreen\joy-logo.png")
        elif uploaded_filename == "nivea_logo.png":
            banner_creator.attach_logo(r"DEMO\Product_suscreen\nivea_logo.png")


    
    # Customize download options and filename based on your requirements

    # Banner display
    st.image(banner_creator.background_image)

# Generate banner button
if st.button("Generate Banner!"):
    generate_banner()


# Additional features like download can be added here