import tkinter as tk
from tkinter import ttk
from utils.insert_text import insertText

def create_tab3(parent, self):
        self.tab3 = ttk.Frame(self.notebook)
        
        self.htmlLabelTab3 = tk.Label(self.tab3, text="HTML")
        self.textLabelTab3 = tk.Label(self.tab3, text="Parafraza Claude")

        self.HTMLWindowTab3 = tk.Text(self.tab3, height=20, width=30)
        self.textWindowTab3 = tk.Text(self.tab3, height=20, width=30)

        self.transferToTextButtonTab3 = tk.Button(
            self.tab3,
            text="Wyślij do Claude -->",
            command=lambda: self.ClaudeClient.createMessage(),
            bg="#008CBA",
            width="15"
        )
        self.transferToHTMLButtonTab3 = tk.Button(
            self.tab3, 
            text="<---", 
            command=lambda: self.paraphraser.addHTML(self.textWindowTab3, self.HTMLWindowTab3), 
            bg="#008CBA", 
            width="15"
        ) 

        self.copyHTMLButtonTab3 = tk.Button(
            self.tab3, 
            text="Kopiuj HTML", 
            command=lambda: self.copyToClipboard(self.HTMLWindowTab3), 
            bg="#008CBA", 
            width="30"
        ) 
        self.copyTextButtonTab3 = tk.Button(
            self.tab3, 
            text="Kopiuj Tekst", 
            command=lambda: self.copyToClipboard(self.textWindowTab3), 
            bg="#008CBA", 
            width="30"
        )  

        self.promptLabelTab3 = tk.Label(self.tab3, text="Prompt")
        self.promptTextWindowTab3 = tk.Text(self.tab3, height=10, width= 30)
        self.promptTextWindowTab3.insert("1.0", self.defaultPrompt)
        
        # Layout for Tab 3
        paddingx2 = 15
        self.htmlLabelTab3.grid(row=0, column=0, padx=(paddingx2, paddingx2/2), pady=(10, 0))
        self.textLabelTab3.grid(row=0, column=2, padx=(paddingx2/2, paddingx2), pady=(10, 0))

        self.HTMLWindowTab3.grid(row=1, column=0, rowspan=2, padx=(paddingx2, paddingx2/2), pady=(5, 10))
        self.textWindowTab3.grid(row=1, column=2, rowspan=2, padx=(paddingx2/2, paddingx2/2), pady=(5, 10))
        self.transferToTextButtonTab3.grid(row=1, column=1, padx=(paddingx2/2,paddingx2), pady=(5, 10))
        
        self.transferToHTMLButtonTab3.grid(row=2, column=1, padx=(paddingx2/2, paddingx2/2), pady=(5, 10))

        self.copyHTMLButtonTab3.grid(row=3, column=0, padx=(paddingx2, paddingx2/2), pady=(10, 5))
        self.copyTextButtonTab3.grid(row=3, column=2, padx=(paddingx2/2,paddingx2), pady=(10, 5))

        self.promptLabelTab3.grid(row=4, column=0, padx=(paddingx2, paddingx2/2), pady=(10, 0))
        self.promptTextWindowTab3.grid(row=4, column=1, padx=(paddingx2/2, paddingx2/2), pady=(10, 0))

        return self.tab3