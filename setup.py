from cx_Freeze import setup, Executable

base = None    

executables = [Executable("ezexp.py", base=base)]

packages = ["idna", "pyautogui", "keyboard", "tkinter"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Hypixel Skyblock easy ench xp",
    options = options,
    version = "0.1",
    description = 'Hypixel Skyblock easy ench xp',
    executables = executables
)
