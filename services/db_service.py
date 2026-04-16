import psycopg2
from models.employee import Employee
from config import DB_CONFIG


def connect():
    return psycopg2.connect(**DB_CONFIG)


def add_employee(emp):
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO employees VALUES (%s, %s, %s, %s)",
            (emp.emp_id, emp.name, emp.position, emp.salary)
        )

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print("DB insert error:", e)


def get_all_employees():
    employees = []
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()

        for r in rows:
            employees.append(Employee(*r))

        cur.close()
        conn.close()

    except Exception as e:
        print("DB fetch error:", e)

    return employees


def delete_employee(emp_id):
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("DELETE FROM employees WHERE emp_id = %s", (emp_id,))
        conn.commit()

        cur.close()
        conn.close()

    except Exception as e:
        print("DB delete error:", e)