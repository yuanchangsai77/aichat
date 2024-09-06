# app.py

import gradio as gr
from a import CreativeTools
from styles import css

class CreativeWritingAssistant:
    def __init__(self):
        self.tools = CreativeTools()

    def generate_story(self, prompt):
        return self.tools.generate_story(prompt)

    def generate_poem(self, theme, style):
        return self.tools.generate_poem(theme, style)

    def generate_character(self, setting):
        return self.tools.generate_character(setting)

    def brainstorm_ideas(self, topic):
        return self.tools.brainstorm_ideas(topic)

    @staticmethod
    def clear_output():
        return "", None  # 清除文本输出和图像

    def create_app(self):
        with gr.Blocks(css=css) as app:
            gr.HTML("<h1 class='title'>Creative Writing Assistant</h1>")
            
            with gr.Tabs():
                with gr.TabItem("Story Generator"):
                    story_prompt = gr.Textbox(label="Enter your story prompt", lines=3)
                    story_output = gr.Textbox(label="Generated Story", lines=10)
                    story_button = gr.Button("Generate Story")

                with gr.TabItem("Poem Generator"):
                    poem_theme = gr.Textbox(label="Enter poem theme")
                    poem_style = gr.Dropdown(["Sonnet", "Haiku", "Free Verse", "Limerick"], label="Select poem style")
                    poem_output = gr.Textbox(label="Generated Poem", lines=10)
                    poem_button = gr.Button("Generate Poem")

                with gr.TabItem("Character Creator"):
                    character_setting = gr.Textbox(label="Enter character setting")
                    character_output = gr.Textbox(label="Generated Character", lines=10)
                    # character_image = gr.Image(label="Character Image")
                    character_button = gr.Button("Create Character")

                with gr.TabItem("Idea Brainstormer"):
                    idea_topic = gr.Textbox(label="Enter topic for brainstorming")
                    idea_output = gr.Textbox(label="Brainstormed Ideas", lines=10)
                    idea_button = gr.Button("Brainstorm Ideas")

            clear_button = gr.Button("Clear All Outputs")

            story_button.click(self.generate_story, inputs=story_prompt, outputs=story_output)
            poem_button.click(self.generate_poem, inputs=[poem_theme, poem_style], outputs=poem_output)
            # character_button.click(self.generate_character, inputs=character_setting, outputs=[character_output, character_image])
            character_button.click(self.generate_character, inputs=character_setting, outputs=[character_output])            
            idea_button.click(self.brainstorm_ideas, inputs=idea_topic, outputs=idea_output)
            
            # clear_button.click(self.clear_output, 
            #                    outputs=[story_output, poem_output, character_output, character_image, idea_output])
            clear_button.click(self.clear_output, 
                               outputs=[story_output, poem_output, character_output, idea_output])

        return app

if __name__ == "__main__":
    creative_assistant = CreativeWritingAssistant()
    app = creative_assistant.create_app()
    app.launch()