import streamlit as st
from PIL import Image
import io
import requests

def generate_caption(image_bytes):
    # Replace with your AI endpoint or model
    # For demonstration, returns a dummy caption
    # You can integrate with HuggingFace, OpenAI, etc.
    return "A beautiful image uploaded by the user."

st.set_page_config(page_title="Safe Image Caption Generator", page_icon="🖼️", layout="centered")
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 4px 24px rgba(0,0,0,0.08);
    }
    .stButton>button {
        background-color: #6a89cc;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-size: 1.1rem;
        border: none;
    }
    .stTextInput>div>input {
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🖼️ Safe Image Caption Generator")
st.write("Upload an image and get a soothing AI-generated caption. Your image is never stored.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

if uploaded_file is not None:
    image_bytes = uploaded_file.read()
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, caption="Uploaded Image", use_column_width=True)
    with st.spinner("Generating caption..."):
        caption = generate_caption(image_bytes)
    st.success(f"Caption: {caption}")
    # Clear memory
    del image_bytes
    del image
    del caption
else:
    st.info("Please upload an image to get started.")
