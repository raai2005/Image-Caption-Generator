# Safe Caption Web

A privacy-focused image caption generator that creates detailed descriptions for your images without ever storing them.

## 🌟 Features

- **Privacy First**: Images are processed in memory and never stored
- **AI-Powered Captions**: Uses Hugging Face's free models for high-quality captions
- **Beautiful UI**: Clean, modern interface with pleasing aesthetics
- **Zero Cost**: Uses free AI services (no paid subscriptions required)
- **Easily Deployable**: Simple to host on Streamlit Sharing or your own server

## 📋 How It Works

1. **Upload Image**: Select any JPG, JPEG, or PNG file
2. **AI Processing**: Your image is sent to the Hugging Face API for analysis
3. **Caption Generation**: A detailed, descriptive caption is created
4. **Memory Cleanup**: All image data is cleared from memory after processing

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

### API Setup (Optional)

The app works without an API key using Hugging Face's anonymous access, but for better rate limits:

1. Create a free Hugging Face account at [huggingface.co](https://huggingface.co/join)
2. Get your API key from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
3. Add it to the `.env` file:

```
HUGGINGFACE_API_KEY=your_huggingface_key_here
```

### Running the App

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
