import anthropic
from dotenv import load_dotenv
import os
import tkinter as tk
from utils.prompt_loader import load_default_prompt
import time

class ClaudeClient:
    def __init__(self, gui): 
        load_dotenv()
        self.gui = gui
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        self.prompt = load_default_prompt()
        self.MAX_RETRIES = 3
        self.DELAY = 5
    
    
    def createMessage(self):
        inputText = self.gui.paraphraser.extractContent(self.gui.HTMLWindowTab3)
        
        for attempt in range(self.MAX_RETRIES):
            try:
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1000,
                    temperature=0,
                    system= self.prompt,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": inputText
                                }
                            ]
                        }
                    ]
                )
                message = response.content[0].text
                self.gui.textWindowTab3.delete("1.0", tk.END)
                self.gui.textWindowTab3.insert("end", message)
                return
            except Exception as e:
                if attempt < self.MAX_RETRIES -1:
                    print(f"Połączenie {attempt + 1} zawiodło. Ponowna próba za {self.DELAY} sekund...")
                    time.sleep(self.DELAY)
                else:
                    print(f"Przekroczono ilość prób. Spróbuj ponownie później. Error: {e}")
                    self.gui.textWindowTab3.insert("end", f"Przekroczono ilość prób. Spróbuj ponownie później. Error: {e}\n\nSprawdź status dostępności API na https://status.anthropic.com/")