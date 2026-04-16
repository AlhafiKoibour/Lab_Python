class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} | {self.name} | {self.position} | {self.salary}"

    def to_string(self):
        return f"{self.emp_id},{self.name},{self.position},{self.salary}"

    @staticmethod
    def from_string(data):
        emp_id, name, position, salary = data.strip().split(",")
        return Employee(emp_id, name, position, float(salary))