from utils.get_base_path import get_base_path
import os

def load_default_prompt():
  
    base_path = get_base_path()
    prompt_path = os.path.join(base_path, 'resources', 'prompt.txt')  # Dynamically build the path

    # Open and read the file
    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            prompt = file.read()
        return prompt
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt file not found at {prompt_path}. Please ensure it exists.")
