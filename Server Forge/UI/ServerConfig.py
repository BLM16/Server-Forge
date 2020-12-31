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

        # Variables to store data collected from this interface
        self.GAME_MODE = ""
        self.DIFFICULTY = ""
        self.HARDCORE = ""
        
        # Set up the window
        self.window = tkinter.Tk()
        self.window.title(f"Server Forge - {serverName}")
        self.window.iconbitmap(os.path.join(CURRENT_DIR, os.pardir, "assets", "Favicon.ico"))
        self.window.minsize(500, 200)
        self.window.maxsize(500, 200)
        self.window.protocol("WM_DELETE_WINDOW", lambda: quit())

        # Set up tkinter frames
        self.mainFrame = ttk.Frame(self.window, width = 100, height = 90)
        self.optionsFrame = ttk.Frame(self.window, width = 100, height = 10)

    def next(self):
        """Gets the choices and returns them to Main"""

        # Ensure all required data was collected
        # Exit the window
        if self.GAME_MODE and self.DIFFICULTY:
            self.window.quit()
            self.window.destroy()

    # Set instance values when the dropdowns are changed
    def SetGM(self, *args): self.GAME_MODE = self.gamemode_var.get()
    def SetDF(self, *args): self.DIFFICULTY = self.difficulty_var.get()
    def SetHC(self, *args): self.HARDCORE = self.hardcore_var.get()

    def chooseGamemode(self):
        """Sets the gamemode from the radio buttons"""

        # Set the gamemode when user clicks a radio button
        self.GAME_MODE = self.gamemode_var.get()

    def chooseDifficulty(self):
        """Sets the difficulty from the radio buttons"""

        # Set the difficulty when user clicks a radio button
        self.DIFFICULTY = self.difficulty_var.get()

    def Render(self):
        """Renders the interface"""

        self.gamemode_var = tkinter.StringVar()
        self.difficulty_var = tkinter.StringVar()
        self.hardcore_var = tkinter.StringVar()

        self.gamemode_var.set('survival')
        self.difficulty_var.set('normal')
        self.hardcore_var.set('false')

        self.gamemode_var.trace("w", self.SetGM)
        self.difficulty_var.trace("w", self.SetDF)
        self.hardcore_var.trace("w", self.SetHC)
        
        self.mainFrame.pack()

        ttk.Label(self.mainFrame, text = "Gamemode: ").grid(row = 0, column = 0)
        ttk.OptionMenu(self.mainFrame, self.gamemode_var, 'survival', *['adventure', 'creative', 'survival']).grid(row = 0, column = 1)

        ttk.Label(self.mainFrame, text = "Difficulty: ").grid(row = 1, column = 0)
        ttk.OptionMenu(self.mainFrame, self.difficulty_var, 'normal', *['peaceful', 'easy', 'normal', 'hard']).grid(row = 1, column = 1)

        ttk.Label(self.mainFrame, text = "Hardcore: ").grid(row = 2, column = 0)
        ttk.OptionMenu(self.mainFrame, self.hardcore_var, 'false', *['true', 'false']).grid(row = 2, column = 1)

        self.optionsFrame.pack(side = tkinter.BOTTOM)

        ttk.Button(self.optionsFrame, text = "Next", command = self.next).pack()

        self.window.mainloop()

        data = {
            "GAME_MODE": self.GAME_MODE,
            "DIFFICULTY": self.DIFFICULTY,
            "HARDCORE": self.HARDCORE
        }

        return data
