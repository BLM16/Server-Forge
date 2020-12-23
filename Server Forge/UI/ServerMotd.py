import tkinter
from tkinter import ttk
import os, sys

# Get the current directory of this file for use in finding the icon file
# Try handles the executable version
# Except handles running this file as a .py
try:
    CURRENT_DIR = f"{sys._MEIPASS}/UI"
except AttributeError:
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class Interface:
    def __init__(self, serverName):
        """Sets up the interface"""

        # Variable to store data collected from this interface
        self.MOTD = ""
        
        # Set up the window
        self.window = tkinter.Tk()
        self.window.title(f"Server Forge - {serverName}")
        self.window.iconbitmap(os.path.join(CURRENT_DIR, os.pardir, "assets", "Favicon.ico"))
        self.window.minsize(500, 200)
        self.window.maxsize(500, 200)

        # Set up tkinter frames
        self.mainFrame = ttk.Frame(self.window, width = 100, height = 90)
        self.optionsFrame = ttk.Frame(self.window, width = 100, height = 10)

    def next(self):
        """Gets the text entered in the textbox and returns the value to Main"""

        # Get MOTD from text box
        serverMotd = self.txtMotd.get()

        # Ensure all required data was collected
        # Exit window loop to proceed
        if serverMotd:
            self.MOTD = serverMotd
            self.window.quit()

        del serverMotd

    def Render(self):
        """Renders the interface"""

        self.mainFrame.pack()

        ttk.Label(self.mainFrame, text = "MOTD:").grid(row = 0, column = 0)

        self.txtMotd = ttk.Entry(self.mainFrame, width = 50)
        self.txtMotd.grid(row = 0, column = 1)

        self.optionsFrame.pack(side = tkinter.BOTTOM)

        ttk.Button(self.optionsFrame, text = "Next", command = self.next).pack()

        self.window.mainloop()

        self.window.destroy()

        return self.MOTD
