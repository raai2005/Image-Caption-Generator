# Safe Caption Web

A soothing, privacy-focused image caption generator built with Streamlit.

## Features

- Upload images securely (handled in memory, never stored)
- AI-generated captions (customizable with your own model/API)
- Beautiful, calming web UI
- Easy to deploy and share

## How to Run Locally

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Start the app:
   ```
   streamlit run app.py
   ```
3. Open your browser at `http://localhost:8501`

## How to Deploy for Public Use

- **Streamlit Community Cloud:**
  1. Push your code to GitHub.
  2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and deploy your app.
- **Other options:** Heroku, AWS, Azure, GCP, etc.

## Customizing the Caption Model

- The default `generate_caption` function returns a placeholder.
- Integrate your own AI model or API (e.g., HuggingFace, OpenAI) in `app.py`.

## Repository Structure

```
app.py
requirements.txt
README.md
```

## License

MIT
