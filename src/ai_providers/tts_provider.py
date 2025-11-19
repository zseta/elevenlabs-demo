from elevenlabs.client import ElevenLabs
from elevenlabs.play import play


class TTSProvider:

    def __init__(self, 
                 api_key: str,
                 voice_id: str ="JBFqnCBsd6RMkjVDRZzb",
                 model_id: str ="eleven_multilingual_v2"):
        self.elevenlabs = ElevenLabs(api_key=api_key)
        self.voice_id = voice_id
        self.model_id = model_id

    def text_to_speech(self, text: str) -> bytes:
        audio = self.elevenlabs.text_to_speech.convert(
            text=text,
            voice_id=self.voice_id,
            model_id=self.model_id,
            output_format="mp3_44100_128",
        )
        return b"".join(audio)
        
if __name__ == "__main__":
    import os, dotenv
    dotenv.load_dotenv()
    
    tts = TTSProvider(api_key=os.environ["ELEVEN_LABS_KEY"])
    tts.text_to_speech("This is a test sentence. Testing!")
