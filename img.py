import streamlit as st
from PIL import Image, ImageOps
import io

def invert_image_color(img):
    """Invert colors of the given PIL image."""
    return ImageOps.invert(img)

def main():
    st.title("Image Inverter")

    # Image upload section
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        # Open and display the original image
        image = Image.open(uploaded_file)
        st.image(image, caption='Original Image', use_column_width=True)

        # Invert the image colors
        inverted_image = invert_image_color(image)

        # Display the inverted image
        st.image(inverted_image, caption='Inverted Image', use_column_width=True)

        # Save the inverted image to a temporary buffer
        buf = io.BytesIO()
        inverted_image.save(buf, format="PNG")
        buf.seek(0)

        # Provide a download link for the inverted image
        st.download_button(
            label="Download Inverted Image",
            data=buf,
            file_name="inverted.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()
