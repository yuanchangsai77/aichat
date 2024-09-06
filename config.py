# config.py

def load_api_key():
    try:
        from config_local import GOOGLE_API_KEY
    except ImportError:
        try:
            from config_example import GOOGLE_API_KEY
        except ImportError:
            raise ValueError("API key not found.")
    return GOOGLE_API_KEY

# 可以在这里添加其他配置项
MODEL_NAME = "gemini-pro"