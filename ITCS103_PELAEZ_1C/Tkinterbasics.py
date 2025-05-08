import os 
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("MORN HAB")
window.geometry("2025x1075")

label = ttk.Label(master = window, text="MORN HAB", font = "TimesNewRoman 35 bold")
label.pack(padx = 200)

button = ttk.Button(master = window, text="PINDUTE", command=window.destroy, padding = 15)
button.pack(pady = 200)

entry = ttk.Entry(master = window)
entry.pack()

window.mainloop()
os.system("cls")
