# LinguaFlow

LinguaFlow is an AI-powered speech translation application designed to convert spoken language into text in another language. The project currently focuses on Malayalam-to-English translation.

## Technologies Used

- Python
- OpenAI Whisper
- IndicTrans2
- PyTorch
- Hugging Face Transformers
- Streamlit
- FFmpeg

## Features

- Audio file upload
- Speech recognition using Whisper
- Machine translation using IndicTrans2
- Interactive web interface built with Streamlit

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd LinguaFlow
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python -m streamlit run app/ui.py
   ```

## Project Status

The application interface and basic translation workflow have been implemented. Malayalam speech recognition and end-to-end translation accuracy are currently being improved.

## Future Improvements

- Improve speech recognition and translation accuracy.
- Add support for additional languages.
- Introduce real-time speech translation.

## License

A license has not yet been specified.
