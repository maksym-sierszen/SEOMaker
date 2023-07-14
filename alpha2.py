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
    #print(f"Document: {self.document}")  # Dodane do debugowania
    #print(f"Paragraphs: {len(self.paragraphs)}")  # Dodane do debugowania
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
        print(f"temp parts: {len(self.templateParts)}")  # Dodane do debugowania

    def lowercaseifyName(self, name):
      name = name.lower()
      symbolsToChange = [".", ",", "`", ":", ";", "/", "'"," "]
      for symbol in symbolsToChange:
        if symbol in name:
          name = name.replace(symbol, "-")
      name = self.Replacer("docx", name, "")
      return name

    def polishReplacer(self, name):
      polish_letters = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
      for letter in polish_letters:
          name = name.replace(letter, polish_letters[letter])
      return name  

    def processContent(self, productName, paragraphs):
      readyToUse = self.Replacer(self.templateParts[1], self.template, productName)

      for i in range(4, len(self.templateParts), 5):
        readyToUse_help = self.Replacer("TEKST_ALTERNATYWNY", self.templateParts[i], productName)
        readyToUse = self.Replacer(self.templateParts[i], readyToUse , readyToUse_help)

      readyToUse_help = self.Replacer("nazwa produktu", self.templateParts[0], productName)
      readyToUse = self.Replacer(self.templateParts[0], readyToUse , readyToUse_help)
      readyToUse = self.Replacer(self.templateParts[3], readyToUse, paragraphs[0])

      readyToUse_help = self.Replacer("NAGLOWEK_1", self.templateParts[5], self.templateParts[6])
      readyToUse = self.Replacer(self.templateParts[5], readyToUse , readyToUse_help)
      readyToUse = self.Replacer(self.templateParts[6], readyToUse, paragraphs[1]) # nagłówek
      readyToUse = self.Replacer(self.templateParts[8], readyToUse, paragraphs[2])

      readyToUse_help = self.Replacer("NAGLOWEK_2", self.templateParts[10], self.templateParts[11])
      readyToUse = self.Replacer(self.templateParts[10], readyToUse , readyToUse_help)
      readyToUse = self.Replacer(self.templateParts[11], readyToUse, paragraphs[3]) # nagłówek
      readyToUse = self.Replacer(self.templateParts[13], readyToUse, paragraphs[4])

      readyToUse_help = self.Replacer("NAGLOWEK_3", self.templateParts[15], self.templateParts[16])
      readyToUse = self.Replacer(self.templateParts[15], readyToUse , readyToUse_help)
      readyToUse = self.Replacer(self.templateParts[16], readyToUse, paragraphs[5]) # nagłówek
      readyToUse = self.Replacer(self.templateParts[18], readyToUse, paragraphs[6])
      
      return readyToUse



class fileManager:
  def __init__(self, gui):
      self.gui = gui
      self.desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
      self.filePath = os.path.join(self.desktop_path, 'wpiszERP.txt')
      
  def saveContent(self, readyToUse):
    with open(self.filePath, "w", encoding="utf-8") as file:
        file.write(readyToUse)

  def openExplorer(self):
      filePath = fd.askopenfilename(initialdir=self.desktop_path, title="Wybierz plik", filetypes=(("docx files", "*.docx"), ("all files", "*.*")))
      if filePath:
          self.gui.fileBox.delete(0, END)
          self.gui.fileBox.insert(0, filePath)
          self.gui.imageNameBox.delete(0, END)
          word = Word()
          word.getData(filePath)

  def generateSEO(self):
    fileName = os.path.basename(self.gui.fileBox.get())
    word = Word()
    word.getData(fileName)  # Uzyskuje dane z pliku
    text = Text()
    text.createFile()  # Tworzy plik
    readyToUse = text.processContent(word.productName, word.paragraphs)  
    self.saveContent(readyToUse)  # Zapisuje przetworzony tekst do pliku
    

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
