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
        self.ENFORCE_WHITELIST = ""
        self.ONLINE_MODE = ""
        self.MAX_PLAYERS = ""
        self.PORT = ""
        
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

        # Get max players and port from text boxes
        max_players = self.txtMaxPlayers.get()
        port = self.txtPort.get()

        # Ensure all required data was collected
        # Exit the window
        if self.ENFORCE_WHITELIST and self.ONLINE_MODE and max_players.isnumeric() and port.isnumeric():
            self.MAX_PLAYERS = max_players
            self.PORT = port
            self.window.quit()
            self.window.destroy()

    # Set instance values when the dropdowns are changed
    def SetEWL(self, *args): self.ENFORCE_WHITELIST = self.enforce_whitelist_var.get()
    def SetOLM(self, *args): self.ONLINE_MODE = self.online_mode_var.get()

    def Render(self):
        """Renders the interface"""

        self.mainFrame.pack()

        self.enforce_whitelist_var = tkinter.StringVar()
        self.online_mode_var = tkinter.StringVar()

        self.enforce_whitelist_var.set('false')
        self.online_mode_var.set('true')

        self.enforce_whitelist_var.trace("w", self.SetEWL)
        self.online_mode_var.trace("w", self.SetOLM)

        ttk.Label(self.mainFrame, text = "Enforce Whitelist: ").grid(row = 0, column = 0)
        ttk.OptionMenu(self.mainFrame, self.enforce_whitelist_var, 'false', *['true', 'false']).grid(row = 0, column = 1)

        ttk.Label(self.mainFrame, text = "Online Mode: ").grid(row = 1, column = 0)
        ttk.OptionMenu(self.mainFrame, self.online_mode_var, 'true', *['true', 'false']).grid(row = 1, column = 1)

        ttk.Label(self.mainFrame, text = "Max Players: ").grid(row = 2, column = 0)
        self.txtMaxPlayers = ttk.Entry(self.mainFrame, width = 10)
        self.txtMaxPlayers.insert(0, "20")
        self.txtMaxPlayers.grid(row = 2, column = 1)

        ttk.Label(self.mainFrame, text = "Port: ").grid(row = 3, column = 0)
        self.txtPort = ttk.Entry(self.mainFrame, width = 10)
        self.txtPort.insert(0, "25565")
        self.txtPort.grid(row = 3, column = 1)

        self.optionsFrame.pack(side = tkinter.BOTTOM)

        ttk.Button(self.optionsFrame, text = "Next", command = self.next).pack()

        self.window.mainloop()
        
        data = {
            "ENFORCE_WHITELIST": self.ENFORCE_WHITELIST,
            "ONLINE_MODE": self.ONLINE_MODE,
            "MAX_PLAYERS": self.MAX_PLAYERS,
            "PORT": self.PORT
        }

        return data
