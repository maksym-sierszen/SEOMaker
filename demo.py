import tkinter as tk
from tkinter import ttk


class TextProcessor:
    def __init__(self, gui):
        self.gui = gui
        self.productDescription = ""
        self.paragraphs = []
        self.productName = ""
        self.template = ""
        self.readyToUse = ""
        self.imageFileName = ""
    
    def getData(self):
        self.productDescription = self.gui.textWindowTab1.get("1.0", "end-1c")
        self.paragraphs = self.productDescription.split('\n')
        # Usuwanie pustych elementów
        self.paragraphs = list(filter(lambda par: par != "", self.paragraphs)) 
        self.productName = self.paragraphs[0]
        self.paragraphs.pop(0)
        print(self.paragraphs[0])

    def generateImageFileName(self, productName):
        imageFileNameBase = self.productName
        polishLetters = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
        for letter in polishLetters:
          imageFileNameBase = imageFileNameBase.replace(letter, polishLetters[letter])

        imageFileNameBase = imageFileNameBase.lower()

        symbolsToChange = [".", ",", "`", ":", ";", "/", "'"," ", "]", "[", "~", "<", ">","+", "=", "|"]
        for symbol in symbolsToChange:
            if symbol in imageFileNameBase:
                imageFileNameBase = imageFileNameBase.replace(symbol, "-")

        while '--' in imageFileNameBase:
            imageFileNameBase = imageFileNameBase.replace('--', '-')

        for i in range(1, 5):
            self.imageFileName = f"{imageFileNameBase}-{i}"
            self.readyToUse = self.readyToUse.replace(f"IMAGENAME{i}", self.imageFileName)
        
        gui.imageNameEntryTab1.delete(0, tk.END)
        gui.imageNameEntryTab1.insert(0, imageFileNameBase) 

     
     
    def fillTemplate(self, productName, paragraphs):
        with open("template.txt", "r", encoding="utf-8") as file:
            self.template = file.read()

        replacements = {
            "ALTTEXT": self.productName,
            "PRODUCTNAME": self.productName,
            "TEXT1": self.paragraphs[0],
            "HEADER2": self.paragraphs[1],
            "TEXT2": self.paragraphs[2],
            "HEADER3": self.paragraphs[3],
            "TEXT3": self.paragraphs[4],
            "HEADER4": self.paragraphs[5],
            "TEXT4": self.paragraphs[6]
        }

        self.readyToUse = self.template


        for key, value in replacements.items():
            self.readyToUse = self.readyToUse.replace(key, value)

     
    def generateSEO(self):
        self.getData()
        self.fillTemplate(self.productName, self.paragraphs)
        self.generateImageFileName(self.productName)
        
        print(self.readyToUse)
        
        gui.HTMLWindowTab1.delete("1.0", tk.END)  # Najpierw usuń obecny tekst
        gui.HTMLWindowTab1.insert("1.0", self.readyToUse)


    
class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("SEOMaker v2.0")
        self.window.geometry("750x500")
        self.window.configure(bg='white')
        self.window.resizable(False, False)
        self.textProcessor = TextProcessor(self)

        notebook = ttk.Notebook(self.window)
        
        # Tab for new files (tab1)
        tab1 = ttk.Frame(notebook)
        
        self.textLabelTab1 = tk.Label(tab1, text="Tekst")
        self.htmlLabelTab1 = tk.Label(tab1, text="HTML")
        
        self.textWindowTab1 = tk.Text(tab1, height=20, width=30)
        self.HTMLWindowTab1 = tk.Text(tab1, height=20, width=30)
        self.transferToHTMLButtonTab1 = tk.Button(tab1, text="--->", command=self.textProcessor.generateSEO)
        
        self.copyHTMLButtonTab1 = tk.Button(tab1, text="Kopiuj HTML", command=lambda: self.copyToClipboard(self.HTMLWindowTab1))
        
        self.imageNameTab1 = tk.Label(tab1, text="Nazwy grafik")
        self.imageNameEntryTab1 = tk.Entry(tab1, width=20)
        self.copyNameButtonTab1 = tk.Button(tab1, text="Kopiuj nazwę", command=lambda: self.copyToClipboard(self.imageNameEntryTab1))
        
        ## SPACING
        # FIRST ROW (0 - Labels)
        self.textLabelTab1.grid(row=0, column=0, padx=(10, 5), pady=(10, 0))
        self.htmlLabelTab1.grid(row=0, column=2, padx=(5, 10), pady=(10, 0))
        
        # SECOND ROW (1 - Windows and button)
        self.textWindowTab1.grid(row=1, column=0, padx=(10, 5), pady=(5, 10))
        self.transferToHTMLButtonTab1.grid(row=1, column=1, padx=(5, 5), pady=10)
        self.HTMLWindowTab1.grid(row=1, column=2, padx=(5, 10), pady=(5, 10))
        
        # THIRD ROW (2 - Copy HTML Button)
        self.copyHTMLButtonTab1.grid(row=2, column=2, padx=(5, 10), pady=10)
        
        # FOURTH ROW (3 - Image Name Section)
        self.imageNameTab1.grid(row=3, column=0, pady=10)
        self.imageNameEntryTab1.grid(row=3, column=1, pady=10)
        self.copyNameButtonTab1.grid(row=3, column=2, pady=10)

    
        # Tab for paraphrases (tab2)
        tab2 = ttk.Frame(notebook)

      
        self.htmlLabelTab2 = tk.Label(tab2, text="HTML")
        self.textLabelTab2 = tk.Label(tab2, text="Tekst")

       
        self.htmlWindowTab2 = tk.Text(tab2, height=20, width=30)
        self.textWindowTab2 = tk.Text(tab2, height=20, width=30)

       
        self.transferToTextButtonTab2 = tk.Button(tab2, text="--->") 
        self.transferToHTMLButtonTab2 = tk.Button(tab2, text="<---") 

        self.copyHTMLButtonTab2 = tk.Button(tab2, text="Kopiuj HTML") 
        self.copyTextButtonTab2 = tk.Button(tab2, text="Kopiuj Tekst")  

        ## SPACING
        # FIRST ROW (0 - Labels)
        self.htmlLabelTab2.grid(row=0, column=0, padx=(10, 5), pady=(10, 0))
        self.textLabelTab2.grid(row=0, column=2, padx=(5, 10), pady=(10, 0))

        # SECOND ROW (1 - Windows and Transfer Button)
        self.htmlWindowTab2.grid(row=1, column=0, rowspan=2, padx=(10, 5), pady=(5, 10))
        self.textWindowTab2.grid(row=1, column=2, rowspan=2, padx=(5, 10), pady=(5, 10))
        self.transferToTextButtonTab2.grid(row=1, column=1, padx=(65, 65), pady=(5, 10))
        
        # THIRD ROW (2 - Transfer Button)
        self.transferToHTMLButtonTab2.grid(row=2, column=1, padx=(65, 65), pady=(5, 10))

        # FOURTH ROW (3 - copyButtons)
        self.copyHTMLButtonTab2.grid(row=3, column=0, padx=(10, 5), pady=(10, 5))
        self.copyTextButtonTab2.grid(row=3, column=2, padx=(5, 10), pady=(10, 5))

 
        # Adding tabs to notebook
        notebook.add(tab1, text="Nowy opis")
        notebook.add(tab2, text="Parafrazy")
        notebook.pack(expand=True, fill='both')

        
    def copyToClipboard(self, widget):
        # For Entry box
        if isinstance(widget, tk.Entry):
            valueToCopy = widget.get()
        # For Text box
        elif isinstance(widget, tk.Text):
            valueToCopy = widget.get("1.0", "end-1c")
        else:
            valueToCopy = ""
        
        self.window.clipboard_clear()
        self.window.clipboard_append(valueToCopy)

        
        
        
        
    def run(self):
        self.window.mainloop()

gui = GUI()
gui.run()
