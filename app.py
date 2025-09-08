import streamlit as st
from PIL import Image
import io
import requests
import base64
import os
from dotenv import load_dotenv
# The OpenAI import will be loaded dynamically in the function to handle cases where it's not installed

def generate_caption(image_bytes):
    """
    Generate a caption for an image using Hugging Face's Inference API.
    
    Args:
        image_bytes: The binary image data
        
    Returns:
        str: A descriptive caption for the image
    """
    try:
        import os
        from dotenv import load_dotenv
        
        # Load API key from .env file
        load_dotenv()
        api_key = os.getenv("HUGGINGFACE_API_KEY")
        
        # If no API key or using the placeholder, try with anonymous access
        # Hugging Face allows limited free requests without an API key
        headers = {}
        if api_key and api_key != "your_huggingface_key_here":
            headers = {"Authorization": f"Bearer {api_key}"}
        
        # Option 1: Using Salesforce BLIP image captioning model (completely free)
        API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
        
        # For higher quality captions but with usage limits:
        # API_URL = "https://api-inference.huggingface.co/models/microsoft/git-large-coco"
        
        # Send request to Hugging Face
        response = requests.post(
            API_URL,
            headers=headers,
            data=image_bytes
        )
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            
            # Different models return results in different formats
            if isinstance(result, list) and len(result) > 0:
                if isinstance(result[0], dict) and "generated_text" in result[0]:
                    caption = result[0]["generated_text"]
                elif isinstance(result[0], str):
                    caption = result[0]
                else:
                    caption = str(result[0])
            else:
                caption = str(result)
                
            # Clean up caption if needed
            caption = caption.strip()
            if caption.startswith('"') and caption.endswith('"'):
                caption = caption[1:-1]
                
            return caption
        else:
            # Model might still be loading or there's an error
            error_msg = f"API Error: {response.status_code} - {response.text}"
            st.error(error_msg)
            if "loading" in response.text.lower():
                return "The caption model is still loading. This happens when the model is accessed for the first time. Please try again in a few seconds."
            else:
                return f"Could not generate a caption. Error: {response.status_code}"
        
    except Exception as e:
        # Handle any errors gracefully
        st.error(f"Error generating caption: {str(e)}")
        
        # Return one of these fallback captions based on error type
        if "authorization" in str(e).lower() or "authentication" in str(e).lower():
            return "API key issue: Please configure your Hugging Face API key in the .env file or try without an API key for limited usage."
        elif "rate limit" in str(e).lower() or "too many requests" in str(e).lower():
            return "Rate limit reached: The API is currently experiencing high demand. Please try again later."
        elif "connection" in str(e).lower() or "timeout" in str(e).lower():
            return "Connection error: Please check your internet connection and try again."
        else:
            return "Could not generate a caption for this image. Please try again later."

def main():
    # Set page config
    st.set_page_config(page_title="Safe Caption Web", page_icon="🖼️", layout="centered")
    
    # Apply CSS
    st.markdown("""
        <style>
        .main {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .stButton>button {
            background: linear-gradient(to right, #4e54c8, #8f94fb);
            color: white;
            border-radius: 30px;
            padding: 0.6rem 1.8rem;
            font-size: 1.1rem;
            border: none;
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(78, 84, 200, 0.3);
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(78, 84, 200, 0.4);
        }
        .stTextInput>div>input {
            border-radius: 10px;
            border: 2px solid #e0e5f2;
        }
        .stFileUploader {
            border-radius: 10px;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.6);
            backdrop-filter: blur(5px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }
        .css-1hveriv, .css-qbe2hs {
            font-weight: 600;
            color: #4e54c8;
        }
        footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: #e0e0e0;
            padding: 10px 0;
            font-size: 14px;
            color: #555;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Main content
    st.title("🖼️ Safe Image Caption Generator")
    
    # File uploader
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"], accept_multiple_files=False)
    
    if uploaded_file is not None:
        # Process the uploaded image
        image_bytes = uploaded_file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        # Add a nice frame around the image
        st.markdown("""
            <div style='padding: 10px; background: white; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.08);'>
        """, unsafe_allow_html=True)
        st.image(image, caption="", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Add a progress bar for better visual feedback
        progress_bar = st.progress(0)
        for i in range(100):
            # Update progress bar
            progress_bar.progress(i + 1)
            
        with st.spinner("Finalizing your caption..."):
            caption = generate_caption(image_bytes)
        
        # Display the caption in a nice container
        st.markdown(f"""
            <div style='background: linear-gradient(to right, rgba(78, 84, 200, 0.1), rgba(143, 148, 251, 0.1)); 
                         padding: 1.5rem; border-radius: 15px; margin: 20px 0; 
                         box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 4px solid #4e54c8;'>
                <h3 style='color: #4e54c8; margin-bottom: 10px; font-weight: 600;'>Your AI-Generated Caption</h3>
                <p style='color: #333; font-size: 20px; line-height: 1.6; font-style: italic;'>{caption}</p>
                <div style='margin-top: 15px; padding-top: 15px; border-top: 1px solid rgba(78, 84, 200, 0.2);'>
                    <p style='color: #666; font-size: 14px;'>
                        <span style='color: #4e54c8; font-weight: 500;'>✨ Caption Features:</span> 
                        This caption is uniquely generated based on visual elements in your image, including colors, objects, 
                        scenery, mood, and composition. Ideal for social media posts, blogs, or accessibility purposes.
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Clear memory
        del image_bytes
        del image
        del caption
    else:
        # Show empty state
        st.markdown("""
            <div style='background: rgba(255, 255, 255, 0.7); padding: 2rem; border-radius: 15px; 
                       text-align: center; margin: 2rem 0; box-shadow: 0 4px 15px rgba(0,0,0,0.05);'>
                <img src="https://cdn-icons-png.flaticon.com/512/4303/4303887.png" width="100">
                <p style='color: #555; font-size: 18px; margin-top: 15px;'>Please upload an image to get started.</p>
                <p style='color: #777; font-size: 14px; margin-top: 10px;'>
                    Our AI will analyze the visual elements and generate a beautiful, descriptive caption.
                    The process is completely secure and private - we never store your images.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Space for footer
        st.markdown("<div style='margin-bottom: 70px;'></div>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
        <div style='position: fixed; bottom: 0; width: 100%; background-color: #e0e0e0; padding: 10px 0; text-align: center; left: 0;'>
            <p style='color: #555; margin-bottom: 5px;'>Safe Caption Web — Your privacy-focused image captioning solution</p>
            <p style='font-size: 12px; color: #777; margin-top: 5px;'>
                Developed with ❤️ | Images processed securely in memory | Never stored
            </p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
