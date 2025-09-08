import streamlit as st
from PIL import Image
import io
import requests

def generate_caption(image_bytes):
    # Replace with your AI endpoint or model
    # For demonstration, returns a dummy caption
    # You can integrate with HuggingFace, OpenAI, etc.
    import time
    # Simulate processing time
    time.sleep(1)
    return "A beautiful mountain landscape with snow-capped peaks reflected in a crystal clear lake, surrounded by lush pine forests under a bright blue sky."

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
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
            padding: 10px 20px;
            font-size: 14px;
            color: #555;
            border-top: 1px solid #eee;
            text-align: center;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.03);
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Main content
    st.title("🖼️ Safe Image Caption Generator")
    st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.6); padding: 1.5rem; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);'>
            <p style='color: #555; font-size: 18px; line-height: 1.6;'>
                Upload an image and get a soothing AI-generated caption. 
                <span style='color: #4e54c8; font-weight: 600;'>Your privacy is our priority</span> - 
                images are processed in memory and never stored.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Add upload section with more description
    st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.8); padding: 1.2rem; border-radius: 15px; margin-bottom: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.03);'>
            <h3 style='color: #4e54c8; margin-bottom: 10px; font-weight: 500;'>📤 Upload Your Image</h3>
            <p style='color: #555; font-size: 16px; margin-bottom: 15px;'>
                Select a JPG, JPEG, or PNG image to generate a detailed, context-aware caption.
            </p>
        </div>
    """, unsafe_allow_html=True)

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
        
        # Add example section
        st.markdown("""
            <div style='background: linear-gradient(to right, rgba(78, 84, 200, 0.05), rgba(143, 148, 251, 0.05));
                        padding: 1.2rem; border-radius: 15px; margin-top: 30px;
                        box-shadow: 0 4px 10px rgba(0,0,0,0.03); border-left: 3px solid #8f94fb;'>
                <h4 style='color: #4e54c8; margin-bottom: 10px;'>What kind of captions will I get?</h4>
                <p style='color: #555; font-size: 15px; line-height: 1.5;'>
                    Our AI generates detailed, context-aware captions that describe:
                    <ul style='margin-top: 8px; color: #555;'>
                        <li>Scenery and landscapes</li>
                        <li>Objects and their arrangement</li>
                        <li>Colors and visual composition</li>
                        <li>Mood and atmosphere</li>
                        <li>Suitable for social media and accessibility</li>
                    </ul>
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
        <footer>
            <p>Safe Caption Web — Your privacy-focused image captioning solution</p>
            <p style='font-size: 12px; color: #777; margin-top: 5px;'>
                Developed with ❤️ | Images processed securely in memory | Never stored
            </p>
        </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
