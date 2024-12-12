import re
import tkinter as tk

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
        self.gui.imageNameEntryTab1.delete(0, tk.END)
        self.gui.imageNameEntryTab1.insert(0, imageFileNameBase+"-") 


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

        mainTemplateElementMini = f"""<div class="col-3-3 cc-mobile">
                                    <div class="col-2-5 cc-mobile-2">
                                    <img src="https://media.komputronik.pl/pl-komputronik/img/opisy_produktow/content/SEO/IMAGENAME.jpg" class="left" alt=""/>
                                    </div>
                                    <div class="col-3-5 cc-mobile-1">
                                    <h3 class="size-5">
                                    
                                    {header}
                                    </h3>
                                     <p>
                                    
                                    {text}

                                    </p>
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
                templateElementMini = f"""<div class="col-5-6 m-center">
                                        <h3 class="size-5">
                                            {header}
                                        </h3>
                                        <p> 
                                            {text}
                                        </p>
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
                    fragments.append(templateElementRight.replace("{header}", header).replace("{text}", text))
                else: 
                    fragments.append(templateElementLeft.replace("{header}", header).replace("{text}", text))

                if (i + 2) < len(paragraphs):
                    fragments.append(separatorElement)

        if self.selectedType != 3:
            self.readyToUse = separatorElement.join(fragments)
        else: 
            filler = ""
            self.readyToUse = filler.join(fragments)

     
    def generateSEO(self):
        self.getData()
        self.fillTemplate(self.productName, self.paragraphs)
        self.generateImageFileName(self.productName)
        
        self.gui.HTMLWindowTab1.delete("1.0", tk.END)  
        self.gui.HTMLWindowTab1.insert("1.0", self.readyToUse)
        
        self.gui.HTMLWindowTab2.delete("1.0", tk.END)  
        self.gui.HTMLWindowTab2.insert("1.0", self.readyToUse)
        
        self.gui.textWindowTab2.delete("1.0", tk.END)

        self.gui.HTMLWindowTab3.delete("1.0", tk.END)  
        self.gui.HTMLWindowTab3.insert("1.0", self.readyToUse)