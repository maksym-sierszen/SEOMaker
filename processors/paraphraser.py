from bs4 import BeautifulSoup

class Paraphraser:
    def __init__(self, gui):
        self.gui = gui
        self.HTMLContent = ""

    def extractContent(self, input_window):
        HTMLContent = input_window.get("1.0", "end-1c")
        soup = BeautifulSoup(HTMLContent, 'html.parser')
        extracted_text = "\n\n".join(p.get_text(strip=True) for p in soup.find_all('p'))
        return extracted_text

    def addHTML(self, input_window, output_window):
        paragraphsContent = input_window.get("1.0", "end-1c").strip().split('\n\n')
        HTMLContent = output_window.get("1.0", "end-1c")

        soup = BeautifulSoup(HTMLContent, 'html.parser')
        paragraphs = soup.find_all('p')

        for p, new_text in zip(paragraphs, paragraphsContent):
            p.string = new_text

        output_window.delete("1.0", "end")
        output_window.insert("1.0", str(soup))
