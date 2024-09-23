import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import re

class TextProcessor:
    def __init__(self, gui):
        self.gui = gui
        self.productDescription = ""
        self.paragraphs = []
        self.productName = ""
        self.readyToUse = ""
        self.imageFileName = ""
        self.templateLength = 4
        self.selectedType = 1
    
    def getData(self):
        self.productDescription = self.gui.textWindowTab1.get("1.0", "end-1c")
        self.paragraphs = self.productDescription.split('\n')
        self.paragraphs = list(filter(lambda par: par != "", self.paragraphs)) 
        self.productName = self.paragraphs[0]
        self.templateLength = len(self.paragraphs) // 2 


    def generateImageFileName(self, productName):
        imageFileNameBase = self.productName
        polishLetters = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
        for letter in polishLetters:
          imageFileNameBase = imageFileNameBase.replace(letter, polishLetters[letter])

        imageFileNameBase = imageFileNameBase.lower()

        symbolsToChange = [".", ",", "`", ":", ";", "/", "'"," ", "]", "[", "~", "<", ">","+", "=", "|", "(", ")"]
        for symbol in symbolsToChange:
            if symbol in imageFileNameBase:
                imageFileNameBase = imageFileNameBase.replace(symbol, "-")

        for i in range(1, self.templateLength+1):
            self.imageFileName = f"{imageFileNameBase}-{i}"
            self.imageFileName = re.sub(r'-{2,}', '-', self.imageFileName)
            self.readyToUse = self.readyToUse.replace(f"IMAGENAME", self.imageFileName, 1)

        imageFileNameBase = re.sub(r'-{2,}', '-', imageFileNameBase)
        gui.imageNameEntryTab1.delete(0, tk.END)
        gui.imageNameEntryTab1.insert(0, imageFileNameBase+"-") 


    def fillTemplate(self, productName, paragraphs):
        fragments = []
        
        header = paragraphs[0] if len(paragraphs) > 0 else ""
        text = paragraphs[1] if len(paragraphs) > 1 else ""


        separatorElement = f"""<div class="separator short"></div>"""
        
       
        mainTemplateElementCenter = f"""<div class="col-3-3 m-center">
                                        <p>

                                        {text}

                                        </p>
                                        </div>

                                        <div class="col-3-3 center">

                                        <img src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/IMAGENAME.jpg" alt=""/>


                                        </div>

                                        <!--img koniec-->





                                        <div class="separator short"></div>


                                        <!-- header-->
                                        <div class="col-3-3">

                                        <h3 class="size-5">
                                                               {header}
                                        </h3>
                                        </div>
                                        <!-- end header-->"""
        
     
        mainTemplateElementLeft = f"""<div class="col-3-3 cc-mobile">
                                    <div class="col-2-5 cc-mobile-2">
                                    <img src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/IMAGENAME.jpg" class="left" alt=""/>
                                    </div>
                                    <div class="col-3-5 cc-mobile-1">

                                    <p>
                                    
                                    {text}

                                    </p>
                                    </div>
                                    </div>
                                    <div class="separator short"></div>


                                    <!-- header-->
                                    <div class="col-3-3">

                                    <h3 class="size-5">
                                    
                                    {header}

                                    </h3>
                                    </div>
                                    <!-- end header-->"""                

        mainTemplateElementMini = f"""<div class="col-1-6 top">
                                    <img alt="" src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/piktogramy/piktogram.svg"/>
                                    </div>
                                    <div class="col-5-6 m-center">
                                    <h3 class="size-5">
                                        {header}
                                    </h3>
                                    <p> 
                                        {text}
                                    </p>
                                    <div class="col-3-3">
                                    <img alt="" class="left" src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/IMAGENAME.jpg"/>
                                    </div>
                                    </div>"""

        if self.selectedType == 1:
            fragments.append(mainTemplateElementCenter)
        elif self.selectedType == 2:
            fragments.append(mainTemplateElementLeft)
        else: 
            fragments.append(mainTemplateElementMini)

        for i in range(2, len(paragraphs), 2):
            header = paragraphs[i] if i < len(paragraphs) else ""
            text = paragraphs[i+1] if i+1 < len(paragraphs) else ""

            if self.selectedType == 3:
                templateElementMini = f"""<div class="col-1-6 top">
                                        <img alt="" src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/piktogramy/piktogram.svg"/>
                                        </div>
                                        <div class="col-5-6 m-center">
                                        <h3 class="size-5">
                                            {header}
                                        </h3>
                                        <p> 
                                            {text}
                                        </p>
                                        <div class="col-3-3">
                                        <img alt="" class="left" src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/IMAGENAME.jpg"/>
                                        </div>
                                        </div> """
                
                fragments.append(templateElementMini.replace("{header}", header).replace("{text}", text))

            else:    
                
                templateElementLeft = f"""<div class="col-3-3 cc-mobile bg-gray-porcelain rounded-2xl">
                                        <div class="col-2-5 cc-mobile-2">
                                        <img src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/IMAGENAME.jpg" class="left" alt=""/>
                                        </div>
                                        <div class="col-3-5 cc-mobile-1">
                                        <h4>
                                        
                                        {header}
                                        
                                        </h4>
                                        <p>
                                        
                                        {text}
                                        
                                        </p>
                                        </div>
                                        </div>"""
    
                templateElementRight = f"""<div class="col-3-3 cc-mobile bg-gray-porcelain rounded-2xl">
                                        <div class="col-3-5 cc-mobile-1 ">
                                        <h4>
                                        {header}
                                        
                                        </h4>
                                        <p>
                                        
                                        {text}
                                        
                                        </p>
                                        </div>
                                        <div class="col-2-5 cc-mobile-2">
                                        <img src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/IMAGENAME.jpg" class="left" alt=""/>
                                        </div>
                                        
                                        </div>"""
                if (i // 2) % 2 == 0:
                    fragments.append(templateElementLeft.replace("{header}", header).replace("{text}", text))
                else: 
                    fragments.append(templateElementRight.replace("{header}", header).replace("{text}", text))

                if (i + 2) < len(paragraphs):
                    fragments.append(separatorElement)

        self.readyToUse = separatorElement.join(fragments)


     
    def generateSEO(self):
        self.getData()
        self.fillTemplate(self.productName, self.paragraphs)
        self.generateImageFileName(self.productName)
        
        gui.HTMLWindowTab1.delete("1.0", tk.END)  # Remove current text
        gui.HTMLWindowTab1.insert("1.0", self.readyToUse)
        
        gui.HTMLWindowTab2.delete("1.0", tk.END)  # Remove current text
        gui.HTMLWindowTab2.insert("1.0", self.readyToUse)
        
        gui.textWindowTab2.delete("1.0", tk.END)


class Paraphraser:
    def __init__(self, gui):
        self.gui = gui
        self.HTMLContent = ''''''
        
    def extractContent(self):
        HTMLContent = self.gui.HTMLWindowTab2.get("1.0", "end-1c")

        # Create a BeautifulSoup object for HTML modification
     
        soup = BeautifulSoup(HTMLContent, 'html.parser')
      

        self.gui.textWindowTab2.delete("1.0", "end")

        for p in soup.find_all('p'):
            text = p.get_text(strip=True) + "\n\n" 
            self.gui.textWindowTab2.insert("end", text)
    
    def addHTML(self):

        paragraphsContent = self.gui.textWindowTab2.get("1.0", "end-1c").strip().split('\n\n')
        HTMLContent = self.gui.HTMLWindowTab2.get("1.0", "end-1c")

        # Create a BeautifulSoup object for HTML modification
       
        soup = BeautifulSoup(HTMLContent, 'html.parser')
   
        paragraphs = soup.find_all('p')
        
        # Remove <html> and <body> tags if they exist, but keep their content
        if soup.html is not None:
            soup.html.unwrap()
        if soup.body is not None:
            soup.body.unwrap()
        
        # Swap the content of each paragraph with the content from TextWindowTab2
        for p, new_text in zip(paragraphs, paragraphsContent):
            p.string = new_text

        # Clear HTMLWindowTab1 and instert modified HTML
        self.gui.HTMLWindowTab2.delete("1.0", "end")
        self.gui.HTMLWindowTab2.insert("1.0", str(soup))
    
    
class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("SEOMaker v2.1.0")
        self.window.iconbitmap("dist/icon.ico")
        self.window.geometry("800x650")
        self.window.configure(background='white')
        self.window.resizable(False, False)
        self.textProcessor = TextProcessor(self)
        self.paraphraser = Paraphraser(self)
        self.defaultPrompt = self.loadDefaultPrompt()
        

        notebook = ttk.Notebook(self.window)
        
        # Tab for new files (tab1)
        tab1 = ttk.Frame(notebook)
        
        self.textLabelTab1 = tk.Label(tab1, text="Tekst")
        self.htmlLabelTab1 = tk.Label(tab1, text="HTML")
        
        self.textWindowTab1 = tk.Text(tab1, height=20, width=30)
        self.HTMLWindowTab1 = tk.Text(tab1, height=20, width=30)
        self.transferToHTMLButtonTab1 = tk.Button(tab1, text="--->", command=self.textProcessor.generateSEO, bg="#008CBA", width="15")
        
        self.copyHTMLButtonTab1 = tk.Button(tab1, text="Kopiuj HTML", command=lambda: self.copyToClipboard(self.HTMLWindowTab1), bg="#008CBA", width="30")
        
        self.imageNameTab1 = tk.Label(tab1, text="Nazwy grafik")
        self.imageNameEntryTab1 = tk.Entry(tab1, width=20)
        self.copyNameButtonTab1 = tk.Button(tab1, text="Kopiuj nazwę", command=lambda: self.copyToClipboard(self.imageNameEntryTab1), bg="#008CBA")
        
        self.var = tk.IntVar()
        self.centerRadioTab1 = tk.Radiobutton(tab1, text="CENTER", variable=self.var, value=1, command=self.radioSelectionSend)
        self.leftRadioTab1 = tk.Radiobutton(tab1, text="LEWO", variable=self.var, value=2, command=self.radioSelectionSend)
        self.miniRadioTab1 = tk.Radiobutton(tab1, text="MINI", variable=self.var, value=3, command=self.radioSelectionSend)
        




        ## SPACING

        paddingx1=50
        # FIRST ROW (0 - Radio Buttons)
        self.centerRadioTab1.grid(row=0, column=0, padx=(paddingx1, paddingx1/2), pady=(20, 0))
        self.leftRadioTab1.grid(row=0, column=1, padx=(paddingx1/2, paddingx1/2), pady=(20, 0))
        self.miniRadioTab1.grid(row=0, column=2, padx=(paddingx1/2, paddingx1), pady=(20, 0))

        # SECOND ROW (1 - Labels)
        self.textLabelTab1.grid(row=1, column=0, padx=(paddingx1, paddingx1/2), pady=(20, 0)) 
        self.htmlLabelTab1.grid(row=1, column=2, padx=(paddingx1/2, paddingx1), pady=(20, 0)) 

        # THIRD ROW (2 - Windows and button)
        self.textWindowTab1.grid(row=2, column=0, padx=(paddingx1, paddingx1/2), pady=(5, 10))
        self.transferToHTMLButtonTab1.grid(row=2, column=1, padx=(paddingx1/2, paddingx1/2), pady=10)
        self.HTMLWindowTab1.grid(row=2, column=2, padx=(paddingx1/2, paddingx1), pady=(5, 10))

        # FOURTH ROW (3 - Copy HTML Button)
        self.copyHTMLButtonTab1.grid(row=3, column=2, padx=(paddingx1/2, paddingx1), pady=10)
                        
        # FIFTH ROW (4 - Image Name Section)
        self.imageNameTab1.grid(row=4, column=0, pady=30)
        self.imageNameEntryTab1.grid(row=4, column=1, pady=30)
        self.copyNameButtonTab1.grid(row=4, column=2, pady=30)


        # Tab for paraphrases (tab2)
        tab2 = ttk.Frame(notebook)

      
        self.htmlLabelTab2 = tk.Label(tab2, text="HTML")
        self.textLabelTab2 = tk.Label(tab2, text="Tekst")

        self.HTMLWindowTab2 = tk.Text(tab2, height=20, width=30)
        self.textWindowTab2 = tk.Text(tab2, height=20, width=30)

        self.transferToTextButtonTab2 = tk.Button(tab2, text="--->", command=self.paraphraser.extractContent, bg="#008CBA", width="15") 
        self.transferToHTMLButtonTab2 = tk.Button(tab2, text="<---", command=self.paraphraser.addHTML, bg="#008CBA", width="15") 

        self.copyHTMLButtonTab2 = tk.Button(tab2, text="Kopiuj HTML", command=lambda: self.copyToClipboard(self.HTMLWindowTab2), bg="#008CBA", width="30") 
        self.copyTextButtonTab2 = tk.Button(tab2, text="Kopiuj Tekst", command=lambda: self.copyToClipboard(self.textWindowTab2, addPrompt=True), bg="#008CBA", width="30")  

        self.promptLabelTab2 = tk.Label(tab2, text="Prompt")
        self.promptTextWindowTab2 = tk.Text(tab2, height=10, width= 30)
        self.promptState = tk.BooleanVar(value=False)
        self.promptCheckbuttonTab2 = tk.Checkbutton(tab2, text="Dodawaj Prompt ", variable=self.promptState)
        self.promptTextWindowTab2.insert("1.0", self.defaultPrompt)

        
        ## SPACING
        paddingx2=15
        # FIRST ROW (0 - Labels)
        self.htmlLabelTab2.grid(row=0, column=0, padx=(paddingx2, paddingx2/2), pady=(10, 0))
        self.textLabelTab2.grid(row=0, column=2, padx=(paddingx2/2, paddingx2), pady=(10, 0))

        # SECOND ROW (1 - Windows and Transfer Button)
        self.HTMLWindowTab2.grid(row=1, column=0, rowspan=2, padx=(paddingx2, paddingx2/2), pady=(5, 10))
        self.textWindowTab2.grid(row=1, column=2, rowspan=2, padx=(paddingx2/2, paddingx2/2), pady=(5, 10))
        self.transferToTextButtonTab2.grid(row=1, column=1, padx=(paddingx2/2,paddingx2), pady=(5, 10))
        
        # THIRD ROW (2 - Transfer Button)
        self.transferToHTMLButtonTab2.grid(row=2, column=1, padx=(paddingx2/2, paddingx2/2), pady=(5, 10))

        # FOURTH ROW (3 - copyButtons)
        self.copyHTMLButtonTab2.grid(row=3, column=0, padx=(paddingx2, paddingx2/2), pady=(10, 5))
        self.copyTextButtonTab2.grid(row=3, column=2, padx=(paddingx2/2,paddingx2), pady=(10, 5))

        # FIFTH ROW (4 - Prompt Section)
        self.promptLabelTab2.grid(row=4, column=0, padx=(paddingx2, paddingx2/2), pady=(10, 0))
        self.promptTextWindowTab2.grid(row=4, column=1, padx=(paddingx2/2, paddingx2/2), pady=(10, 0))
        #self.copyPromptButtonTab2.grid(row=4, column=2, padx=(10, 5), pady=(10, 0))
        self.promptCheckbuttonTab2.grid(row=4, column=2, padx=(paddingx2/2,paddingx2), pady=(10, 0))
        
        
        
        
        style=ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background='lightblue')
        style.map('TNotebook.Tab', background=[('selected', '#008CBA')])
        # Adding tabs to notebook
        notebook.add(tab1, text="Nowy opis")
        notebook.add(tab2, text="Parafrazy")
        
        notebook.pack(expand=True, fill='both')
         
    def loadDefaultPrompt(self):
        with open('prompt.txt', 'r', encoding='utf-8') as file:
           prompt = file.read()
           return prompt
    
    def copyToClipboard(self, widget, addPrompt=False):
        
        # Adding prompt for content from TextWindowTab2
         # Only when addPrompt is True check the state of promptState
        if addPrompt and self.promptState.get():
            promptContent = self.promptTextWindowTab2.get("1.0", "end-1c")+ "\n\n"
        else:
            promptContent = ""
        
        # For Entry box
        if isinstance(widget, tk.Entry):
            valueToCopy = widget.get()
        # For Text box
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


if __name__ == "__main__":
    gui = GUI()
    gui.run()