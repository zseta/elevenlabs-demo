from groq import Groq

from models.persona import Persona

class LLMProvider:    
    
    persona_list = [
        Persona(name="Overenthusiastic Football coach",
                prompt="""Act as an overenthusiastic american football Coach."""),
        Persona(name="Overdramatic Soap Actor",
                prompt="""Act as an Overdramatic Soap Actor. emotional, theatrical,
                everything is a crisis"""),
        Persona(name="Pretentious Wine Expert",
                prompt="""Act as a Pretentious Wine Expert. Make the conversation
                about wine.""")
    ]
    
    system_prompt = """You are a talented impersonator chatbot. Provide 20 words max answers."""
    
    def __init__(self, api_key, model_name="llama-3.1-8b-instant"):
        self.model_name = model_name
        self.client = Groq(api_key=api_key)
        
    def persona_names(self):
        return [p.name for p in self.persona_list]
        
    def generate_response(self, persona_name: str, user_query: str):
        persona = next((p for p in self.persona_list if p.name == persona_name), None)
        messages = [
                {"role": "system",
                "content": self.system_prompt},
                {"role": "system", 
                "content": persona.prompt},
                {"role": "user", 
                "content": user_query}
        ]
        response = self.client.chat.completions.create(
                            model=self.model_name,
                            messages=messages,
                        )
        return response.choices[0].message.content
        
        