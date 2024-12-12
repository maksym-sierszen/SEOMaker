import tkinter as tk
from tkinter import ttk
from utils.prompt_loader import loadDefaultPrompt

from .tabs import create_tab1, create_tab2, create_tab3



class GUI:
    def __init__(self, text_processor, paraphraser, claude_client):
        self.window = tk.Tk()
        self.window.title("SEOMaker v2.2.1")
        self.window.iconbitmap("icon.ico")
        self.window.geometry("800x650")
        self.window.configure(background='white')
        self.window.resizable(False, False)

        self.textProcessor = text_processor
        self.paraphraser = paraphraser
        self.ClaudeClient = claude_client
        self.defaultPrompt = loadDefaultPrompt()

        self.createWidgets()
        self.setupLayout()

    def createWidgets(self):
        self.notebook = ttk.Notebook(self.window)
        self.tab1 = create_tab1(self.notebook, self)
        self.tab2 = create_tab2(self.notebook, self)
        self.tab3 = create_tab3(self.notebook, self)
        self.notebook.add(self.tab1, text="Nowy opis")
        self.notebook.add(self.tab2, text="Parafrazy Manual")
        self.notebook.add(self.tab3, text="Parafrazy API")
        
    

    def setupLayout(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background='lightblue')
        style.map('TNotebook.Tab', background=[('selected', '#008CBA')])

       
        self.notebook.pack(expand=True, fill='both')


    # EXTRACT TO UTILS  
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
    
    #EXTRACT TO UTILS
    def radioSelectionSend(self):
        self.textProcessor.selectedType = self.var.get()