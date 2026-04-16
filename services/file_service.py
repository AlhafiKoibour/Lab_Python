from models.employee import Employee

FILE_NAME = "employees.txt"


def add_employee(emp):
    try:
        with open(FILE_NAME, "a") as f:
            f.write(emp.to_string() + "\n")
    except Exception as e:
        print("File write error:", e)


def get_all_employees():
    employees = []
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                employees.append(Employee.from_string(line))
    except FileNotFoundError:
        pass
    return employees


def delete_employee(emp_id):
    employees = get_all_employees()
    employees = [e for e in employees if e.emp_id != emp_id]

    try:
        with open(FILE_NAME, "w") as f:
            for e in employees:
                f.write(e.to_string() + "\n")
    except Exception as e:
        print("File rewrite error:", e)