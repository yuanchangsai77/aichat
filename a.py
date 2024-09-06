# creative_tools.py

import google.generativeai as genai
from config import load_api_key, MODEL_NAME

# below for image
import base64
from PIL import Image
from io import BytesIO

class CreativeTools:
    def __init__(self):
        self.text_model = self._initialize_model(MODEL_NAME)
        self.vision_model = self._initialize_model('gemini-pro-vision')

    def _initialize_model(self, model_name):
        api_key = load_api_key()
        genai.configure(api_key=api_key,transport='rest')
        return genai.GenerativeModel(model_name)

    def generate_story(self, prompt):
        try:
            response = self.text_model.generate_content(f"Write a short story based on this prompt: {prompt}")
            return response.text
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def generate_poem(self, theme, style):
        try:
            response = self.text_model.generate_content(f"Write a {style} poem about {theme}")
            return response.text
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def generate_character(self, setting):
        try:
            character_description = self.text_model.generate_content(
                f"Create a detailed character description for a character in a {setting} setting. "
                "Include physical appearance, personality traits, and background."
                "Using Simply Chinese as main response"
            ).text

            # image_prompt = f"Create an image of a character based on this description: {character_description}"
            # image_response = self.vision_model.generate_content(image_prompt)
            
            # # 假设 image_response 包含了生成的图像数据
            # # 这里需要根据实际的 API 响应格式来处理图像数据
            # # 以下是一个示例，实际实现可能需要调整
            # image_data = image_response.image
            # image = Image.open(BytesIO(base64.b64decode(image_data)))
            
            # return character_description, image
            return character_description

        except Exception as e:
            return f"An error occurred: {str(e)}", None

    def brainstorm_ideas(self, topic):
        try:
            response = self.text_model.generate_content(f"Brainstorm 5 creative ideas related to {topic}")
            return response.text
        except Exception as e:
            return f"An error occurred: {str(e)}"