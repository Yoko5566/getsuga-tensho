# Getsuga Tensho

A tiny Python text-based fan project.

The program starts a simple command-line battle. Enter the correct skill command to update a generated `test.txt` file and complete the story.

## How it works

1. Run the program.
2. The game creates or resets `test.txt`.
3. Enter a command.
4. If the command is not recognized, the program asks again.
5. Enter `月牙天沖`.
6. The program updates `test.txt` and opens the result automatically.

## Run from source

Requirements:

- Windows
- Python 3

Run:

```powershell
python app.py
```

## Build a Windows executable

Install PyInstaller:

```powershell
python -m pip install pyinstaller
```

Build:

```powershell
pyinstaller --onefile --name "月牙天沖" app.py
```

The executable will be created under `dist/`.

## Disclaimer

This is an unofficial, non-commercial fan-made educational project created for learning Python, file I/O, command-line interaction, packaging, and Git/GitHub workflow.

BLEACH-related names, characters, techniques, and story elements belong to their respective rights holders. This repository does not include official artwork, music, logos, or other copyrighted media.

## License

The original source code in this repository is released under the MIT License. The license does not grant rights to third-party intellectual property referenced by the fan project.
