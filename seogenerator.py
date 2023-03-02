from tkinter import *
from tkinter import filedialog as fd
import docx2txt
import os

def textRemover(toRemove, fromRemove):
  if toRemove in fromRemove:
      fromRemove = fromRemove.replace(toRemove, "")
  return fromRemove



# Open the file
def openWord(wordFile):
  document = docx2txt.process(wordFile)

  paragraphs = []
  paragraphs = document.split('\n\n')
  # Warunek że jeśli paragraph[0] == filename to skip

  wordFile = textRemover(".docx", wordFile)
  if (paragraphs[0] == wordFile):
    paragraphs.pop(0)


  print(paragraphs[0])
  print("\n\n")
  print(paragraphs[1])
  print("\n\n")
  print(paragraphs[2])



# Choose file and create filename for graphics
def openExplorer():
  # Open explore window
  filePath = fd.askopenfilename()
  fileBox.delete(0, END)
  fileBox.insert(0, filePath)

  # Put the file path into input
  imageNameBox.delete(0, END)
  fileName = os.path.basename(filePath)
  fileNameReady = lowercaseifyName(fileName)
  imageNameBox.insert(0, fileNameReady)

  openWord(fileName)


# Convert filename into a product-name-image- format
def lowercaseifyName(name):
  name = name.lower()
  symbolsToChange = [".", ",", "`", ":", ";", "/", "'"," "]
  for symbol in name:
    if symbol in symbolsToChange:
      name = name.replace(symbol, "-")

    # Remove file extension from name
    name = textRemover("docx", name)
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