class Employee:
    def __init__(self, emp_id: str, name: str, position: str, salary: float):
        self.emp_id = emp_id.strip()
        self.name = name.strip()
        self.position = position.strip()
        self.salary = float(salary)
        self.validate()
    
    def validate(self):
        """Valider les données de l'employé"""
        if not self.emp_id:
            raise ValueError("L'ID de l'employé ne peut pas être vide")
        if not self.name:
            raise ValueError("Le nom ne peut pas être vide")
        if not self.position:
            raise ValueError("Le poste ne peut pas être vide")
        if self.salary < 0:
            raise ValueError("Le salaire ne peut pas être négatif")
    
    def to_string(self) -> str:
        """Convertit l'objet en ligne CSV pour le fichier texte."""
        return f"{self.emp_id},{self.name},{self.position},{self.salary}"
    
    def __str__(self) -> str:
        """Représentation lisible de l'employé"""
        return f"Employee(ID={self.emp_id}, Nom={self.name}, Poste={self.position}, Salaire={self.salary:.2f}€)"
    
    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def from_string(data: str):
        """Crée un objet Employee à partir d'une ligne de texte."""
        try:
            parts = data.strip().split(",")
            if len(parts) == 4:
                return Employee(parts[0], parts[1], parts[2], float(parts[3]))
        except (ValueError, IndexError):
            pass
        return None