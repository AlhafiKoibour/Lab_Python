import sqlite3
from models.employee import Employee

DB_PATH = "employees.db"

def init_db():
    """Initialise la base de données SQLite"""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    emp_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    position TEXT NOT NULL,
                    salary REAL NOT NULL
                )
            """)
            conn.commit()
    except Exception as e:
        print(f"Erreur Database (Initialisation) : {e}")

def get_connection():
    return sqlite3.connect(DB_PATH)

def add_employee_db(emp: Employee):
    query = "INSERT OR IGNORE INTO employees (emp_id, name, position, salary) VALUES (?, ?, ?, ?)"
    try:
        with get_connection() as conn:
            conn.execute(query, (emp.emp_id, emp.name, emp.position, emp.salary))
            conn.commit()
    except Exception as e:
        print(f"Erreur Database (Insertion) : {e}")

def get_all_employees_db():
    employees = []
    try:
        with get_connection() as conn:
            cursor = conn.execute("SELECT emp_id, name, position, salary FROM employees ORDER BY emp_id")
            for row in cursor.fetchall():
                employees.append(Employee(*row))
    except Exception as e:
        print(f"Erreur Database (Lecture) : {e}")
    return employees

def update_employee_db(emp: Employee):
    """Modifier un employé existant"""
    query = "UPDATE employees SET name = ?, position = ?, salary = ? WHERE emp_id = ?"
    try:
        with get_connection() as conn:
            cursor = conn.execute(query, (emp.name, emp.position, emp.salary, emp.emp_id))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"Aucun employé trouvé avec l'ID {emp.emp_id}")
    except Exception as e:
        print(f"Erreur Database (Modification) : {e}")

def delete_employee_db(emp_id: str):
    """Supprimer un employé"""
    query = "DELETE FROM employees WHERE emp_id = ?"
    try:
        with get_connection() as conn:
            cursor = conn.execute(query, (emp_id,))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"Aucun employé trouvé avec l'ID {emp_id}")
    except Exception as e:
        print(f"Erreur Database (Suppression) : {e}")