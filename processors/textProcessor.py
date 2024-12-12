from dataExtractor import dataExtractor
from HTMLTemplateBuilder import HTMLTemplateBuilder
from imageFilenameGenerator import imageFilenameGenerator

class TextProcessor:
    def __init__(self, gui):
        self.gui = gui
        self.dataExtractor = dataExtractor(gui)
        self.htmlTemplateBuilder = HTMLTemplateBuilder()
        self.imageFilenameGenerator = imageFilenameGenerator(gui)
        self.selectedType = 1
    
    def generateSEO(self):
        extractedData = self.dataExtractor.extractData()
        
        self.htmlTemplateBuilder.selectedType = self.selectedType
        readyToUse = self.htmlTemplateBuilder.fillTemplate(
            extractedData['productName'], 
            extractedData['paragraphs']
        )
        
        imageFileName = self.imageFilenameGenerator.generateImageFileName(
            extractedData['productName'], 
            extractedData['templateLength']
        )
        
        self.gui.HTMLWindowTab1.delete("1.0", tk.END)  
        self.gui.HTMLWindowTab1.insert("1.0", readyToUse)
        
        self.gui.HTMLWindowTab2.delete("1.0", tk.END)  
        self.gui.HTMLWindowTab2.insert("1.0", readyToUse)
        
        self.gui.textWindowTab2.delete("1.0", tk.END)

        self.gui.HTMLWindowTab3.delete("1.0", tk.END)  
        self.gui.HTMLWindowTab3.insert("1.0", readyToUse)