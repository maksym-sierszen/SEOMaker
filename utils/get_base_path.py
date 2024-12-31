import os
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):  # If the application is running as a frozen executable
        return sys._MEIPASS  # PyInstaller extracts files to a temp directory
    return os.path.dirname(os.path.abspath(__file__))  # Path of the current file

def get_project_root():
    return os.path.dirname(get_base_path())  # Moves one level up to the project root
