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
    if isinstance(uploaded_background, str) :
        background_image_path = r"DEMO\generated\beach_bannerbg03.jpg"
    
    coords = {'logo_area': (0, 0), 
              'image_area': (470, 130), 
              'content_area': (28, 125), 
              'clickable_area': (128, 369)
              }

    banner_creator = BannerCreator(background_image_path, coords)

    if uploaded_product_image:
        banner_creator.attach_image("DEMO\Product_suscreen\product_sunscreen.jpg")

    if uploaded_logo:
        banner_creator.attach_logo("DEMO\Product_suscreen\logo.jpg")

    banner_creator.attach_content(text=u"Summer Essentials - \n Get yours now!", text_font_path=r"assets\fonts\Lora-SemiBoldItalic.ttf")
    banner_creator.attach_clickable_area(text=u"Shop Now", text_font_path=r"assets\fonts\Lora-Medium.ttf")

    # Customize download options and filename based on your requirements

    # Banner display
    st.image(banner_creator.background_image)

# Generate banner button
if st.button("Generate Banner!"):
    generate_banner()


# Additional features like download can be added here