import os
from models.employee import Employee

FILE_NAME = "employees.txt"

def add_employee(emp: Employee):
    """Ajouter un employé dans le fichier"""
    try:
        with open(FILE_NAME, "a", encoding="utf-8") as f:
            f.write(emp.to_string() + "\n")
    except Exception as e:
        print(f"Erreur d'écriture : {e}")

def get_all_employees():
    """Lire tous les employés du fichier"""
    employees = []
    if not os.path.exists(FILE_NAME):
        return employees
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                emp = Employee.from_string(line)
                if emp:
                    employees.append(emp)
    except Exception as e:
        print(f"Erreur de lecture : {e}")
    return employees

def update_employee(emp: Employee):
    """Mettre à jour un employé dans le fichier"""
    try:
        employees = get_all_employees()
        updated = False
        
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for e in employees:
                if e.emp_id == emp.emp_id:
                    f.write(emp.to_string() + "\n")
                    updated = True
                else:
                    f.write(e.to_string() + "\n")
        
        if not updated:
            print(f"Aucun employé trouvé avec l'ID {emp.emp_id}")
    except Exception as e:
        print(f"Erreur lors de la modification : {e}")

def delete_employee(emp_id: str):
    """Supprimer un employé du fichier"""
    try:
        employees = get_all_employees()
        deleted = False
        
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for e in employees:
                if e.emp_id != emp_id:
                    f.write(e.to_string() + "\n")
                else:
                    deleted = True
        
        if not deleted:
            print(f"Aucun employé trouvé avec l'ID {emp_id}")
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")