from dotenv import load_dotenv
import google.generativeai as genai
import os, sys

def load_gemini() -> bool:
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("You need an Gemini API key to run Lumen-Agent.")
        print("Check the docs for more informations.")
        sys.exit()
        return False

    genai.configure(api_key=api_key)
    return True

def change_model(model_name: str = "gemini-2.5-flash-lite"):
    model = genai.GenerativeModel(model_name)

def prompt(prompt_content: str) -> str:
    pass

def reset_chat():
    pass