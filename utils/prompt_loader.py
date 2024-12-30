def load_default_prompt():
    with open('utils/prompt.txt', 'r', encoding='utf-8') as file:
        prompt = file.read()
        return prompt