import tkinter as tk
from tkinter import messagebox

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.employee import Employee
import services.file_service as file_service
import services.db_service as db_service


class EmployeeApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.mode = "file"

        # =========================
        # शीर्ष FRAME: INPUT AREA
        # =========================
        input_frame = tk.LabelFrame(root, text="Employee Details", padx=10, pady=10)
        input_frame.pack(fill="x", padx=10, pady=10)

        # Labels + Entries (grid layout)
        tk.Label(input_frame, text="Employee ID").grid(row=0, column=0, sticky="w")
        tk.Label(input_frame, text="Name").grid(row=1, column=0, sticky="w")
        tk.Label(input_frame, text="Position").grid(row=2, column=0, sticky="w")
        tk.Label(input_frame, text="Salary").grid(row=3, column=0, sticky="w")

        self.entry_id = tk.Entry(input_frame, width=30)
        self.entry_name = tk.Entry(input_frame, width=30)
        self.entry_position = tk.Entry(input_frame, width=30)
        self.entry_salary = tk.Entry(input_frame, width=30)

        self.entry_id.grid(row=0, column=1, padx=10, pady=5)
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)
        self.entry_position.grid(row=2, column=1, padx=10, pady=5)
        self.entry_salary.grid(row=3, column=1, padx=10, pady=5)

        # =========================
        # BUTTON FRAME
        # =========================
        btn_frame = tk.Frame(root)
        btn_frame.pack(fill="x", padx=10)

        tk.Button(btn_frame, text="Add Employee", bg="green", fg="white",
                  command=self.add_employee, width=20).pack(side="left", padx=5)

        tk.Button(btn_frame, text="Delete Employee", bg="red", fg="white",
                  command=self.delete_employee, width=20).pack(side="left", padx=5)

        tk.Button(btn_frame, text="Switch Mode", bg="blue", fg="white",
                  command=self.switch_mode, width=20).pack(side="left", padx=5)

        # =========================
        # LIST FRAME
        # =========================
        list_frame = tk.LabelFrame(root, text="Employees List", padx=10, pady=10)
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.listbox = tk.Listbox(list_frame, width=80, height=15)
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.refresh_list()

    # =========================
    # SERVICE SELECTION
    # =========================
    def get_service(self):
        return file_service if self.mode == "file" else db_service

    # =========================
    # ADD EMPLOYEE
    # =========================
    def add_employee(self):
        try:
            emp = Employee(
                self.entry_id.get().strip(),
                self.entry_name.get().strip(),
                self.entry_position.get().strip(),
                float(self.entry_salary.get())
            )

            if not emp.emp_id or not emp.name:
                raise ValueError("Empty fields")

            service = self.get_service()
            service.add_employee(emp)

            self.clear_inputs()
            self.refresh_list()

        except ValueError:
            messagebox.showerror("Error", "Invalid input! Check fields.")

    # =========================
    # DELETE EMPLOYEE
    # =========================
    def delete_employee(self):
        try:
            selected = self.listbox.get(self.listbox.curselection())
            emp_id = selected.split("|")[0].strip()

            service = self.get_service()
            service.delete_employee(emp_id)

            self.refresh_list()

        except:
            messagebox.showerror("Error", "Please select an employee!")

    # =========================
    # REFRESH LIST
    # =========================
    def refresh_list(self):
        self.listbox.delete(0, tk.END)

        service = self.get_service()
        employees = service.get_all_employees()

        for emp in employees:
            self.listbox.insert(tk.END, str(emp))

    # =========================
    # SWITCH MODE
    # =========================
    def switch_mode(self):
        self.mode = "db" if self.mode == "file" else "file"
        messagebox.showinfo("Mode", f"Switched to {self.mode.upper()} mode")
        self.refresh_list()

    # =========================
    # CLEAR INPUTS
    # =========================
    def clear_inputs(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_position.delete(0, tk.END)
        self.entry_salary.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()