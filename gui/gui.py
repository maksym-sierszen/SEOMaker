# gui/gui.py
import tkinter as tk
from tkinter import ttk
from utils.prompt_loader import loadDefaultPrompt

class GUI:
    def __init__(self, TextProcessorClass, ParaphraserClass):
        self.window = tk.Tk()
        self.window.title("SEOMaker v2.2.0")
        self.window.iconbitmap("icon.ico")
        self.window.geometry("800x650")
        self.window.configure(background='white')
        self.window.resizable(False, False)
        
        # Inicjalizujemy prompt
        self.defaultPrompt = loadDefaultPrompt()
        
        # Tworzymy instancje przekazanych klas, zamiast importować je tutaj
        self.textProcessor = TextProcessorClass(self)
        self.paraphraser = ParaphraserClass(self)
        
        # ClaudeClient będzie przypisany w main.py po utworzeniu GUI
        self.ClaudeClient = None

        notebook = ttk.Notebook(self.window)
        
        # --- Poniżej umieść kod GUI z zakładkami (Tab1, Tab2, Tab3) ---
        # Bez zmian w logice, wszystkie odwołania do gui zmieniamy na self.
        
        # Tab1
        tab1 = ttk.Frame(notebook)
        
        self.textLabelTab1 = tk.Label(tab1, text="Tekst")
        self.htmlLabelTab1 = tk.Label(tab1, text="HTML")
        
        self.textWindowTab1 = tk.Text(tab1, height=20, width=30)
        self.HTMLWindowTab1 = tk.Text(tab1, height=20, width=30)
        self.transferToHTMLButtonTab1 = tk.Button(
            tab1, 
            text="--->", 
            command=self.textProcessor.generateSEO, 
            bg="#008CBA", 
            width="15"
        )
        
        self.copyHTMLButtonTab1 = tk.Button(tab1, text="Kopiuj HTML", command=lambda: self.copyToClipboard(self.HTMLWindowTab1), bg="#008CBA", width="30")
        
        self.imageNameTab1 = tk.Label(tab1, text="Nazwy grafik")
        self.imageNameEntryTab1 = tk.Entry(tab1, width=20)
        self.copyNameButtonTab1 = tk.Button(tab1, text="Kopiuj nazwę", command=lambda: self.copyToClipboard(self.imageNameEntryTab1), bg="#008CBA")
        
        self.var = tk.IntVar()
        self.centerRadioTab1 = tk.Radiobutton(tab1, text="CENTER", variable=self.var, value=1, command=self.radioSelectionSend)
        self.leftRadioTab1 = tk.Radiobutton(tab1, text="LEWO", variable=self.var, value=2, command=self.radioSelectionSend)
        self.miniRadioTab1 = tk.Radiobutton(tab1, text="MINI", variable=self.var, value=3, command=self.radioSelectionSend)
        
        paddingx1 = 50
        self.centerRadioTab1.grid(row=0, column=0, padx=(paddingx1, paddingx1/2), pady=(20, 0))
        self.leftRadioTab1.grid(row=0, column=1, padx=(paddingx1/2, paddingx1/2), pady=(20, 0))
        self.miniRadioTab1.grid(row=0, column=2, padx=(paddingx1/2, paddingx1), pady=(20, 0))

        self.textLabelTab1.grid(row=1, column=0, padx=(paddingx1, paddingx1/2), pady=(20, 0))
        self.htmlLabelTab1.grid(row=1, column=2, padx=(paddingx1/2, paddingx1), pady=(20, 0))

        self.textWindowTab1.grid(row=2, column=0, padx=(paddingx1, paddingx1/2), pady=(5, 10))
        self.transferToHTMLButtonTab1.grid(row=2, column=1, padx=(paddingx1/2, paddingx1/2), pady=10)
        self.HTMLWindowTab1.grid(row=2, column=2, padx=(paddingx1/2, paddingx1), pady=(5, 10))

        self.copyHTMLButtonTab1.grid(row=3, column=2, padx=(paddingx1/2, paddingx1), pady=10)
                        
        self.imageNameTab1.grid(row=4, column=0, pady=30)
        self.imageNameEntryTab1.grid(row=4, column=1, pady=30)
        self.copyNameButtonTab1.grid(row=4, column=2, pady=30)

        # Tab2
        tab2 = ttk.Frame(notebook)
      
        self.htmlLabelTab2 = tk.Label(tab2, text="HTML")
        self.textLabelTab2 = tk.Label(tab2, text="Tekst")

        self.HTMLWindowTab2 = tk.Text(tab2, height=20, width=30)
        self.textWindowTab2 = tk.Text(tab2, height=20, width=30)

        self.transferToTextButtonTab2 = tk.Button(
            tab2,
            text="--->",
            command=lambda: self.paraphraser.insertText(
                self.textWindowTab2,
                self.paraphraser.extractContent(self.HTMLWindowTab2)
            ),
            bg="#008CBA",
            width="15"
        )

        self.transferToHTMLButtonTab2 = tk.Button(tab2, text="<---", command=lambda: self.paraphraser.addHTML(self.textWindowTab2, self.HTMLWindowTab2), bg="#008CBA", width="15") 

        self.copyHTMLButtonTab2 = tk.Button(tab2, text="Kopiuj HTML", command=lambda: self.copyToClipboard(self.HTMLWindowTab2), bg="#008CBA", width="30") 
        self.copyTextButtonTab2 = tk.Button(tab2, text="Kopiuj Tekst", command=lambda: self.copyToClipboard(self.textWindowTab2, addPrompt=True), bg="#008CBA", width="30")  

        self.promptLabelTab2 = tk.Label(tab2, text="Prompt")
        self.promptTextWindowTab2 = tk.Text(tab2, height=10, width= 30)
        self.promptState = tk.BooleanVar(value=False)
        self.promptCheckbuttonTab2 = tk.Checkbutton(tab2, text="Dodawaj Prompt ", variable=self.promptState)
        self.promptTextWindowTab2.insert("1.0", self.defaultPrompt)

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

        # Tab3
        tab3 = ttk.Frame(notebook)
        self.htmlLabelTab3 = tk.Label(tab3, text="HTML")
        self.textLabelTab3 = tk.Label(tab3, text="Parafraza Claude")

        self.HTMLWindowTab3 = tk.Text(tab3, height=20, width=30)
        self.textWindowTab3 = tk.Text(tab3, height=20, width=30)

        self.transferToTextButtonTab3 = tk.Button(
            tab3,
            text="Wyślij do Claude -->",
            command=lambda: self.ClaudeClient.createMessage() if self.ClaudeClient else None,
            bg="#008CBA",
            width="15"
        )
        self.transferToHTMLButtonTab3 = tk.Button(tab3, text="<---", command=lambda: self.paraphraser.addHTML(self.textWindowTab3, self.HTMLWindowTab3), bg="#008CBA", width="15") 

        self.copyHTMLButtonTab3 = tk.Button(tab3, text="Kopiuj HTML", command=lambda: self.copyToClipboard(self.HTMLWindowTab3), bg="#008CBA", width="30") 
        self.copyTextButtonTab3 = tk.Button(tab3, text="Kopiuj Tekst", command=lambda: self.copyToClipboard(self.textWindowTab3), bg="#008CBA", width="30")  

        self.promptLabelTab3 = tk.Label(tab3, text="Prompt")
        self.promptTextWindowTab3 = tk.Text(tab3, height=10, width=30)
        self.promptTextWindowTab3.insert("1.0", self.defaultPrompt)

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

        style=ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background='lightblue')
        style.map('TNotebook.Tab', background=[('selected', '#008CBA')])

        notebook.add(tab1, text="Nowy opis")
        notebook.add(tab2, text="Parafrazy Manual")
        notebook.add(tab3, text="Parafrazy API")
        
        notebook.pack(expand=True, fill='both')

    def copyToClipboard(self, widget, addPrompt=False):
        if addPrompt and self.promptState.get():
            promptContent = self.promptTextWindowTab2.get("1.0", "end-1c")+ "\n\n"
        else:
            promptContent = ""
        
        if isinstance(widget, tk.Entry):
            valueToCopy = widget.get()
        elif isinstance(widget, tk.Text):
            valueToCopy = widget.get("1.0", "end-1c")
        else:
            valueToCopy = ""
        
        valueToCopy = promptContent + valueToCopy
        
        self.window.clipboard_clear()
        self.window.clipboard_append(valueToCopy)

    def run(self):
        self.window.mainloop()

    def radioSelectionSend(self):
        self.textProcessor.selectedType = self.var.get()
