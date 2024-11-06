# Structify

Structify is a Python-based command-line tool that generates a project directory structure based on a simple text file. It provides a convenient way to create consistent and organized project structures for software development projects.


https://github.com/user-attachments/assets/33d20ef2-3ac8-48b7-9c56-2d08604fd7b8


## Features

- Create project structures from a simple text-based configuration file
- Supports nested directories and files
- Automatically creates the specified directory structure in the desired output location

## Installation

Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/808Kamalesh/structify.git
cd structify
```

# Install dependencies

```bash
pip install -r requirements.txt
```

# Usage

To generate a project structure, provide a structure file as an argument:

```bash
python structify.py <structure_file> --output <output_directory>
```

# Example

```bash
python structify.py my_structure.txt --output ./my_project
```

# Structure File Format

Make your structure in a text file with indented lines representing directory. For example:
my_structure.txt should look like-

```bash
MyProjectRoot
    src/
        main.py
        utils/
            helper.py
    README.md
    .gitignore
```

# Output

```bash

D:\Structify>python structify.py my_structure.txt --output ./my_project

░█▀▀░▀█▀░█▀▄░█░█░█▀▀░▀█▀░▀█▀░█▀▀░█░█
░▀▀█░░█░░█▀▄░█░█░█░░░░█░░░█░░█▀▀░░█░
░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░░░░▀░

Output directory: D:\Structify\my_project\MyProjectRoot

Structure File Content:
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ MyProjectRoot                                                                                                                      │
│     src/                                                                                                                           │
│         main.py                                                                                                                    │
│         utils/                                                                                                                     │
│             helper.py                                                                                                              │
│     README.md                                                                                                                      │
│     .gitignore                                                                                                                     │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
  Creating project structure... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100%

✨ Project structure created successfully!

Created Project Structure:
MyProjectRoot
└── MyProjectRoot
    ├── .gitignore
    ├── README.md
    └── src
        ├── main.py
        └── utils
            └── helper.py

  Project Statistics   
┏━━━━━━━━━━━━━┳━━━━━━━┓
┃ Type        ┃ Count ┃
┡━━━━━━━━━━━━━╇━━━━━━━┩
│ Files       │ 4     │
│ Directories │ 3     │
│ Total Items │ 7     │
└─────────────┴───────┘
```

# Author : 808Kamalesh



