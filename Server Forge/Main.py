from UI import ServerInit, ServerConfig, ServerMotd
import os, sys

# Get the current directory of this app for use with writting server files
# Try handles the executable version
# Except handles running this file as a .py
try:
    CURRENT_DIR = sys._MEIPASS
except AttributeError:
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class Server:
    def GetServerInfo(self):
        """Renders the UI windows in order and sets the returned data as instance variables"""

        serverInitData = ServerInit.Interface().Render()
        self.name = serverInitData["SERVER_NAME"]
        self.saveDir = serverInitData["SERVER_SAVE_DIR"]

        serverConfigData = ServerConfig.Interface(self.name).Render()
        self.gamemode = serverConfigData["GAME_MODE"]
        self.difficulty = serverConfigData["DIFFICULTY"]

        self.motd = ServerMotd.Interface(self.name).Render()

        del serverInitData, serverConfigData

    def CreateDirectory(self):
        """Creates the directory for the server files to be written to"""

        # Check if a folder exists with the same name in the location to save the server to
        # If it doesn't, make the folder for the server
        # If it does, use the naming convention "servername (1)" and check if that exists or increment the (1) to (2) etc.
        if not os.path.exists(os.path.join(self.saveDir, self.name)):
            os.makedirs(os.path.join(self.saveDir, self.name))
            self.dir = os.path.join(self.saveDir, self.name)
        else:
            i = 1
            while True:
                if not os.path.exists(os.path.join(self.saveDir, self.name + f" ({i})")):
                    os.makedirs(os.path.join(self.saveDir,  self.name + f" ({i})"))
                    self.dir = os.path.join(self.saveDir,  self.name + f" ({i})")
                    del i
                    break

                i += 1

    def WriteFiles(self):
        """Writes server files to the server directory from templates"""

        # eula.txt
        with open(os.path.join(self.dir, "eula.txt"), "w") as f:
            f.write("eula=true")

        # start.bat
        with open(os.path.join(self.dir, "start.bat"), "w") as f:
            f.write("java -Xmx1024M -Xms1024M -jar server.jar")

        # server.jar
        with open(os.path.join(self.dir, "server.jar"), "wb") as f:
            with open(os.path.join(CURRENT_DIR, "templates", "server.jar.template"), "rb") as tmp:
                f.write(tmp.read())

        # server.properties
        with open(os.path.join(self.dir, "server.properties"), "w") as f:
            with open(os.path.join(CURRENT_DIR, "templates", "server.properties.template"), "r") as tmp:
                f.write(
                    tmp.read()
                        # Replace the 'template values'
                        .replace("|GAMEMODE|", self.gamemode)
                        .replace("|DIFFICULTY|", self.difficulty)
                        .replace("|SERVER_NAME|", self.name)
                        .replace("|MOTD|", self.motd)
                )

if __name__ == "__main__":
    SERVER = Server()

    SERVER.GetServerInfo()
    SERVER.CreateDirectory()
    SERVER.WriteFiles()
