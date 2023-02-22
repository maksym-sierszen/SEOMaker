# GUI
from tkinter import *
from tkinter import filedialog as fd
import os

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


def openExplorer():
  # Open explore window
  filePath = fd.askopenfilename()
  fileBox.delete(0, END)
  fileBox.insert(0, filePath)

  #only do when function success
  # Put the file path into input
  imageNameBox.delete(0, END)
  fileName = os.path.basename(filePath)
  fileName = lowercaseifyName(fileName)
  imageNameBox.insert(0, fileName)

def lowercaseifyName(name):
  name = name.lower()
  symbolsToChange = [".", ",", "`", ":", ";", "/", "'"," "]
  for symbol in name:
    if symbol in symbolsToChange:
      name = name.replace(symbol, "-")

    if "docx" in name:
      name = name.replace("docx", "")
  return name

test = "De'longi.3"
print(lowercaseifyName(test))
# Copy the newly generated image file name to the clipboard
def copyImageName():
  imageName = imageNameBox.get()
  root.clipboard_clear()  
  root.clipboard_append(imageName)  



browseButton = Button(root, text="Przeglądaj pliki", command=openExplorer)
copyNameButton = Button(root, text="Kopiuj", command=copyImageName)

pathLabel.grid(row=0, column=0,padx=20, pady=20)
fileBox.grid(row=0, column=1, padx=10, pady=20)
browseButton.grid(row=0, column=2, padx=20, pady=20)

imageName.grid(row=1, column=0,padx=20, pady=20)
imageNameBox.grid(row=1, column=1, padx=10, pady=20)
copyNameButton.grid(row=1, column=2, padx=20, pady=20)


root.mainloop()


# Break template down into parts


# Extract parts from docx file


# Fill template parts with docx content


# Generate SEO file