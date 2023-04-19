from tkinter import *
from tkinter import filedialog as fd
import docx2txt
import os


# TO DO:
# polskie znaki replacer
# dodac dziwne znaczki do nazwy
# dodac mozliwosc zmiany nazwy po wklejeniu jej po prostu też



def textReplacer(toReplace, fromReplace, withReplace):
  if toReplace in fromReplace:
      fromReplace = fromReplace.replace(toReplace, withReplace)
  return fromReplace

# Choose file and create filename for graphics
def openExplorer():
  # Open explore window
  filePath = fd.askopenfilename()
  fileBox.delete(0, END)
  fileBox.insert(0, filePath)

  # Put the file path into input
  imageNameBox.delete(0, END)
  global fileName 
  fileName = os.path.basename(filePath)
  fileNameReady = lowercaseifyName(fileName)
  imageNameBox.insert(0, fileNameReady)

  getFromWord(fileName)
  makeText()

# Work on docx file
def getFromWord(wordFile):
  document = docx2txt.process(wordFile)

  global paragraphs
  paragraphs = []
  paragraphs = document.split('\n\n')

  # If first paragraph is the same as products name then skip it (product name is taken from the file name)
  wordFile = textReplacer(".docx", wordFile, "")
  if (paragraphs[0] == wordFile):
    paragraphs.pop(0)

  # print(paragraphs[0])
  # print("\n---przerwa ---\n")
  # print(paragraphs[1])
  # print("\n---przerwa ---\n")
  # print(paragraphs[2])
  # print("\n---przerwa ---\n")
  # print(paragraphs[3])
  # print("\n---przerwa ---\n")
  # print(paragraphs[4])
  #################
  # taki pomysl że parzyste to tresc a nieparzyste to naglowki

# Working with the txt
def makeText():
  # Open the template
  with open("template.txt", "r", encoding="utf-8") as file:
      # odczytanie całej zawartości pliku
      template = file.read()
      

  templateParts = []
  templateParts = template.split('\n\n')

  # print(templateParts[0])
  # print("\n---przerwa ---\n")
  # print(templateParts[1])
  # print("\n---przerwa ---\n")
  # print(templateParts[2])
  # print("\n---przerwa ---\n")
  # print(templateParts[3])
  # print("\n---przerwa ---\n")
  # print(templateParts[4])
  #################

  # Fill the template
  
  readyToUse = textReplacer(templateParts[1], template, fileName)
  readyToUse_help = textReplacer("nazwa produktu", templateParts[0], fileName)
  readyToUse = textReplacer(templateParts[0], readyToUse , readyToUse_help)
  readyToUse = textReplacer(templateParts[3], readyToUse, paragraphs[0])

  readyToUse = textReplacer(templateParts[6], readyToUse, paragraphs[1])
  readyToUse = textReplacer(templateParts[8], readyToUse, paragraphs[2])

  readyToUse = textReplacer(templateParts[11], readyToUse, paragraphs[3])
  readyToUse = textReplacer(templateParts[13], readyToUse, paragraphs[4])

  readyToUse = textReplacer(templateParts[16], readyToUse, paragraphs[5])
  readyToUse = textReplacer(templateParts[18], readyToUse, paragraphs[6])
  # Save to new file
  with open("wpisz_kod_ERP.txt", "w", encoding="utf-8") as file:
      file.write(readyToUse)



# Convert filename into a product-name-image- format
def lowercaseifyName(name):
  name = name.lower()
  symbolsToChange = [".", ",", "`", ":", ";", "/", "'"," "]
  for symbol in name:
    if symbol in symbolsToChange:
      name = name.replace(symbol, "-")

    # Remove file extension from name
    name = textReplacer("docx", name, "")
    # if "docx" in name:
    #   name = name.replace("docx", "")
  return name

# Copy the newly generated image file name to the clipboard
def copyImageName():
  imageName = imageNameBox.get()
  root.clipboard_clear()  
  root.clipboard_append(imageName)  



## WORD




# Break template down into parts


# Extract parts from docx file


# Fill template parts with docx content


# Generate SEO file






### GUI 
root = Tk()
root.geometry("600x250")

# Wybierz plik, który chcesz wrzucić w szablon SEO
pathLabel = Label(root, text="Ścieżka pliku:")
fileBox = Entry(root, width=40)
fileBox.insert(0, "Wybierz opis")

# Przygotowana specjalnie nazwa pliku, którą można skopiować do grafik
imageName = Label(root, text="Nazwy grafik:")
imageNameBox = Entry(root, width=40)
imageNameBox.insert(0, " ")


browseButton = Button(root, text="Przeglądaj pliki", command=openExplorer)
copyNameButton = Button(root, text="Kopiuj", command=copyImageName)

pathLabel.grid(row=0, column=0,padx=20, pady=20)
fileBox.grid(row=0, column=1, padx=10, pady=20)
browseButton.grid(row=0, column=2, padx=20, pady=20)

imageName.grid(row=1, column=0,padx=20, pady=20)
imageNameBox.grid(row=1, column=1, padx=10, pady=20)
copyNameButton.grid(row=1, column=2, padx=20, pady=20)

root.mainloop()