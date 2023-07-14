from tkinter import *
from tkinter import filedialog as fd
import docx2txt
import os

class Word():
  def __init__(self):
    self.document = ""
    self.productName = ""
    self.paragraphs = []

  def getData(self, wordFile):
    self.document = docx2txt.process(wordFile)
    self.paragraphs = self.document.split('\n\n')
    text = Text()
    self.productName = text.Replacer(".docx", wordFile, "")

    if (self.paragraphs[0] == self.productName): 
      self.paragraphs.pop(0)


class Text():
    def __init__(self):
        self.templateParts = []
        self.template = ""
        

    def Replacer(self, toReplace, fromReplace, withReplace):
        if toReplace in fromReplace:
            fromReplace = fromReplace.replace(toReplace, withReplace)
        return fromReplace

    def createFile(self):
        with open("template.txt", "r", encoding="utf-8") as file:
            self.template = file.read()
        self.templateParts = self.template.split('\n\n')


    def generateImageFileName(self, productName):
      polish_letters = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
      for letter in polish_letters:
          productName = productName.replace(letter, polish_letters[letter])

      productName = productName.lower()

      symbolsToChange = [".", ",", "`", ":", ";", "/", "'"," "]
      for symbol in symbolsToChange:
        if symbol in productName:
          productName = productName.replace(symbol, "-")
      productName = self.Replacer("docx", productName, "")

      return productName

    def processContent(self, productName, paragraphs):

      readyToUse = self.template
    
      readyToUse = self.Replacer("ALTTEXT", readyToUse, productName)
      readyToUse = self.Replacer("PRODUCTNAME", readyToUse, productName)

      readyToUse = self.Replacer("TEXT1", readyToUse, paragraphs[0])
      readyToUse = self.Replacer("HEADER2", readyToUse, paragraphs[1])
      readyToUse = self.Replacer("TEXT2", readyToUse, paragraphs[2])
      readyToUse = self.Replacer("HEADER3", readyToUse, paragraphs[3])
      readyToUse = self.Replacer("TEXT3", readyToUse, paragraphs[4])
      readyToUse = self.Replacer("HEADER4", readyToUse, paragraphs[5])
      readyToUse = self.Replacer("TEXT4", readyToUse, paragraphs[6])

      imageFileNameBase = self.generateImageFileName(productName)
      for i in range(1, 5):
        imageFileName = f"{imageFileNameBase}-{i}"
        readyToUse = self.Replacer(f"IMAGENAME{i}", readyToUse, imageFileName)

        gui.imageNameBox.delete(0, END)
        gui.imageNameBox.insert(0, imageFileNameBase + "-")
      
    
      return readyToUse

    def splitFirstSentence(self, paragraph):
        sentences = paragraph.split('. ', 1)
        return sentences[0], sentences[1] if len(sentences) > 1 else ''



class fileManager:
  def __init__(self, gui):
      self.gui = gui
      self.desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
      self.filePath = os.path.join(self.desktop_path, 'wpiszERP.txt')
      
  def saveContent(self, readyToUse):
    try:
        with open(self.filePath, "w", encoding="utf-8") as file:
            file.write(readyToUse)
    except Exception as e:
        print(f"Error while saving the file: {e}")

  def openExplorer(self):
      try:
          filePath = fd.askopenfilename(initialdir=self.desktop_path, title="Wybierz plik", filetypes=(("docx files", "*.docx"), ("all files", "*.*")))
          if filePath:
              self.gui.fileBox.delete(0, END)
              self.gui.fileBox.insert(0, filePath)
              self.gui.imageNameBox.delete(0, END)
              word = Word()
              word.getData(filePath)
      except Exception as e:
          print(f"Error while opening the file explorer: {e}")

  def generateSEO(self):
      #try:
          fileName = os.path.basename(self.gui.fileBox.get())
          word = Word()
          word.getData(fileName)  # Uzyskuje dane z pliku
          text = Text()
          text.createFile()  # Tworzy plik
          readyToUse = text.processContent(word.productName, word.paragraphs)  
          self.saveContent(readyToUse)  # Zapisuje przetworzony tekst do pliku
      # except Exception as e:
      #     print(f"Error while generating SEO: {e}")
        
    

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x250")
        self.manager = fileManager(self)

        self.pathLabel = Label(self.root, text="Ścieżka pliku:")
        self.fileBox = Entry(self.root, width=40)
        self.fileBox.insert(0, "Wybierz opis")

        self.imageName = Label(self.root, text="Nazwy grafik:")
        self.imageNameBox = Entry(self.root, width=40)
        self.imageNameBox.insert(0, " ")

        self.browseButton = Button(self.root, text="Przeglądaj pliki", command=self.manager.openExplorer)
        self.createButton = Button(self.root, text = "Generuj", command=self.manager.generateSEO)
        self.copyNameButton = Button(self.root, text="Kopiuj", command=self.copyImageName)


        self.pathLabel.grid(row=0, column=0, padx=20, pady=20)
        self.fileBox.grid(row=0, column=1, padx=10, pady=20)
        self.browseButton.grid(row=0, column=2, padx=20, pady=20)

        self.imageName.grid(row=1, column=0, padx=20, pady=20)
        self.imageNameBox.grid(row=1, column=1, padx=10, pady=20)
        self.copyNameButton.grid(row=1, column=2, padx=20, pady=20)

        self.createButton.grid(row=2, column=2, padx=20, pady=20)


    def copyImageName(self):
      imageName = self.imageNameBox.get()
      self.root.clipboard_clear()  
      self.root.clipboard_append(imageName)

    def run(self):
        self.root.mainloop()

# Tworzenie instancji klasy GUI
gui = GUI()
gui.run()
