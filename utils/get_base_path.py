import os
import sys

def get_base_path():
  
    #Returns the base path for the application, considering both local and PyInstaller builds.
    
    if getattr(sys, 'frozen', False):  # If running as a PyInstaller bundle
        return sys._MEIPASS  # Folder where PyInstaller extracts resources
    return os.path.dirname(os.path.abspath(__file__))  # Path for local development
