import anthropic
from dotenv import load_dotenv
import os
import tkinter as tk
from utils.prompt_loader import load_default_prompt


class ClaudeClient:
    def __init__(self, gui): 
        load_dotenv()
        self.gui = gui
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        self.prompt = load_default_prompt()

    
    
    def createMessage(self):
        inputText = self.gui.paraphraser.extractContent(self.gui.HTMLWindowTab3)
        message = self.client.messages.create(
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
        message = message.content[0].text
        self.gui.textWindowTab3.delete("1.0", tk.END)
        self.gui.textWindowTab3.insert("end", message)