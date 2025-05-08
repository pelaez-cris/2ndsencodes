import tkinter as tk

def handle_click(event):
    print("Napindot kita!")
window = tk.Tk()

button = tk.Button(window, text="Click me!")
button.pack()
button.bind("<Button-1>", handle_click)

window.mainloop()