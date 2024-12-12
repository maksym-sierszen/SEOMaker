def loadDefaultPrompt():
    with open('prompt.txt', 'r', encoding='utf-8') as file:
        prompt = file.read()
        return prompt