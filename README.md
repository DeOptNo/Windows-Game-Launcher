**IT IS HIGHLY RECOMMENDED TO DOWNLOAD THE LATEST VERSION OF PYTHON FROM THE MICROSOFT STORE!** **You may also need Visual Studio Code if you cannot edit the Python code with Windows Notepad.**

# Windows Game Launcher
This is a custom game launcher I created in Python. It's easy to make your own version with your own games.

**_How to Add Your Games to the Launcher_**
1. Download the Python code file and create a folder in a location that is easy to remember and accessible (recommended locations: Documents, Desktop, or anywhere in your user directory).

2. Inside this folder, create a subfolder called "Games".
   ![image](https://github.com/user-attachments/assets/786b341e-aff9-4959-a880-c665fc5d1ca4)


4. Add your game executable (.exe) files or Internet shortcuts into the "Games" folder.

5. Within the "Games" folder, create another subfolder called "Icons".
![image](https://github.com/user-attachments/assets/a86b1ddc-7f7e-4310-b52f-29e721e00b54)


6. Open the Python file in Notepad to edit the directory paths for the files.

**Things to Change:**
Insert the directory path inside the quotation marks like this: 
`C:\Where\ever\the\files\are\in\your\pc\drive`

Example:
```python
ICONS_FOLDER = r"C:\ThisPC\Users\me\Documents\GameLauncher\Games\Icons"


GAMES_FOLDER = r"C:\ThisPC\Users\me\Documents\GameLauncher\Games\"
ICONS_FOLDER = r"C:\ThisPC\Users\me\Documents\GameLauncher\Games\Icons"
FALLBACK_ICON_PATH = r"C:\ThisPC\Users\me\Documents\GameLauncher\Games\Icons\fallback.png"  # Fallback icon image
HOVER_SOUND_PATH = r"C:\ThisPC\Users\me\Documents\GameLauncher\Games\hover.wav"
LAUNCH_SOUND_PATH = r"C:\ThisPC\Users\me\Documents\GameLauncher\Games\launch.wav"
```

6. Download the sound files and ensure they are named `hover.wav` or `launch.wav`; otherwise, they will not work.

8. After updating the directory paths, if double-clicking the .py file does not launch the program and you have Python installed from the Microsoft Store, download Visual Studio Code and the Python extension. You will need to install the required dependencies and packages for it to run properly. (I know this because it worked for my test subject, a friend of mine.)

**Coming soon: I will provide a list of necessary packages once I recall them, as there are a few.**
