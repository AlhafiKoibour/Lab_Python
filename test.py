#!/usr/bin/env python3
"""
Script de test pour l'application de gestion des employés
Teste toutes les fonctionnalités sans lancer la GUI
"""

import sys
sys.path.insert(0, ".")

from models.employee import Employee
from services.db_service import (
    init_db, add_employee_db, get_all_employees_db,
    update_employee_db, delete_employee_db
)
from services.file_service import (
    add_employee, get_all_employees, update_employee, delete_employee
)

def test_employee_model():
    """Tester le modele Employee"""
    print("\n[TEST] Modele Employee")
    try:
        emp = Employee("E001", "Alice Dupont", "Developer", 3500)
        print(f"  [OK] Cree: {emp}")
        
        # Test validation
        try:
            bad_emp = Employee("", "Bob", "Dev", 2000)
            print("  [ECHEC] La validation aurait du rejeter l'ID vide")
        except ValueError:
            print("  [OK] Validation ID fonctionnelle")
        
        # Test from_string
        emp2 = Employee.from_string("E002,Charlie Brown,Manager,4000")
        if emp2 and emp2.emp_id == "E002":
            print("  [OK] from_string fonctionne")
    except Exception as e:
        print(f"  [ECHEC] {e}")

def test_db_service():
    """Tester le service database"""
    print("\n[TEST] Service Database (SQLite)")
    try:
        # Initialiser
        init_db()
        print("  [OK] Base de donnees initialisee")
        
        # Ajouter
        emp1 = Employee("DB001", "Test User", "Developer", 3000)
        add_employee_db(emp1)
        print("  [OK] Employee ajoute")
        
        # Lire
        employees = get_all_employees_db()
        if len(employees) > 0:
            print(f"  [OK] {len(employees)} employee(s) lus")
        
        # Modifier
        emp1_mod = Employee("DB001", "Test User Modified", "Senior Dev", 4000)
        update_employee_db(emp1_mod)
        print("  [OK] Employee modifie")
        
        # Verifier modification
        employees = get_all_employees_db()
        for e in employees:
            if e.emp_id == "DB001" and e.position == "Senior Dev":
                print("  [OK] Modification verifiee")
                break
        
        # Supprimer
        delete_employee_db("DB001")
        print("  [OK] Employee supprime")
        
    except Exception as e:
        print(f"  [ECHEC] {e}")

def test_file_service():
    """Tester le service fichier"""
    print("\n[TEST] Service Fichier (CSV)")
    try:
        # Ajouter
        emp1 = Employee("FILE001", "File User", "Analyst", 2800)
        add_employee(emp1)
        print("  [OK] Employee ajoute au fichier")
        
        # Lire
        employees = get_all_employees()
        if len(employees) > 0:
            print(f"  [OK] {len(employees)} employee(s) lus depuis fichier")
        
        # Modifier
        emp1_mod = Employee("FILE001", "File User Modified", "Senior Analyst", 3500)
        update_employee(emp1_mod)
        print("  [OK] Employee modifie dans fichier")
        
        # Supprimer
        delete_employee("FILE001")
        print("  [OK] Employee supprime du fichier")
        
    except Exception as e:
        print(f"  [ECHEC] {e}")

def test_validation():
    """Tester les validations"""
    print("\n[TEST] Validations")
    errors = []
    
    # Test salaire negatif
    try:
        emp = Employee("E001", "Test", "Dev", -1000)
        errors.append("Salaire negatif accepte")
    except ValueError:
        print("  [OK] Salaire negatif rejete")
    
    # Test nom vide
    try:
        emp = Employee("E001", "", "Dev", 1000)
        errors.append("Nom vide accepte")
    except ValueError:
        print("  [OK] Nom vide rejete")
    
    # Test poste vide
    try:
        emp = Employee("E001", "Test", "", 1000)
        errors.append("Poste vide accepte")
    except ValueError:
        print("  [OK] Poste vide rejete")
    
    if errors:
        print(f"  [ECHEC] {len(errors)} validation(s) manquante(s)")
    else:
        print("  [OK] Toutes les validations OK")

if __name__ == "__main__":
    print("=" * 50)
    print("Tests de l'Application Employee")
    print("=" * 50)
    
    test_employee_model()
    test_db_service()
    test_file_service()
    test_validation()
    
    print("\n" + "=" * 50)
    print("Tests termines")
    print("=" * 50)
