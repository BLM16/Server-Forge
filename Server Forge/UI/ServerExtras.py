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
        self.FORCE_GAMEMODE = ""
        self.SPAWN_MONSTERS = ""
        self.PVP = ""
        self.COMMAND_BLOCK = ""
        
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
        """Gets the dropdown settings and returns them to Main"""

        # Ensure all required data was collected
        # Exit the window
        if self.FORCE_GAMEMODE and self.SPAWN_MONSTERS and self.PVP and self.COMMAND_BLOCK:
            self.window.quit()
            self.window.destroy()

    # Set instance values when the dropdowns are changed
    def SetFGM(self, *args): self.FORCE_GAMEMODE = self.force_gamemode_var.get()
    def SetSMT(self, *args): self.SPAWN_MONSTERS = self.spawn_monsters_var.get()
    def SetPVP(self, *args): self.PVP = self.pvp_var.get()
    def SetCMD(self, *args): self.COMMAND_BLOCK = self.command_block_var.get()

    def Render(self):
        """Renders the interface"""

        self.mainFrame.pack()

        self.force_gamemode_var = tkinter.StringVar()
        self.spawn_monsters_var = tkinter.StringVar()
        self.pvp_var = tkinter.StringVar()
        self.command_block_var = tkinter.StringVar()

        self.force_gamemode_var.set('false')
        self.spawn_monsters_var.set('true')
        self.pvp_var.set('true')
        self.command_block_var.set('false')

        self.force_gamemode_var.trace("w", self.SetFGM)
        self.spawn_monsters_var.trace("w", self.SetSMT)
        self.pvp_var.trace("w", self.SetPVP)
        self.command_block_var.trace("w", self.SetCMD)

        ttk.Label(self.mainFrame, text = "Force Gamemode: ").grid(row = 0, column = 0)
        ttk.OptionMenu(self.mainFrame, self.force_gamemode_var, 'false', *['true', 'false']).grid(row = 0, column = 1)

        ttk.Label(self.mainFrame, text = "Spawn Monsters: ").grid(row = 1, column = 0)
        ttk.OptionMenu(self.mainFrame, self.spawn_monsters_var, 'true', *['true', 'false']).grid(row = 1, column = 1)

        ttk.Label(self.mainFrame, text = "PVP: ").grid(row = 2, column = 0)
        ttk.OptionMenu(self.mainFrame, self.pvp_var, 'true', *['true', 'false']).grid(row = 2, column = 1)

        ttk.Label(self.mainFrame, text = "Enable Command Blocks: ").grid(row = 3, column = 0)
        ttk.OptionMenu(self.mainFrame, self.command_block_var, 'false', *['true', 'false']).grid(row = 3, column = 1)

        self.optionsFrame.pack(side = tkinter.BOTTOM)

        ttk.Button(self.optionsFrame, text = "Next", command = self.next).pack()

        self.window.mainloop()
        
        data = {
            "FORCE_GAMEMODE": self.FORCE_GAMEMODE,
            "SPAWN_MONSTERS": self.SPAWN_MONSTERS,
            "PVP": self.PVP,
            "COMMAND_BLOCK": self.COMMAND_BLOCK
        }

        return data
