from tkinter import *
from tkinter import filedialog as fd
from pathlib import Path
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
    self.productName = os.path.basename(wordFile)
    self.productName = self.productName.replace(".docx", "")

    if (self.paragraphs[0] == self.productName): 
      self.paragraphs.pop(0)


class Text():
    def __init__(self):
        self.templateParts = []
        self.template = ""
        

    def createFile(self):
        with open("template.txt", "r", encoding="utf-8") as file:
            self.template = file.read()
        self.templateParts = self.template.split('\n\n')


    def generateImageFileName(self, productName):
      polish_letters = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
      for letter in polish_letters:
          productName = productName.replace(letter, polish_letters[letter])

      productName = productName.lower()

      symbolsToChange = [".", ",", "`", ":", ";", "/", "'"," ", "]", "[", "~", "<", ">","+", "="]
      for symbol in symbolsToChange:
        if symbol in productName:
          productName = productName.replace(symbol, "-")

      while '--' in productName:
        productName = productName.replace('--', '-')

      productName = productName.replace("docx", "")

      return productName


    def processContent(self, productName, paragraphs):

      readyToUse = self.template

      readyToUse = readyToUse.replace("ALTTEXT", productName)
      readyToUse = readyToUse.replace("PRODUCTNAME", productName)

      readyToUse = readyToUse.replace("TEXT1", paragraphs[0])
      readyToUse = readyToUse.replace("HEADER2", paragraphs[1])
      readyToUse = readyToUse.replace("TEXT2", paragraphs[2])
      readyToUse = readyToUse.replace("HEADER3", paragraphs[3])
      readyToUse = readyToUse.replace("TEXT3", paragraphs[4])
      readyToUse = readyToUse.replace("HEADER4", paragraphs[5])
      readyToUse = readyToUse.replace("TEXT4", paragraphs[6])

      imageFileNameBase = self.generateImageFileName(productName)
      for i in range(1, 5):
        imageFileName = f"{imageFileNameBase}-{i}"
        readyToUse = readyToUse.replace(f"IMAGENAME{i}", imageFileName)

        gui.imageNameBox.delete(0, END)
        gui.imageNameBox.insert(0, imageFileNameBase + "-")

      return readyToUse


    def splitFirstSentence(self, paragraph):
        sentences = paragraph.split('. ', 1)
        return sentences[0], sentences[1] if len(sentences) > 1 else ''



class fileManager:
  def __init__(self, gui):
      self.gui = gui
      self.desktopPath = Path.home() / 'OneDrive - Grupa Komputronik' / 'Pulpit'
      self.filePath = self.desktopPath / 'wpiszERP.txt'

  def saveContent(self, readyToUse):
    try:
        with open(self.filePath, "w", encoding="utf-8") as file:
            file.write(readyToUse)
    except Exception as e:
        print(f"Error while saving the file: {e}")

  def openExplorer(self):
      try:
          filePath = fd.askopenfilename(initialdir=self.desktopPath, title="Wybierz plik", filetypes=(("docx files", "*.docx"), ("all files", "*.*")))
          if filePath:
              self.gui.fileBox.delete(0, END)
              self.gui.fileBox.insert(0, filePath)
              self.gui.imageNameBox.delete(0, END)
              word = Word()
              word.getData(filePath)
      except Exception as e:
          print(f"Error while opening the file explorer: {e}")

  def generateSEO(self):
          fileName = os.path.abspath(self.gui.fileBox.get())
          word = Word()
          word.getData(fileName) 
          text = Text()
          text.createFile() 
          readyToUse = text.processContent(word.productName, word.paragraphs)  
          dirPath = os.path.dirname(fileName) 
          self.filePath = os.path.join(dirPath, f'wpiszERP - {word.productName}.txt')
          self.saveContent(readyToUse) 

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("SEOMaker v1.0")
        self.root.iconbitmap("icon.ico")
        self.root.geometry("700x250")
        self.root.configure(bg='white')  
        self.root.resizable(False,False)
        self.manager = fileManager(self)

        self.pathLabel = Label(self.root, text="Ścieżka pliku:", bg='white', font=('Helvetica', 12))  
        self.fileBox = Entry(self.root, width=40, font=('Helvetica', 12))  
        self.fileBox.insert(0, "Wybierz opis")

        self.imageName = Label(self.root, text="Nazwy grafik:", bg='white', font=('Helvetica', 12)) 
        self.imageNameBox = Entry(self.root, width=40, font=('Helvetica', 12))  
        self.imageNameBox.insert(0, " ")

        self.browseButton = Button(self.root, text="Przeglądaj pliki", command=self.manager.openExplorer, bg='#008CBA', fg='white', font=('Helvetica', 12))  
        self.createButton = Button(self.root, text = "Generuj", command=self.manager.generateSEO, bg='#008CBA', fg='white', font=('Helvetica', 12))  
        self.copyNameButton = Button(self.root, text="Kopiuj", command=self.copyImageName, bg='#008CBA', fg='white', font=('Helvetica', 12))  

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

gui = GUI()
gui.run()