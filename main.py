import tkinter as tk
from gui.app import EmployeeApp

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()