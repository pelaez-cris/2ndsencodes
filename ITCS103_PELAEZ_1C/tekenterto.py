import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Advanced Tkinter Example")
window.geometry("2025x1075")  # Set the size of the window

# Label for greeting
greeting_label = tk.Label(window, text="Enter your name:", font=("Arial", 14))
greeting_label.pack(pady=20)

# Entry widget for user input
name_entry = tk.Entry(window, font=("Arial", 14))
name_entry.pack(pady=10)

# Label to display the greeting
personalized_greeting = tk.Label(window, text="", font=("Arial", 14))
personalized_greeting.pack(pady=20)

# Canvas to draw a moving rectangle
canvas = tk.Canvas(window, width=600, height=200, bg="lightgray")
canvas.pack()

# Function to update the greeting based on the name input
def display_greeting():
    name = name_entry.get()  # Get the name from the entry widget
    if name:
        personalized_greeting.config(text=f"Hello, {name}!")
    else:
        personalized_greeting.config(text="Hello, Stranger!")

# Function to animate a moving rectangle
def animate_rectangle():
    x = 0
    y = 100
    rectangle = canvas.create_rectangle(x, y, x+50, y+30, fill="blue")
    
    def move_rect():
        nonlocal x
        if x < 600:
            x += 5
            canvas.coords(rectangle, x, y, x+50, y+30)
            window.after(50, move_rect)  # Move the rectangle every 50 milliseconds

    move_rect()

# Button to trigger the greeting display
greet_button = tk.Button(window, text="Display Greeting", font=("Arial", 12), command=display_greeting)
greet_button.pack(pady=10)

# Button to trigger the rectangle animation
animate_button = tk.Button(window, text="Start Animation", font=("Arial", 12), command=animate_rectangle)
animate_button.pack(pady=10)


button = tk.Button(master = window, text="PINDUTE", command=window.destroy)
button.pack(pady = 20)


# Run the application
window.mainloop()
