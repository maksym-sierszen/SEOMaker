class HTMLTemplateBuilder:
    def __init__(self, selectedType=1):
        self.selectedType = selectedType
        self.readyToUse = ""
    
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

                                        <div class="separator short"></div>

                                        <div class="col-3-3">
                                        <h3 class="size-5">
                                        {header}
                                        </h3>
                                        </div>"""
        
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

                                    <div class="col-3-3">
                                    <h3 class="size-5">
                                    {header}
                                    </h3>
                                    </div>"""                

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
        
        return self.readyToUse
    
    def addHTML(self, inputWindow, outputWindow):
        paragraphsContent = inputWindow.get("1.0", "end-1c").strip().split('\n\n')
        htmlContent = outputWindow.get("1.0", "end-1c")
        
        soup = BeautifulSoup(htmlContent, 'html.parser')
        
        if soup.html is not None:
            soup.html.unwrap()
        if soup.body is not None:
            soup.body.unwrap()
        
        paragraphs = soup.find_all('p')
        
        for p, newText in zip(paragraphs, paragraphsContent):
            p.string = newText

        outputWindow.delete("1.0", "end")
        outputWindow.insert("1.0", str(soup))

    def addHTMLClaude(self):
        paragraphsContent = self.gui.textWindowTab3.get("1.0", "end-1c").strip().split('\n\n')
        htmlContent = self.gui.HTMLWindowTab3.get("1.0", "end-1c")
        
        soup = BeautifulSoup(htmlContent, 'html.parser')
        paragraphs = soup.find_all('p')
        
        if soup.html is not None:
            soup.html.unwrap()
        if soup.body is not None:
            soup.body.unwrap()
        
        for p, newText in zip(paragraphs, paragraphsContent):
            p.string = newText

        self.gui.HTMLWindowTab3.delete("1.0", "end")
        self.gui.HTMLWindowTab3.insert("1.0", str(soup))