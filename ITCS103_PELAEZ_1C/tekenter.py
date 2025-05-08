import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Hard-coded Tkinter Example")
window.geometry("2025x1075")  # Set the size of the window

# Create a label and add it to the window
label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)  # Add some padding around the label

# Function to update the label when the button is clicked
def change_label_text():
    label.config(text="Button Clicked!")

# Create a button that will call the function when clicked
button = tk.Button(window, text="Click Me", command=change_label_text)
button.pack()

# Run the application
window.mainloop()
