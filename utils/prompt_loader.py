from utils.get_base_path import get_project_root
import os

def load_default_prompt():
    base_path = get_project_root()  # Get the project root directory
    prompt_path = os.path.join(base_path, 'resources', 'prompt.txt')  

    # Open the file dynamically based on the constructed path
    with open(prompt_path, 'r', encoding='utf-8') as file:
        prompt = file.read()
        return prompt
