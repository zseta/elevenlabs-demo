from deepgram import (
    DeepgramClient,
)


class TTSProvider:

    def __init__(self, 
                 api_key: str,
                 model_id: str ="aura-2-thalia-en"):
        self.deepgram = DeepgramClient(api_key=api_key)
        self.model_id = model_id

    def text_to_speech(self, text: str) -> bytes:
        audio = self.deepgram.speak.v1.audio.generate(
            text=text,
            model="aura-2-thalia-en"
        )
        return b"".join(audio)
        
if __name__ == "__main__":
    import os, dotenv
    dotenv.load_dotenv()
    
    tts = TTSProvider(api_key=os.environ["DEEPGRAM_KEY"])
    tts.text_to_speech("This is a test sentence. Testing!")
