# Directory Inventory

Directory Inventory is a lightweight utility that exports the contents of a folder to a text file.

The application provides a simple graphical interface that allows you to:

* Select a folder to scan.
* Choose where to save the output file.
* Export either a simple file list or a complete folder structure.
* Generate easy-to-share text documentation of a directory.

## Features

### File List

Exports the names of files and folders located in the selected directory.

**Example**

```text
FileA.txt
FileB.pdf
Photos
Documents
```

### Folder Structure

Exports the directory hierarchy using a tree-style layout.

**Example**

```text
Project
├── README.md
├── Source
│   ├── Main.py
│   └── BackEnd.py
└── Data
    └── Config.json
```

## Usage

![Screenshot 2025-01-14 130622](https://github.com/user-attachments/assets/181e9e41-76dd-46c8-ba19-ce61063380ce)

1. Launch the application.
2. Click **Directory** and select the folder you want to export.
3. Select the desired output format:

   * File List
   * Folder Structure
4. Click **Text File**.
5. Choose the output file location and name.
6. Save the file.

## Project Structure

```text
FrontEnd.py
└── User Interface

BackEnd.py
└── Directory Reading
└── File List Generation
└── Folder Structure Generation
```

## Requirements

* Python 3.x
* tkinter (included with most Python installations)

## License

See the LICENSE file included with this project.
