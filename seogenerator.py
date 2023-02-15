# GUI
from tkinter import *
from tkinter import filedialog as fd

root = Tk()
root.geometry("600x250")

pathLabel = Label(root, text="Ścieżka pliku:")

inputBox = Entry(root, width=40)
inputBox.insert(0, "Wybierz opis")

def openExplorer():
  # Open explore window
  filename = fd.askopenfilename()
  inputBox.delete(0, END)
  inputBox.insert(0, filename)
  # Put the file path into input

browseButton = Button(root, text="Przeglądaj pliki", command=openExplorer)


pathLabel.grid(row=0, column=0,padx=20, pady=20)
inputBox.grid(row=0, column=1, padx=10, pady=20)
browseButton.grid(row=0, column=2, padx=20, pady=20)

root.mainloop()


# Break template down into parts


# Extract parts from docx file


# Fill template parts with docx content


# Generate SEO file