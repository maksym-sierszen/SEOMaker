from gui import GUI
from clients.claude_client import ClaudeClient
from processors.text_processor import TextProcessor
from processors.paraphraser import Paraphraser



if __name__ == "__main__":
    # Create GUI first without linking components
    gui = GUI(text_processor=None, paraphraser=None, claude_client=None)

    # Initialize components
    text_processor = TextProcessor(gui)
    paraphraser = Paraphraser(gui)
    claude_client = ClaudeClient(gui)

    # Link components to GUI
    gui.textProcessor = text_processor
    gui.paraphraser = paraphraser
    gui.ClaudeClient = claude_client

    # Start the GUI application
    gui.run()
