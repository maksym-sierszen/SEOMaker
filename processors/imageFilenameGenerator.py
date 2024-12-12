import re

class imageFilenameGenerator:
    def __init__(self, gui):
        self.gui = gui
        self.imageFileName = ""
        self.readyToUse = ""
    
    def generateImageFileName(self, productName, templateLength):
        imageFileNameBase = productName
        polishLetters = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
        for letter in polishLetters:
            imageFileNameBase = imageFileNameBase.replace(letter, polishLetters[letter])

        imageFileNameBase = imageFileNameBase.lower()

        symbolsToChange = [".", ",", "`", ":", ";", "/", "'"," ", "]", "[", "~", "<", ">","+", "=", "|", "(", ")"]
        for symbol in symbolsToChange:
            if symbol in imageFileNameBase:
                imageFileNameBase = imageFileNameBase.replace(symbol, "-")

        for i in range(1, templateLength+1):
            self.imageFileName = f"{imageFileNameBase}-{i}"
            self.imageFileName = re.sub(r'-{2,}', '-', self.imageFileName)
            self.readyToUse = self.readyToUse.replace(f"IMAGENAME", self.imageFileName, 1)

        imageFileNameBase = re.sub(r'-{2,}', '-', imageFileNameBase)
        self.gui.imageNameEntryTab1.delete(0, tk.END)
        self.gui.imageNameEntryTab1.insert(0, imageFileNameBase+"-")
        
        return self.imageFileName