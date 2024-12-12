import tkinter as tk
from tkinter import ttk
from utils.insert_text import insertText
def create_tab2(parent, self):
        self.tab2 = ttk.Frame(self.notebook)
        
        self.htmlLabelTab2 = tk.Label(self.tab2, text="HTML")
        self.textLabelTab2 = tk.Label(self.tab2, text="Tekst")

        self.HTMLWindowTab2 = tk.Text(self.tab2, height=20, width=30)
        self.textWindowTab2 = tk.Text(self.tab2, height=20, width=30)

        self.transferToTextButtonTab2 = tk.Button(
            self.tab2,
            text="--->",
            command=lambda: insertText(
                self.textWindowTab2,
                self.paraphraser.extractContent(self.HTMLWindowTab2)
            ),
            bg="#008CBA",
            width="15"
        )

        self.transferToHTMLButtonTab2 = tk.Button(
            self.tab2, 
            text="<---", 
            command=lambda: self.paraphraser.addHTML(self.textWindowTab2, self.HTMLWindowTab2), 
            bg="#008CBA", 
            width="15"
        ) 

        self.copyHTMLButtonTab2 = tk.Button(
            self.tab2, 
            text="Kopiuj HTML", 
            command=lambda: self.copyToClipboard(self.HTMLWindowTab2), 
            bg="#008CBA", 
            width="30"
        ) 
        self.copyTextButtonTab2 = tk.Button(
            self.tab2, 
            text="Kopiuj Tekst", 
            command=lambda: self.copyToClipboard(self.textWindowTab2, addPrompt=True), 
            bg="#008CBA", 
            width="30"
        )  

        self.promptLabelTab2 = tk.Label(self.tab2, text="Prompt")
        self.promptTextWindowTab2 = tk.Text(self.tab2, height=10, width= 30)
        self.promptState = tk.BooleanVar(value=False)
        self.promptCheckbuttonTab2 = tk.Checkbutton(
            self.tab2, 
            text="Dodawaj Prompt ", 
            variable=self.promptState
        )
        self.promptTextWindowTab2.insert("1.0", self.defaultPrompt)
        
        # Layout for Tab 2
        paddingx2 = 15
        self.htmlLabelTab2.grid(row=0, column=0, padx=(paddingx2, paddingx2/2), pady=(10, 0))
        self.textLabelTab2.grid(row=0, column=2, padx=(paddingx2/2, paddingx2), pady=(10, 0))

        self.HTMLWindowTab2.grid(row=1, column=0, rowspan=2, padx=(paddingx2, paddingx2/2), pady=(5, 10))
        self.textWindowTab2.grid(row=1, column=2, rowspan=2, padx=(paddingx2/2, paddingx2/2), pady=(5, 10))
        self.transferToTextButtonTab2.grid(row=1, column=1, padx=(paddingx2/2,paddingx2), pady=(5, 10))
        
        self.transferToHTMLButtonTab2.grid(row=2, column=1, padx=(paddingx2/2, paddingx2/2), pady=(5, 10))

        self.copyHTMLButtonTab2.grid(row=3, column=0, padx=(paddingx2, paddingx2/2), pady=(10, 5))
        self.copyTextButtonTab2.grid(row=3, column=2, padx=(paddingx2/2,paddingx2), pady=(10, 5))

        self.promptLabelTab2.grid(row=4, column=0, padx=(paddingx2, paddingx2/2), pady=(10, 0))
        self.promptTextWindowTab2.grid(row=4, column=1, padx=(paddingx2/2, paddingx2/2), pady=(10, 0))
        self.promptCheckbuttonTab2.grid(row=4, column=2, padx=(paddingx2/2,paddingx2), pady=(10, 0))

        return self.tab2