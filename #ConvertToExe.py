#program:       ConvertToExe
#purpose:       is a game
#progamer:      Madison Arndt 10/26/2023

import PyInstaller.__main__
import os

_FP = os.path.dirname(os.path.abspath(__file__))


#old specs
try:
    os.remove(f"{_FP}/Directory_Inventory.spec")
except:
    print("failed run")

iconPath = os.path.dirname(os.path.abspath(__file__))
#iconPath = f"{os.path.dirname(_FP)}"

opt = [f'{_FP}/Directory_Inventory.py',
       '--noconsole',
       '--noconfirm',
       '--onefile',
       #icon
       f"--add-data={os.path.join(iconPath, 'Icon.png')}:.",
       f"--icon={os.path.join(iconPath, 'Icon.png')}"]


#cleen app
opt.append("--clean")

#run app maker
PyInstaller.__main__.run(opt)





















