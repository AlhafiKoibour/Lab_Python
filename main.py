import tkinter as tk
from gui.app import EmployeeApp

def main():
    """Point d'entrée principal de l'application"""
    root = tk.Tk()
    root.title("Gestion des Employés")
    root.geometry("800x650")
    root.resizable(True, True)
    
    # Initialiser l'application
    app = EmployeeApp(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()