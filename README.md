Modern Calculator (Tkinter)

A simple modern-style calculator built using Python and Tkinter.
It supports basic arithmetic operations with a clean dark UI.

 -Features

Modern dark theme interface

Large, easy-to-read display

Basic operations:

Addition (+)

Subtraction (-)

Multiplication (×)

Division (÷)

Percentage (%)

Clear button (C)

Backspace button (⌫)

Error handling for invalid expressions

- Requirements

Python 3.x

Tkinter (comes pre-installed with most Python distributions)

- How to Run

Save the code in a file:

calculator.py


Run the program:

python calculator.py

- Interface Overview

Top section → display screen

Bottom section → calculator buttons

Golden buttons → operations

Dark buttons → numbers and controls

- Notes

The calculator uses Python eval() to compute expressions.

Multiplication and division symbols are converted internally:

× → *

÷ → /

- Project Structure
calculator.py   # Main application file
README.md       # Project documentation

- Possible Improvements

Keyboard input support

Scientific calculator mode

History panel

Better button animations

Safer expression parser (instead of eval)
