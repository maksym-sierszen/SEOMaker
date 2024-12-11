import anthropic
from dotenv import load_dotenv
import os
import tkinter as tk

class ClaudeClient:
    def __init__(self, gui): 
        load_dotenv()
        self.gui = gui
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        self.prompt = self.gui.loadDefaultPrompt(self)
    
    
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
        gui.textWindowTab3.delete("1.0", tk.END)
        gui.textWindowTab3.insert("end", message)