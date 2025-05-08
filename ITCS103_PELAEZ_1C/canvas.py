import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")

        # Create a canvas widget
        self.canvas = tk.Canvas(root, bg="white", width=2025, height=1075)
        self.canvas.pack()

        # Initialize drawing variables
        self.last_x = None
        self.last_y = None
        self.pen_color = "blue"  # Default color

        
        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        # Create a color selection button
        color_button = tk.Button(root, text="Choose Color", command=self.choose_color)
        color_button.pack()

    def start_drawing(self, event):
        """Start drawing on the canvas."""
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        """Draw a line from the last position to the current mouse position."""
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.pen_color, width=2)
            self.last_x = event.x
            self.last_y = event.y

    def stop_drawing(self, event):
        """Reset the last_x and last_y when the mouse button is released."""
        self.last_x = None
        self.last_y = None

    def choose_color(self):
        """Open a color chooser dialog to select colors."""
        color = tk.colorchooser.askcolor()[1]
        if color:
            self.pen_color = color


# Create the main application window
root = tk.Tk()
app = DrawingApp(root)

# Start the Tkinter event loop
root.mainloop()