# Image Caption Generator

A versatile image caption generator with both offline local processing and Google's Gemini AI integration.

## 🌟 Features

- **Dual Caption Sources**: Choose between local processing or Google's Gemini AI
- **Privacy Option**: Local mode processes images entirely offline with no data sharing
- **Advanced AI**: Gemini mode provides context-aware, detailed captions
- **Custom Prompts**: Guide the AI to generate captions in specific styles
- **Beautiful UI**: Dark-themed, modern interface with visual feedback
- **Memory Safe**: Images are processed in memory and never stored

## 📋 How It Works

### Application Workflow

1. **Choose Caption Source**: Select between local processing or Gemini AI
2. **Configure Options**: For Gemini mode, customize the prompt if desired
3. **Upload Image**: Select any JPG, JPEG, or PNG file
4. **Processing**: The image is analyzed based on your selected method
5. **View Results**: Get a beautifully displayed, descriptive caption
6. **Memory Cleanup**: All image data is cleared from memory after processing

### Technical Workflow

#### Local Processing Mode:

1. Image is loaded into memory using PIL (Python Imaging Library)
2. Basic properties are extracted (dimensions, aspect ratio)
3. Color analysis identifies dominant colors and brightness
4. Edge detection estimates image complexity
5. Simple heuristics help guess content type
6. Caption is constructed from these analyzed elements

#### Gemini AI Mode:

1. Image is converted to base64 format
2. The application dynamically selects the best available Gemini model
3. Image and custom prompt are sent to Google's Gemini API
4. The AI analyzes the actual content and context of the image
5. A detailed, contextually accurate caption is generated
6. The result is displayed with proper error handling

## 🚀 Getting Started

### Installation

1. Clone this repository:

```bash
git clone https://github.com/raai2005/Image-Caption-Generator.git
cd Image-Caption-Generator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### API Setup

#### For Gemini AI:

1. Create a Google AI Studio account at [ai.google.dev](https://ai.google.dev/)
2. Get your API key from the API Keys section
3. Add it to the `.env` file:

```
GOOGLE_GEMINI_API_KEY=your_gemini_api_key_here
```

### Running the App

Run the application with Streamlit:

```bash
streamlit run app.py
```

The web interface will open in your default browser, typically at [http://localhost:8501](http://localhost:8501).

## 💡 Usage Tips

1. **For quick captions without API setup**: Use the "Local Processing" option which works offline
2. **For detailed, context-aware captions**: Configure your Gemini API key and use the "Gemini AI" option
3. **Customize Gemini prompts**: Try different styles like "Professional", "Gen Z", or your own custom prompt
4. **Image requirements**: For best results, use clear images with good lighting

## 🔍 Tech Stack

- **Streamlit**: Web application framework
- **PIL (Pillow)**: Image processing in local mode
- **Google Generative AI**: Gemini integration for advanced captions
- **Python-dotenv**: Environment variable management

## 🔒 Privacy

- Local processing mode keeps your images entirely on your device
- When using Gemini AI, images are sent to Google's servers for processing according to their [privacy policy](https://ai.google.dev/privacy)
- No images or captions are ever stored persistently by this application

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the application.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

Start the application:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## 🔒 Privacy Details

- **No Image Storage**: Images are processed in memory and deleted immediately
- **No User Tracking**: No cookies or user analytics
- **API Security**: When using Hugging Face API, only the image data is transmitted (no personal information)

## 🛠️ Advanced Configuration

### Using Alternative Models

Edit the `generate_caption()` function in `app.py` to use different Hugging Face models:

```python
# For more artistic captions:
API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"

# For more detailed object descriptions:
API_URL = "https://api-inference.huggingface.co/models/microsoft/git-large-coco"
```

## 📋 Repository Structure

```
app.py           # Main application file with UI and caption generation logic
requirements.txt # Dependencies
.env             # API keys (optional)
README.md        # Documentation
README.md
```

## License

MIT
