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
        
        # Set up the window
        self.window = tkinter.Tk()
        self.window.title(f"Server Forge - {serverName}")
        self.window.iconbitmap(os.path.join(CURRENT_DIR, os.pardir, "assets", "Favicon.ico"))
        self.window.minsize(500, 200)
        self.window.maxsize(500, 200)

        # Set up tkinter frames
        self.mainFrame = ttk.Frame(self.window, width = 100, height = 90)
        self.optionsFrame = ttk.Frame(self.window, width = 100, height = 10)
        self.gamemodeFrame = ttk.Frame(self.mainFrame, width = 50, height = 90)
        self.difficultyFrame = ttk.Frame(self.mainFrame, width = 50, height = 90)

    def next(self):
        """Gets the choices and returns them to Main"""

        # Ensure all required data was collected
        # Exit the window loop to proceed
        if self.GAME_MODE and self.DIFFICULTY:
            self.window.quit()

    def chooseGamemode(self):
        """Sets the gamemode from the radio buttons"""

        # Set the gamemode when user clicks a radio button
        self.GAME_MODE = self.gamemodeChoice.get()

    def chooseDifficulty(self):
        """Sets the difficulty from the radio buttons"""

        # Set the difficulty when user clicks a radio button
        self.DIFFICULTY = self.difficultyChoice.get()

    def Render(self):
        """Renders the interface"""

        self.gamemodeChoice = tkinter.StringVar()
        self.difficultyChoice = tkinter.StringVar()
        
        self.mainFrame.pack()
        self.gamemodeFrame.grid(row = 0, column = 0)
        self.difficultyFrame.grid(row = 0, column = 1)

        ttk.Label(self.gamemodeFrame, text = "Gamemode:").pack(anchor = tkinter.W)

        ttk.Radiobutton(self.gamemodeFrame, text = "Survival", var = self.gamemodeChoice, value = "survival", command = self.chooseGamemode).pack(anchor = tkinter.W)
        ttk.Radiobutton(self.gamemodeFrame, text = "Creative", var = self.gamemodeChoice, value = "creative", command = self.chooseGamemode).pack(anchor = tkinter.W)
        ttk.Radiobutton(self.gamemodeFrame, text = "Adventure", var = self.gamemodeChoice, value = "adventure", command = self.chooseGamemode).pack(anchor = tkinter.W)

        ttk.Label(self.difficultyFrame, text = "Difficulty:").pack(anchor = tkinter.W)

        ttk.Radiobutton(self.difficultyFrame, text = "Peaceful", var = self.difficultyChoice, value = "peaceful", command = self.chooseDifficulty).pack(anchor = tkinter.W)
        ttk.Radiobutton(self.difficultyFrame, text = "Easy", var = self.difficultyChoice, value = "easy", command = self.chooseDifficulty).pack(anchor = tkinter.W)
        ttk.Radiobutton(self.difficultyFrame, text = "Normal", var = self.difficultyChoice, value = "normal", command = self.chooseDifficulty).pack(anchor = tkinter.W)
        ttk.Radiobutton(self.difficultyFrame, text = "Hard", var = self.difficultyChoice, value = "hard", command = self.chooseDifficulty).pack(anchor = tkinter.W)

        self.optionsFrame.pack(side = tkinter.BOTTOM)

        ttk.Button(self.optionsFrame, text = "Next", command = self.next).pack()

        self.window.mainloop()

        self.window.destroy()

        data = {
            "GAME_MODE": self.GAME_MODE,
            "DIFFICULTY": self.DIFFICULTY
        }

        return data
