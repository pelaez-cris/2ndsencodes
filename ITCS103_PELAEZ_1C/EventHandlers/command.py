import tkinter as tk

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"
def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

window = tk.Tk()
window.geometry("2025x1075")

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease =tk.Button(window,text='-', command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nesw")

window.mainloop()
