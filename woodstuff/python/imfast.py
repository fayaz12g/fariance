import tkinter as tk

def display_file_content(filename):
    # Read the file content into a list of lines
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Function to display the next line on key press
    def append_next_line(event=None):
        nonlocal current_line
        if current_line < len(lines):
            # Insert the next line into the text widget
            text_widget.insert(tk.END, lines[current_line])
            current_line += 1
            text_widget.see(tk.END)  # Scroll to the latest line

    # Create the root window
    root = tk.Tk()
    root.title("Fake Python IDE")

    # Create a text widget to display the file content
    text_widget = tk.Text(root, wrap=tk.NONE, font=("Courier", 12), bg="black", fg="white")
    text_widget.pack(fill=tk.BOTH, expand=1)

    # Initialize line counter
    current_line = 0

    # Bind any key press to the append_next_line function
    root.bind('<Key>', append_next_line)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == '__main__':
    # Replace 'your_python_file.py' with the file you want to display
    display_file_content('script.py')
