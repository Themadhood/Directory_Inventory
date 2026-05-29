__ErrorInfo__   = {'program':       "Directory_Inventory.FrontEnd",
                   'version':       "0.0.2",
                   'ErrorTab':      "Small Apps"}

__ModuleInfo__  = {"Programmer":     "Themadhood Pequot",
                   "Legal":        f"""
{__ErrorInfo__['program']} (c) 2026 THEMADHOOD Software
All rights reserved. Redistribution, modification, or reverse engineering
of this software is prohibited without explicit written permission.
Unauthorized use may result in legal action.""",
                   "Date":          "1/14/2025",
                   "Time":          "0000:00:00: 01:00:00",
                   "Update":        """
Split frontend from backend.
Added flat/tree output toggle.
""",
                   "Info":          """
GUI driver for directory export.
Supports flat file listing and tree output.
"""}



#Imports
import io,sys,os
import tkinter as TK
from tkinter import filedialog as FD
from tkinter import messagebox as MB

try:
    from .BackEnd import DirectoryListBackEnd, FLAT_MODE, TREE_MODE
except ImportError:
    from BackEnd import DirectoryListBackEnd, FLAT_MODE, TREE_MODE


def resource_path(relative_path):    
    try:       
        base_path = sys._MEIPASS
    except:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)
ICON = resource_path(f"Icon.png")




#constants
BG = "black"
FG = "white"
BUTTON_PAD_X = 10
BUTTON_PAD_Y = 10



###########################################################################
################################ Program ##################################
###########################################################################

class DirectoryListFrontEnd(TK.Tk):
    def __init__(self):
        TK.Tk.__init__(self)

        self._BackEnd = DirectoryListBackEnd()
        self._OutputMode = TK.StringVar(value=FLAT_MODE)

        self.title("List Directory")
        self.geometry("+341+285")
        self.resizable(width=False, height=False)
        self.config(bg=BG)
        self._icon_img = TK.PhotoImage(file=ICON)
        self.iconphoto(True, self._icon_img)

        self._BuildGui()
        self.mainloop()


    def _BuildGui(self):
        TK.Button(takefocus=True, text="Directory",
                  command=self.SetDr).grid(row=0, column=0,
                                           padx=BUTTON_PAD_X,
                                           pady=BUTTON_PAD_Y)

        self._DirLbl = TK.Label(bg=BG, fg=FG, takefocus=True,
                                text=str(self._BackEnd.DirPath()),
                                wraplength=200)
        self._DirLbl.grid(row=1, column=0,
                          padx=BUTTON_PAD_X,
                          pady=BUTTON_PAD_Y)

        TK.Label(bg=BG, fg=FG, takefocus=True,
                 text="---->>").grid(row=1, column=1,
                                      padx=BUTTON_PAD_X,
                                      pady=BUTTON_PAD_Y)

        TK.Button(takefocus=True, text="Text File",
                  command=self.SaveFile).grid(row=1, column=2,
                                              padx=BUTTON_PAD_X,
                                              pady=BUTTON_PAD_Y)

        modeFrame = TK.Frame(bg=BG)
        modeFrame.grid(row=2, column=0, columnspan=3,
                       padx=BUTTON_PAD_X,
                       pady=(0, BUTTON_PAD_Y))

        TK.Radiobutton(modeFrame, bg=BG, fg=FG, selectcolor=BG,
                       activebackground=BG, activeforeground=FG,
                       text="File List", variable=self._OutputMode,
                       value=FLAT_MODE).grid(row=0, column=0,
                                             padx=BUTTON_PAD_X)

        TK.Radiobutton(modeFrame, bg=BG, fg=FG, selectcolor=BG,
                       activebackground=BG, activeforeground=FG,
                       text="Folder Structure", variable=self._OutputMode,
                       value=TREE_MODE).grid(row=0, column=1,
                                             padx=BUTTON_PAD_X)


    def SetDr(self):
        path = FD.askdirectory()
        if path == "":
            return

        try:
            self._BackEnd.SetDirPath(path)
            self._DirLbl.config(text=str(self._BackEnd.DirPath()))
        except Exception as exception:
            MB.showerror("Error", str(exception))


    def SaveFile(self):
        if self._BackEnd.DirPath() is None:
            MB.showwarning("Warning", "Directory path is not selected")
            return

        saveFile = FD.asksaveasfile(filetypes=[("Text Document", "*.txt")],
                                    defaultextension=".txt")
        if saveFile is None:
            MB.showwarning("Warning", "Please select a file to save")
            return

        path = saveFile.name
        saveFile.close()

        try:
            fileText = self._BackEnd.BuildText(self._OutputMode.get())

            with io.open(path, "w", encoding="utf-8") as file:
                file.write(fileText)

            self._BackEnd.ClearDirPath()
            self._DirLbl.config(text=str(self._BackEnd.DirPath()))
        except Exception as exception:
            MB.showerror("Error", str(exception))



###########################################################################
###########################################################################
###########################################################################

if __name__ == "__main__":
    DirectoryListFrontEnd()
