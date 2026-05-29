__ErrorInfo__   = {'program':       "TMP_DrToTxtLst_BackEnd",
                   'version':       "0.0.2",
                   'ErrorTab':      "Functions"}

__ModuleInfo__  = {"Programmer":     "Themadhood Pequot",
                   "Legal":        f"""
{__ErrorInfo__['program']} (c) 2026 THEMADHOOD Software
All rights reserved. Redistribution, modification, or reverse engineering
of this software is prohibited without explicit written permission.
Unauthorized use may result in legal action.""",
                   "Date":          "5/29/2026",
                   "Time":          "0000:00:00: 01:00:00",
                   "Update":        """
Split frontend from backend.
Added tree generation support.
""",
                   "Info":          """
Directory listing and tree generation functions.
"""}



#Imports
from pathlib import Path







#constants
FLAT_MODE = "flat"
TREE_MODE = "tree"
TREE_BRANCH = "├── "
TREE_LAST_BRANCH = "└── "
TREE_PIPE = "│   "
TREE_SPACE = "    "



###########################################################################
################################ Program ##################################
###########################################################################

class DirectoryListBackEnd:
    def __init__(self, dirPath=None):
        self._DirPath = None
        if dirPath is not None:
            self.SetDirPath(dirPath)


    def SetDirPath(self, dirPath):
        path = Path(dirPath)
        if not path.exists():
            raise FileNotFoundError(f"Directory does not exist: {path}")
        if not path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {path}")

        self._DirPath = path
        return self._DirPath


    def DirPath(self):
        return self._DirPath


    def ClearDirPath(self):
        self._DirPath = None


    def BuildText(self, mode=FLAT_MODE):
        if self._DirPath is None:
            raise ValueError("Directory path is not selected")

        if mode == TREE_MODE:
            return self.ListDirectoryTree(self._DirPath)

        return self.ListDirectoryContents(self._DirPath)


    def ListDirectoryContents(self, dirPath=None):
        path = self._ResolvePath(dirPath)
        entries = self._SortedEntries(path)
        return "\n".join(entry.name for entry in entries) + "\n"


    def ListDirectoryTree(self, dirPath=None):
        path = self._ResolvePath(dirPath)
        textLst = [path.name]
        textLst.extend(self._BuildTreeLines(path))
        return "\n".join(textLst) + "\n"


    def _ResolvePath(self, dirPath=None):
        if dirPath is None:
            if self._DirPath is None:
                raise ValueError("Directory path is not selected")
            return self._DirPath

        path = Path(dirPath)
        if not path.exists():
            raise FileNotFoundError(f"Directory does not exist: {path}")
        if not path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {path}")
        return path


    def _SortedEntries(self, path):
        return sorted(path.iterdir(), key=lambda entry: (not entry.is_dir(), entry.name.lower()))


    def _BuildTreeLines(self, path, prefix=""):
        entries = self._SortedEntries(path)
        lines = []

        for index, entry in enumerate(entries):
            isLast = index == len(entries) - 1
            branch = TREE_LAST_BRANCH if isLast else TREE_BRANCH
            lines.append(f"{prefix}{branch}{entry.name}")

            if entry.is_dir():
                nextPrefix = prefix + (TREE_SPACE if isLast else TREE_PIPE)
                lines.extend(self._BuildTreeLines(entry, nextPrefix))

        return lines



###########################################################################
###########################################################################
###########################################################################

if __name__ == "__main__":
    print("This is a backend module. Run FrontEnd.py to open the GUI.")
