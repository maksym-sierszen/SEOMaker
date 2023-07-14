from tkinter import *
from tkinter import filedialog as fd
import docx2txt
import os

class Word():
  def __init__(self):
    self.document = None
    self.productName = None
    self.paragraphs = []

  def getData(self, wordFile):
    self.document = docx2txt.process(wordFile)
    self.paragraphs = self.document.split('\n\n')
    self.productName = Text.Replacer(".docx", wordFile, "")

    if (self.paragraphs[0] == self.productName): 
      self.paragraphs.pop(0)

# TO DO:
# dodac mozliwosc zmiany nazwy po wklejeniu jej po prostu też

class Text():
    def __init__(self, templateParts):
        self.templateParts = []
        self.template = None

    def Replacer(self, toReplace, fromReplace, withReplace):
        if toReplace in fromReplace:
            fromReplace = fromReplace.replace(toReplace, withReplace)
        return fromReplace
    
    def makeFile(self):
        with open("template.txt", "r", encoding="utf-8") as file:
            self.template = file.read()
        self.templateParts = self.template.split('\n\n')

          
    # product-name-image- format
    def lowercaseifyName(self, name):
      name = name.lower()
      symbolsToChange = [".", ",", "`", ":", ";", "/", "'"," "]
      for symbol in name:
        if symbol in symbolsToChange:
          name = name.replace(symbol, "-")

        # Remove file extension from name
        name = Text.Replacer("docx", name, "")
        # if "docx" in name:
        #   name = name.replace("docx", "")
      return name

    def polishReplacer(self, name):
      polish_letters = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
      for letter in polish_letters:
          name = name.replace(letter, polish_letters[letter])
      return name  


    def processHeaders(self, readyToUse, productName, paragraphs):
        for i in range(0, len(paragraphs)):
            readyToUse_help = self.Replacer("NAGLOWEK_" + str(i+1), self.templateParts[i*5+5], self.templateParts[i*5+6])
            readyToUse = self.Replacer(self.templateParts[i*5+5], readyToUse , readyToUse_help)
            readyToUse = self.Replacer(self.templateParts[i*5+6], readyToUse, paragraphs[i]) 
            readyToUse = self.Replacer(self.templateParts[i*5+8], readyToUse, paragraphs[i+1])
        return readyToUse

    def processContent(self, productName, paragraphs, file_path):
        readyToUse = self.Replacer(self.templateParts[1], self.template, productName)

        for i in range(4, len(self.templateParts), 5):
            readyToUse_help = self.Replacer("TEKST_ALTERNATYWNY", self.templateParts[i], productName)
            readyToUse = self.Replacer(self.templateParts[i], readyToUse , readyToUse_help)

        readyToUse_help = self.Replacer("nazwa produktu", self.templateParts[0], productName)
        readyToUse = self.Replacer(self.templateParts[0], readyToUse , readyToUse_help)
        readyToUse = self.Replacer(self.templateParts[3], readyToUse, paragraphs[0])

        readyToUse = self.process_paragraphs(readyToUse, productName, paragraphs)

    

class fileManager:
  def __init__(self, gui):
      self.gui = gui
      self.desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
      self.filePath = os.path.join(self.desktop_path, 'wpiszERP.txt')
  def saveContent(self):
    with open(self.filePath, "w", encoding="utf-8") as file:
        file.write(Text().readyToUse)  # lub inna metoda uzyskania readyToUse

  def openExplorer(self):
      filePath = fd.askopenfilename(initialdir=self.desktop_path, title="Wybierz plik", filetypes=(("docx files", "*.docx"), ("all files", "*.*")))
      if filePath:
          self.gui.fileBox.delete(0, END)
          self.gui.fileBox.insert(0, filePath)
          self.gui.imageNameBox.delete(0, END)
          fileName = os.path.basename(filePath)
          fileNameReady = Text().lowercaseifyName(fileName)
          fileNameReady = Text().polishReplacer(fileNameReady)
          self.gui.imageNameBox.insert(0, fileNameReady)
          word = Word()
          word.getData(filePath)
          text = Text()
          text.makeFile()


    # def saveContent(self):
    #   with open(fileManager.filePath, "w", encoding="utf-8") as file:
    #       file.write(Text.readyToUse)


    # def openExplorer(self):
    #     filePath = fd.askopenfilename(initialdir=self.desktop_path, title="Wybierz plik", filetypes=(("docx files", "*.docx"), ("all files", "*.*")))
    #     if filePath:
    #         self.gui.fileBox.delete(0, END)
    #         self.gui.fileBox.insert(0, filePath)

    #         self.gui.imageNameBox.delete(0, END)
    #         fileName = os.path.basename(filePath)
    #         fileNameReady = Text.lowercaseifyName(fileName)
    #         fileNameReady = Text.polishReplacer(fileNameReady)
    #         self.gui.imageNameBox.insert(0, fileNameReady)

    #         Word.getFile(filePath)
    #         Text.makeFile()


class GUI:
    def __init__(self):
      self.root = Tk()
      self.root.geometry("600x250")

      self.pathLabel = Label(self.root, text="Ścieżka pliku:")
      self.fileBox = Entry(self.root, width=40)
      self.fileBox.insert(0, "Wybierz opis")

      self.imageName = Label(self.root, text="Nazwy grafik:")
      self.imageNameBox = Entry(self.root, width=40)
      self.imageNameBox.insert(0, " ")

      self.browseButton = Button(self.root, text="Przeglądaj pliki", command=fileManager.openExplorer)
      self.copyNameButton = Button(self.root, text="Kopiuj", command=self.copyImageName)

      self.pathLabel.grid(row=0, column=0, padx=20, pady=20)
      self.fileBox.grid(row=0, column=1, padx=10, pady=20)
      self.browseButton.grid(row=0, column=2, padx=20, pady=20)

      self.imageName.grid(row=1, column=0, padx=20, pady=20)
      self.imageNameBox.grid(row=1, column=1, padx=10, pady=20)
      self.copyNameButton.grid(row=1, column=2, padx=20, pady=20)

    def copyImageName(self):
      imageName = GUI.imageNameBox.get()
      GUI.root.clipboard_clear()  
      GUI.root.clipboard_append(imageName)

    def run(self):
        self.root.mainloop()

# Tworzenie instancji klasy GUI
gui = GUI()
gui.run()