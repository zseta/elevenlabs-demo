# ElevenLabs Demo

A [FastAPI](https://fastapi.tiangolo.com/) web application that generates AI-powered audio advice using different personas. Users can select a persona and ask questions to receive audio responses using [ElevenLabs text-to-speech API](https://elevenlabs.io/docs/capabilities/text-to-speech).


## Prerequisites
- Python 3.13+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [ElevenLabs](https://elevenlabs.io/) API key
- [Groq](https://groq.com/) API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/zseta/elevenlabs-demo.git
cd elevenlabs-demo
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Create a `.env` file in the project root (see `example.env`):
```
ELEVEN_LABS_KEY=your_elevenlabs_api_key
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

## Available Personas

- **Averenthusiastic Football coach**: Overenthusiastic American football coach
- **Overdramatic Soap Actor**: Emotional and theatrical, treats everything as a crisis
- **Pretentious Wine Expert**: Makes every conversation about wine


## Dependencies

- **FastAPI**: Web framework for building the API
- **ElevenLabs**: Text-to-speech API client
- **Groq**: LLM API client for generating text responses
- **python-dotenv**: Environment variable management
- **Jinja2**: Template engine for HTML rendering
- **HTMX**: Minimal frontend interactivity

## Configuration

The application uses the following default settings:

- **LLM Model**: `llama-3.1-8b-instant` (Groq)
- **TTS Voice**: Default ElevenLabs voice
- **TTS Model**: `eleven_multilingual_v2`
- **Audio Format**: MP3 (44.1kHz, 128kbps)
- **Response Length**: Maximum 20 words


To customize TTS settings, modify the parameters in `src/ai_providers/tts_provider.py`.
