# Luhn Brute-force Trainer GUI

**Educational Tool to Learn the Luhn Algorithm Using Python and Tkinter**

## Description
This project is a graphical Python application designed to teach and demonstrate how the Luhn algorithm can be used to validate credit card numbers. It accepts the first 6 digits (BIN) and the last 4 digits of a card, then brute-forces the 6 missing middle digits to find combinations that result in valid Luhn numbers.

> ⚠️ **For educational and ethical use only.**
> This tool does not interact with or validate real credit card data. Use it strictly for algorithm learning and teaching purposes.

## Features
- Beginner-friendly Tkinter GUI
- Accepts input for BIN and last 4 digits
- Brute-forces the missing 6 digits and checks validity using Luhn algorithm
- Displays sample valid card numbers and total checked combinations

## How to Run

1. **Install Python 3** (if not already installed)
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/luhn-bruteforce-gui.git
   cd luhn-bruteforce-gui
   ```
3. Run the script:
   ```bash
   python luhn_gui.py
   ```

## Optional: Build Executable (Windows)

If you'd like to turn this script into a `.exe` file:
```bash
python -m pip install pyinstaller
pyinstaller --onefile --windowed luhn_gui.py
```
Your executable will appear in the `dist/` folder.

## Repository Contents
- `luhn_gui.py`: Main script with GUI interface
- `README.md`: This documentation file

## License
MIT License — free to use, share, and modify.

---
If you found this project useful for learning or teaching, feel free to contribute or star the repo!
