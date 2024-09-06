import google.generativeai as genai


# 加载api
def load_api_key():
    try:
        from config_local import GOOGLE_API_KEY
    except ImportError:
        try:
            from config_example import GOOGLE_API_KEY
        except ImportError:
            raise ValueError("API key not found.")
    return GOOGLE_API_KEY


# 初始化模型
def initialize_model(model_name="gemini-pro"):
    api_key = load_api_key()
    genai.configure(api_key=api_key, transport='rest')
    return genai.GenerativeModel(model_name)


def generate_story(model, prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")


def main():
    model = initialize_model()

    while True:
        prompt = input("Enter a story prompt (or 'quit' to exit): ")
        if prompt.lower() == 'quit':
            break

        try:
            story = generate_story(model, prompt)
            print("\nGenerated Story:")
            print(story)

        except TimeoutError as te:
            print(f"Error: {te}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()