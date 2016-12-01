import tkinter as tk
from tkinter import filedialog


def fileopen():
    root = tk.Tk()
    root.withdraw()
    return(filedialog.askopenfilename())
