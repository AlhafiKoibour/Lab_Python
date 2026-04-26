import tkinter as tk
from tkinter import messagebox
from services.file_service import add_employee, get_all_employees, update_employee, delete_employee
from services.db_service import add_employee_db, get_all_employees_db, init_db, delete_employee_db, update_employee_db
from models.employee import Employee

class EmployeeApp:
    def __init__(self, root):
        init_db()
        
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("780x560")
        self.root.resizable(False, False)
        self.mode = "DB"
        self.selected_employee = None
        self.search_text = tk.StringVar()
        
        # --- Employee Details ---
        details_frame = tk.LabelFrame(root, text="Employee Details", padx=12, pady=12, font=("Arial", 10, "bold"))
        details_frame.place(x=12, y=12, width=756, height=180)
        
        tk.Label(details_frame, text="Employee ID", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=4)
        self.entry_id = tk.Entry(details_frame, width=40, font=("Arial", 10))
        self.entry_id.grid(row=0, column=1, pady=4, padx=8)
        
        tk.Label(details_frame, text="Name", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=4)
        self.entry_name = tk.Entry(details_frame, width=40, font=("Arial", 10))
        self.entry_name.grid(row=1, column=1, pady=4, padx=8)
        
        tk.Label(details_frame, text="Position", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=4)
        self.entry_position = tk.Entry(details_frame, width=40, font=("Arial", 10))
        self.entry_position.grid(row=2, column=1, pady=4, padx=8)
        
        tk.Label(details_frame, text="Salary", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=4)
        self.entry_salary = tk.Entry(details_frame, width=40, font=("Arial", 10))
        self.entry_salary.grid(row=3, column=1, pady=4, padx=8)
        
        # --- Buttons ---
        buttons_frame = tk.Frame(root)
        buttons_frame.place(x=12, y=210, width=756, height=60)
        
        self.btn_add = tk.Button(buttons_frame, text="Add Employee", bg="#008000", fg="white", font=("Arial", 10, "bold"), width=16, command=self.add_employee)
        self.btn_add.pack(side="left", padx=4)
        
        self.btn_modify = tk.Button(buttons_frame, text="Modify Employee", bg="#ffa500", fg="white", font=("Arial", 10, "bold"), width=16, command=self.update_employee)
        self.btn_modify.pack(side="left", padx=4)
        
        self.btn_delete = tk.Button(buttons_frame, text="Delete Employee", bg="#d60000", fg="white", font=("Arial", 10, "bold"), width=16, command=self.delete_employee)
        self.btn_delete.pack(side="left", padx=4)
        
        self.btn_switch = tk.Button(buttons_frame, text="Switch Mode", bg="#0028ff", fg="white", font=("Arial", 10, "bold"), width=16, command=self.toggle_mode)
        self.btn_switch.pack(side="left", padx=4)
        
        # --- Search ---
        search_frame = tk.Frame(root)
        search_frame.place(x=12, y=280, width=756, height=34)
        
        tk.Label(search_frame, text="Search by Name:", font=("Arial", 10)).pack(side="left", padx=(0, 8))
        self.entry_search = tk.Entry(search_frame, textvariable=self.search_text, width=30, font=("Arial", 10))
        self.entry_search.pack(side="left")
        
        self.btn_search = tk.Button(search_frame, text="Search", bg="#444444", fg="white", font=("Arial", 10, "bold"), width=10, command=self.search_employee)
        self.btn_search.pack(side="left", padx=8)
        
        self.btn_reset = tk.Button(search_frame, text="Reset", bg="#666666", fg="white", font=("Arial", 10, "bold"), width=10, command=self.reset_search)
        self.btn_reset.pack(side="left")
        
        # --- Employees List ---
        list_label = tk.Label(root, text="Employees List", font=("Arial", 10, "bold"))
        list_label.place(x=12, y=320)
        
        list_frame = tk.Frame(root, bd=2, relief="sunken")
        list_frame.place(x=12, y=340, width=756, height=200)
        
        self.listbox = tk.Listbox(list_frame, font=("Arial", 10), activestyle="none")
        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)
        
        self.scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.refresh_list()
    
    def toggle_mode(self):
        self.mode = "FILE" if self.mode == "DB" else "DB"
        self.search_text.set("")
        self.refresh_list()
    
    def add_employee(self):
        emp_id = self.entry_id.get().strip()
        name = self.entry_name.get().strip()
        position = self.entry_position.get().strip()
        salary_str = self.entry_salary.get().strip()
        
        if not all([emp_id, name, position, salary_str]):
            messagebox.showwarning("Validation", "Tous les champs sont obligatoires!")
            return
        try:
            salary = float(salary_str)
        except ValueError:
            messagebox.showerror("Erreur", "Le salaire doit être un nombre!")
            return
        
        try:
            emp = Employee(emp_id, name, position, salary)
            if self.mode == "DB":
                add_employee_db(emp)
            else:
                add_employee(emp)
            self.clear_form()
            self.refresh_list()
            messagebox.showinfo("Succès", "Employé ajouté avec succès!")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'ajout : {e}")
        finally:
            self.root.update_idletasks()
    
    def update_employee(self):
        if self.selected_employee is None:
            messagebox.showwarning("Sélection", "Veuillez sélectionner un employé à modifier!")
            return
        emp_id = self.entry_id.get().strip()
        name = self.entry_name.get().strip()
        position = self.entry_position.get().strip()
        salary_str = self.entry_salary.get().strip()
        
        if not all([emp_id, name, position, salary_str]):
            messagebox.showwarning("Validation", "Tous les champs sont obligatoires!")
            return
        try:
            salary = float(salary_str)
        except ValueError:
            messagebox.showerror("Erreur", "Le salaire doit être un nombre!")
            return
        
        try:
            emp = Employee(emp_id, name, position, salary)
            if self.mode == "DB":
                update_employee_db(emp)
            else:
                update_employee(emp)
            self.clear_form()
            self.refresh_list()
            messagebox.showinfo("Succès", "Employé modifié avec succès!")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la modification : {e}")
        finally:
            self.root.update_idletasks()
    
    def delete_employee(self):
        emp_id = self.entry_id.get().strip()
        if not emp_id:
            messagebox.showwarning("Sélection", "Veuillez sélectionner un employé à supprimer!")
            return
        if not messagebox.askyesno("Confirmation", f"Supprimer l'employé {emp_id} ?"):
            return
        try:
            if self.mode == "DB":
                delete_employee_db(emp_id)
            else:
                delete_employee(emp_id)
            self.clear_form()
            self.refresh_list()
            messagebox.showinfo("Succès", "Employé supprimé avec succès!")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la suppression : {e}")
        finally:
            self.root.update_idletasks()
    
    def search_employee(self):
        self.refresh_list()
    
    def reset_search(self):
        self.search_text.set("")
        self.refresh_list()
    
    def on_select(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return
        index = selection[0]
        value = self.listbox.get(index)
        if not value:
            return
        parts = value.split(" | ")
        if len(parts) < 4:
            return
        self.selected_employee = parts[0]
        self.entry_id.delete(0, tk.END)
        self.entry_id.insert(0, parts[0])
        self.entry_name.delete(0, tk.END)
        self.entry_name.insert(0, parts[1])
        self.entry_position.delete(0, tk.END)
        self.entry_position.insert(0, parts[2])
        self.entry_salary.delete(0, tk.END)
        self.entry_salary.insert(0, parts[3])
    
    def clear_form(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_position.delete(0, tk.END)
        self.entry_salary.delete(0, tk.END)
        self.selected_employee = None
    
    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        try:
            employees = get_all_employees_db() if self.mode == "DB" else get_all_employees()
            query = self.search_text.get().strip().lower()
            if query:
                employees = [emp for emp in employees if query in emp.name.lower()]
            for emp in employees:
                self.listbox.insert(tk.END, f"{emp.emp_id} | {emp.name} | {emp.position} | {emp.salary:.2f}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement : {e}")
        finally:
            self.root.update_idletasks()

