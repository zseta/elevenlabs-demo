import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import base64

from ai_providers.tts_provider import TTSProvider
from ai_providers.llm_provider import LLMProvider


load_dotenv()
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

tts = TTSProvider(api_key=os.environ["ELEVEN_LABS_KEY"])
llm = LLMProvider(api_key=os.environ["GROQ_KEY"])

user_query_examples = [
    "How to make pancake?",
    "How to build a house?",
    "I want to become a football player"
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    context = {
        "request": request,
        "personas": llm.persona_names(),
        "input_examples": user_query_examples
    }
    return templates.TemplateResponse("index.html", context)

@app.post("/audio-advice", response_class=HTMLResponse)
async def audio_advice(request: Request,
                       persona: str = Form(...),
                       user_query: str = Form(...)):    
    text_advice = llm.generate_response(persona, user_query)
    print(text_advice)
    audio = tts.text_to_speech(text_advice)
    audio_base64 = base64.b64encode(audio).decode('utf-8')
    context = {"request": request,
               "audio_data": audio_base64}
    return templates.TemplateResponse("audio_advice.html", context)


