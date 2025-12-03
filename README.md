# Deepgram Demo

A [FastAPI](https://fastapi.tiangolo.com/) web application that generates AI-powered audio advice using different personas. Users can select a persona and ask questions to receive audio responses using [Deepgram text-to-speech API](https://developers.deepgram.com/docs/text-to-speech).

See the video how it works: https://www.youtube.com/shorts/7znRT8ROR4c


## Prerequisites
- Python 3.13+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Deepgram](https://deepgram.com/) API key
- [Groq](https://groq.com/) API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/zseta/deepgram-demo.git
cd deepgram-demo
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Create a `.env` file in the project root (see `example.env`):
```
DEEPGRAM_KEY=your_deepgram_api_key
GROQ_KEY=your_groq_api_key
```

## Usage
1. Start the development server:
```bash
cd src
uv run fastapi run app.py --reload
```
1. Open your browser and navigate to `http://localhost:8000`
1. Select a persona from the dropdown menu
1. Enter your question in the text field
1. Submit to receive an audio response

## Dependencies

- **FastAPI**: Web framework for building the API
- **Deepgram**: Text-to-speech API client
- **Groq**: LLM API client for generating text responses
- **python-dotenv**: Environment variable management
- **Jinja2**: Template engine for HTML rendering
- **HTMX**: Minimal frontend interactivity

## Configuration

The application uses the following default settings:

- **LLM Model**: `llama-3.1-8b-instant` (Groq)
- **TTS Model**: Default Deepgram model
- **Audio Format**: MP3 (44.1kHz, 128kbps)
- **Response Length**: Maximum 20 words


To customize TTS settings, modify the parameters in `src/ai_providers/tts_provider.py`.
