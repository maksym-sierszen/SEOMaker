def insertText(self, outputWindow, text):
        outputWindow.delete("1.0", "end")
        outputWindow.insert("end", text)