import tkinter
from tkinter import ttk, filedialog
import os, sys

# Get the current directory of this file for use in finding the icon file
# Try handles the executable version
# Except handles running this file as a .py
try:
    CURRENT_DIR = f"{sys._MEIPASS}/UI"
except AttributeError:
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class Interface:
    def __init__(self):
        """Sets up the interface"""

        # Variables to store data collected from this interface
        self.SERVER_NAME = ""
        self.SERVER_SAVE_DIR = ""
        
        # Set up the window
        self.window = tkinter.Tk()
        self.window.title("Server Forge")
        self.window.iconbitmap(os.path.join(CURRENT_DIR, os.pardir, "assets", "Favicon.ico"))
        self.window.minsize(500, 200)
        self.window.maxsize(500, 200)

        # Set up tkinter frames
        self.mainFrame = ttk.Frame(self.window, width = 100, height = 90)
        self.optionsFrame = ttk.Frame(self.window, width = 100, height = 10)

    def next(self):
        """Gets the text entered in the textbox and returns the value to Main"""

        # Get server name from text box
        serverName = self.txtServerName.get()

        # Ensure all required data was collected
        # Exit the window loop to proceed
        if serverName and self.SERVER_SAVE_DIR:
            self.SERVER_NAME = serverName
            self.window.quit()

        del serverName

    def showFileDialog(self):
        """Shows the file dialog to choose where to save the server folder"""

        # Show file dialogue for user to select where to save their server to
        serverSaveDir = filedialog.askdirectory()

        # Verify they chose a folder (didn't close the file dialogue manually)
        # Display the save directory in a disabled textbox
        if serverSaveDir:
            lblSaveLocation = ttk.Entry(self.mainFrame, width = 50)
            lblSaveLocation.insert(0, serverSaveDir)
            lblSaveLocation.configure(state = tkinter.DISABLED)
            lblSaveLocation.grid(row = 1, column = 1)

            self.SERVER_SAVE_DIR = serverSaveDir

        del serverSaveDir

    def Render(self):
        """Renders the interface"""

        self.mainFrame.pack()

        ttk.Label(self.mainFrame, text = "Server Name:").grid(row = 0, column = 0)

        self.txtServerName = ttk.Entry(self.mainFrame, width = 50)
        self.txtServerName.grid(row = 0, column = 1)

        ttk.Label(self.mainFrame, text = "Location:").grid(row = 1, column = 0)

        ttk.Button(self.mainFrame, text = "Browse", command = self.showFileDialog).grid(row = 1, column = 2)

        self.optionsFrame.pack(side = tkinter.BOTTOM)

        ttk.Button(self.optionsFrame, text = "Next", command = self.next).pack()

        self.window.mainloop()
        
        self.window.destroy()

        data = {
            "SERVER_NAME": self.SERVER_NAME,
            "SERVER_SAVE_DIR": self.SERVER_SAVE_DIR
        }

        return data
