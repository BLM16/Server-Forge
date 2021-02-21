@ECHO off
TITLE Server Forge - Tools

SET retdir=%cd%
SET sfdir=%~dp0

ECHO.

IF [%1] NEQ [] ( SET command=%1 ) ELSE ( GOTO ERR )

cd %sfdir%

IF %command% == build ( GOTO BUILD )
IF %command% == devbuild ( GOTO DEVBUILD )
IF %command% == clean ( GOTO CLEAN )

GOTO ERR

:BUILD

    ECHO Building Program
    
    pyinstaller "Server Forge/Main.py" --name="ServerForge" --icon="Server Forge/assets/Favicon.ico" ^
        --add-data "Server Forge/assets;assets" ^
        --onefile --windowed ^
        --clean

    ECHO Output Directory: %sfdir%dist
    GOTO END

:DEVBUILD

    ECHO Building Program - Dev Mode

    pyinstaller "Server Forge/Main.py" --name="ServerForge" --icon="Server Forge/assets/Favicon.ico" ^
        --add-data "Server Forge/assets;assets" ^
        --onefile --windowed ^
        --debug=all --log-level=DEBUG ^
        --clean

    ECHO Output Directory: %sfdir%dist
    GOTO END

:CLEAN

    ECHO Cleaning Program

    IF EXIST "build" ( RMDIR /S /Q "build" )
    IF EXIST "dist" ( RMDIR /S /Q "dist" )
    IF EXIST "ServerForge.spec" ( DEL /Q "ServerForge.spec" )
    FOR /D /R . %%d IN ("*") DO ( IF EXIST "%%d\*.pyo" ( DEL /Q "%%d\*.pyo" ) )
    FOR /D /R . %%d IN ("__pycache__") DO ( IF EXIST "%%d" ( RMDIR /S /Q "%%d" ) )

    GOTO END

:ERR

    ECHO ERROR
    ECHO.
    cd %retdir%
    GOTO :EOF

:END

    ECHO Done
    ECHO.
    cd %retdir%
    GOTO :EOF
