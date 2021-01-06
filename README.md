<h1>
    <img src="./public/Icon_32x32.png" style="vertical-align: middle;" />
    <span style="display: inline; vertical-align: middle;">Server Forge</span>
</h1>

[![Python](https://img.shields.io/static/v1?logo=data:image/png;base64,R0lGODlhEAAQAPZkAOu7GOu+IfPBGvrHGf3LG//MHOvCKv/PI//PJP/QJf/QJv/TLf3SL//TLv/TL+vFNOjHPf/TMP/UMP3VNv/WN/rTOf/XOP/XOf/XOvnVPv/YOuzORf3ZQf/aQf/aQv/bQv/bQ//bRP3dSv/eS//fTf3eTv/fTv/iVf/jV//jWP/mYf/nYf/nYvLhbvXjb/3pav/rbDJghzZmkDZnkTVokjZpkzZplDdoljdqljlsljhslzltmTpvmzpwnDtwnDtwnTxxnj1zoD1zoj10oT50oj51oz92pUB4pkB4p0F5qEJ7qkN8q0N9rUN9rkR9rUR+rUV/r0aAsEaAsUaBskeBskiDtEiEtUiFtkmFt0qHuUqGukuIu0yJvEyKvE2LvkyKv06NwE+NwVCPw1KRxv///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAGUALAAAAAAQABAAAAemgGWCZWFaUkxGQDeDjIJdZFJKRD04jYxXkUQ+ODWWZV9XTEQ5Mjk4lYxjYVxVUEdAPDWnZScjGWViX1RQSrA1vzFlIx0Tn1dUkkCnNMEbxAtlx0tHnY0dFwsHZVLTNGUtLywnJiHYCARlTEpDZS4wLCnk5gUCgkM+Ze/xHRoLCAUFLMEzAeGBgQAAAHiKVy5CgoCeysiTkIAMuohlKjgsMACjx0GBAAA7&label=Python&message=3.9.0&color=brightgreen&link=https://www.python.org/)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-blue.svg?label=License&link=https://mit-license.org/)](./LICENSE)

![](./public/Banner.png)

Developer: [Bradley Myers](https://github.com/BLM16/)

Date created: 23-11-2020 | Last updated: 30-12-2020

---

**Server Forge** is a tool to automate Minecraft Server file generation. It compiles the provided server information into the required files for a Minecraft server. *Featuring a simple UI, and eventually command line accessibility*, it is an easy tool to use that saves you the effort of editing property files and lets you spend your time playing, not messing with server settings.

**For more detailed information, please look at the [wiki](https://github.com/BLM16/Server-Forge/wiki).**

## Setup and Overview
**Make sure you have python 3 installed, and added to path.**

To get the latest [server.jar.template](./Server%20Forge/templates/server.jar.template), click [here](https://www.minecraft.net/en-us/download/server) and download the latest .jar file. Save the file to the [templates directory](./Server%20Forge/templates) as "server.jar.template".

Make sure you are in complience with the [Minecraft EULA](https://account.mojang.com/documents/minecraft_eula).

---

Server Forge uses the following folder structure:

| Folder / File                       |  Overview                                                                                   |
| ----------------------------------- | ------------------------------------------------------------------------------------------- |
| [public](./public)                  | Assets used outside of the project go here such as the banner and icon used in this readme. |
| [Server Forge](./Server%20Forge)    | All code and related assets go here such as the [UI](./Server%20Forge/UI) scripts and the [favicon](./Server%20Forge/assets/Favicon.ico) used in those windows. The server file [templates](./Server%20Forge/templates) also reside here. |
| [Main.py](./Server%20Forge/Main.py) | This is the main file for the project. It handles rendering the GUIs in order, storing server information, and creating server files. |
| [sf.bat](./sf.bat)                  | This batch file has premade scripts to help with compiling the project. This is the equivalent to a makefile. For more info on how to use it, click [here](https://github.com/BLM16/Server-Forge/wiki/sf.bat-usage). |

Server Forge uses Tkinter for the GUI. Tkinter comes preinstalled with python and it allows you to create simple GUIs, which we use in this project to have a visual way for users to provide server information. For more information on tkinter, look at [python's docs](https://docs.python.org/3/library/tkinter.html).

## Compiling and Distribution

To build the Server Forge app into an exe file, you need pyinstaller. To install pyinstaller, run the following command in a terminal.

```bat
pip install pyinstaller
```

Once pyinstaller is installed, you can use the premade scripts in [sf.bat](./sf.bat). To build the app in development/debug mode run the following command in a terminal from the root of this project, or by specifying the path to the batch file:

```bat
sf devbuild
```

To build the app for distribution without debug info, use this command:

```bat
sf build
```

## License
This tool is licensed under the [MIT License](./LICENSE)
