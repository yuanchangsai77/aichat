# creative_tools.py

import google.generativeai as genai
from config import load_api_key, MODEL_NAME

class CreativeTools:
    def __init__(self):
        self.model = self._initialize_model()

    def _initialize_model(self):
        api_key = load_api_key()
        genai.configure(api_key=api_key, transport='rest')
        return genai.GenerativeModel(MODEL_NAME)

    def generate_story(self, prompt):
        try:
            response = self.model.generate_content(f"Write a short story based on this prompt: {prompt}")
            return response.text
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def generate_poem(self, theme, style):
        try:
            response = self.model.generate_content(f"Write a {style} poem about {theme}")
            return response.text
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def generate_character(self, setting):
        try:
            response = self.model.generate_content(f"Create a detailed character description for a character in a {setting} setting")
            return response.text
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def brainstorm_ideas(self, topic):
        try:
            response = self.model.generate_content(f"Brainstorm 5 creative ideas related to {topic}")
            return response.text
        except Exception as e:
            return f"An error occurred: {str(e)}"