class dataExtractor:
    def __init__(self, gui):
        self.gui = gui
        self.productDescription = ""
        self.paragraphs = []
        self.productName = ""
        self.templateLength = 4
    
    def extractData(self):
        self.productDescription = self.gui.textWindowTab1.get("1.0", "end-1c")
        self.paragraphs = self.productDescription.split('\n')
        self.paragraphs = list(filter(lambda par: par != "", self.paragraphs)) 
        self.productName = self.paragraphs[0]
        self.templateLength = len(self.paragraphs) // 2
        
        return {
            'productName': self.productName,
            'paragraphs': self.paragraphs,
            'templateLength': self.templateLength
        }
    
    # wydzielone z paraphraser
    def extractContent(self, inputWindow):
        htmlContent = inputWindow.get("1.0", "end-1c")
        soup = BeautifulSoup(htmlContent, 'html.parser')
        extractedText = "\n\n".join(p.get_text(strip=True) for p in soup.find_all('p'))
        return extractedText