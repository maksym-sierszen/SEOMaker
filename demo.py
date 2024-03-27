import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("SEOMaker v2.0")
        self.window.iconbitmap("icon.ico")
        self.window.geometry("500x250")
        self.window.configure(bg='white')  
        self.window.resizable(False,False)
    
        notebook = ttk.Notebook(self.window)
        
        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)

        notebook.add(tab1, text="Nowy opis")
        notebook.add(tab2, text="Parafrazy")
        notebook.pack()

    def run(self):
        self.window.mainloop()
        

gui = GUI()
gui.run()