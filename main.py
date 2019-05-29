"""
This Py sheet will handle the logic of the program
"""
import os
from textmanage import Notepad

np = Notepad()
np.read_file()
#This makes it work in both Windows and Linux OSes
clear = lambda: os.system("cls") if os.name == "nt" else os.system("clear")
# print("Executing Input-Loop")
while True:
    print('Use "~" to remove elements, "@@" to show the buffer and "!" to exit the program\n')
    np.show_text()
    t = input()
    clear()
    if t == "!": break
    if t == "~":
        np.remove(input("What do you want to remove? "))
        continue
    if t == "@@": continue
    np.buffer(t)
    # print("Loop end reached")
np.write_to_file()