__ErrorInfo__   = {'program':       "Directory_Inventory.Directory_Inventory",
                   'version':       "0.0.0",
                   'ErrorTab':      "Small Apps"}

__ModuleInfo__  = {"Programmer":     "Themadhood Pequot",
                   "Legal":        f"""
{__ErrorInfo__['program']} (c) 2026 THEMADHOOD Software
All rights reserved. Redistribution, modification, or reverse engineering
of this software is prohibited without explicit written permission.
Unauthorized use may result in legal action.""",
                   "Date":          "5/29/2026",
                   "Time":          "0000:00:00: 01:00:00",
                   "Update":        """
""",
                   "Info":          """
"""}


try:
    from .FrontEnd import DirectoryListFrontEnd
except ImportError:
    from FrontEnd import DirectoryListFrontEnd


DirectoryListFrontEnd()
