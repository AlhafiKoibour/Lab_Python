# Architecture - Employee Manager

Vue d'ensemble de l'architecture de l'application.

## Diagramme d'architecture

```
┌─────────────────────────────────────────────────────────┐
│                   INTERFACE UTILISATEUR                 │
│                   (Tkinter GUI - gui/app.py)            │
│  ┌──────────────────────────────────────────────────┐   │
│  │ - Formulaire (ID, Nom, Poste, Salaire)          │   │
│  │ - Liste des employes (TreeView)                 │   │
│  │ - Boutons (Ajouter, Modifier, Supprimer, etc)   │   │
│  │ - Bouton basculage MODE (DATABASE ↔ FILE)       │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                     COUCHE METIER                        │
│           (Services - services/*.py)                    │
│  ┌──────────────────────┐    ┌──────────────────────┐   │
│  │  db_service.py       │    │ file_service.py      │   │
│  │ (SQLite)             │    │ (CSV)                │   │
│  │ - add_employee_db    │    │ - add_employee       │   │
│  │ - get_all_employees_db│  │ - get_all_employees  │   │
│  │ - update_employee_db │    │ - update_employee    │   │
│  │ - delete_employee_db │    │ - delete_employee    │   │
│  └──────────────────────┘    └──────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                   COUCHE DONNEES                         │
│              (Models - models/*.py)                     │
│  ┌──────────────────────────────────────────────────┐   │
│  │ Employee                                         │   │
│  │ - emp_id: str                                    │   │
│  │ - name: str                                      │   │
│  │ - position: str                                  │   │
│  │ - salary: float                                  │   │
│  │ Methods:                                         │   │
│  │ - validate()                                     │   │
│  │ - to_string() / from_string()                    │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                   STOCKAGE PERSISTANT                    │
│              (SQLite ou CSV)                            │
│  ┌──────────────────────┐    ┌──────────────────────┐   │
│  │ employees.db         │    │ employees.txt        │   │
│  │ (SQLite database)    │    │ (CSV file)           │   │
│  │                      │    │                      │   │
│  │ Table:               │    │ Format:              │   │
│  │ CREATE TABLE         │    │ ID,Nom,Poste,Salaire │   │
│  │ employees (          │    │ E001,Alice,Dev,3500  │   │
│  │   emp_id TEXT,       │    │ E002,Bob,Mgr,4500    │   │
│  │   name TEXT,         │    │                      │   │
│  │   position TEXT,     │    │                      │   │
│  │   salary REAL        │    │                      │   │
│  │ )                    │    │                      │   │
│  └──────────────────────┘    └──────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## Flux de donnees

### Ajouter un employe

```
Utilisateur
   ↓ (remplit formulaire)
GUI (gui/app.py - add_employee)
   ↓ (valide, crée Employee)
Service (db_service.py ou file_service.py)
   ↓ (insère dans BD/fichier)
Base de donnees (employees.db ou employees.txt)
   ↓ (retour succes)
GUI (rafraichit la liste)
```

### Modifier un employe

```
Utilisateur (clique sur employe dans liste)
   ↓
GUI (on_select event)
   ↓ (rempli le formulaire)
Formulaire
   ↓ (utilisateur modifie + clique "Modifier")
GUI (update_employee)
   ↓ (valide, crée Employee)
Service (update_employee_db ou update_employee)
   ↓ (met à jour)
Base de donnees
   ↓
GUI (rafraichit la liste)
```

## Dependances entre modules

```
main.py
  └── gui/app.py
       ├── models/employee.py
       ├── services/db_service.py
       │    └── models/employee.py
       └── services/file_service.py
            └── models/employee.py

test.py
  ├── models/employee.py
  ├── services/db_service.py
  └── services/file_service.py
```

## Patterns de code

### Service Pattern
```python
# Service expose interface consistante
def add_employee_db(emp: Employee) -> None
def get_all_employees_db() -> List[Employee]
def update_employee_db(emp: Employee) -> None
def delete_employee_db(emp_id: str) -> None
```

### Model Pattern
```python
# Model encapsule les donnees et validations
class Employee:
    def __init__(self, emp_id, name, position, salary)
    def validate(self)
    def to_string(self) -> str
```

### GUI Pattern (Tkinter)
```python
# Separer logique et presentation
class EmployeeApp:
    def __init__(self, root)
    def on_select(event)      # Selection
    def add_employee(self)     # Action
    def refresh_list(self)     # UI update
```

## Modes de stockage

### Mode DATABASE (Recommande)

**Avantages:**
- SQL queries performantes
- ACID compliant
- Multi-utilisateurs (futur)
- Pas de parsing manuel
- Transactions

**Inconvenients:**
- Moins lisible sans outils
- Depend de SQLite

**Fichiers:**
- `employees.db` : Base de donnees SQLite
- `services/db_service.py` : Implementation

### Mode FILE (CSV)

**Avantages:**
- Editable manuellement
- Portable
- Pas de dependances
- Facile a debugger

**Inconvenients:**
- Plus lent avec beaucoup de donnees
- Pas de transactions
- Parsing manuel

**Fichiers:**
- `employees.txt` : Fichier CSV
- `services/file_service.py` : Implementation

## Configuration

```python
# config.py centralise les parametres
DATABASE_PATH = "employees.db"
FILE_PATH = "employees.txt"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
DEFAULT_MODE = "DATABASE"
```

## Gestion des erreurs

```
Tous les services (db_service.py, file_service.py):
try:
    # operation
except Exception as e:
    print(f"Erreur: {e}")  # Log
    # GUI affiche messagebox.showerror()
```

## Structure des fichiers

```
Employee/
├── main.py                 # Entry point
├── config.py              # Configuration globale
├── project.json           # Metadata
├── test.py               # Tests
│
├── gui/                  # Interface utilisateur
│   ├── __init__.py
│   └── app.py           # EmployeeApp class
│
├── models/              # Modeles de donnees
│   ├── __init__.py
│   └── employee.py      # Employee class
│
├── services/            # Logique metier
│   ├── __init__.py
│   ├── db_service.py    # Database operations
│   └── file_service.py  # File operations
│
├── Documentation/
│   ├── README.md        # Documentation complète
│   ├── QUICKSTART.md    # Demarrage rapide
│   ├── CONTRIBUTING.md  # Guide contribution
│   ├── ROADMAP.md       # Futures versions
│   ├── CHANGELOG.md     # Historique
│   └── ARCHITECTURE.md  # Ce fichier
│
└── Generated/
    ├── employees.db     # SQLite database
    └── employees.txt    # CSV file
```

## Performance

### Complexité temps (O)

| Operation | Mode DB | Mode FILE |
|-----------|---------|-----------|
| Add       | O(1)    | O(n)      |
| Read all  | O(n)    | O(n)      |
| Update    | O(1)    | O(n)      |
| Delete    | O(1)    | O(n)      |
| Search    | O(log n)| O(n)      |

### Memoire

- In-memory : ~100 bytes par Employee
- DB overhead : Minimal (SQLite optimisé)
- GUI memory : ~5 MB pour 1000 employes

## Securite

### Validation

```python
# input validation
- Longueur min/max (config.py)
- Type checking
- Salaire positif
- ID unique (DB only)
```

### Donnees sensibles

```python
# Pas de donnees sensibles actuellement
# TODO v2.0: Hacher les mots de passe
# TODO v2.0: Chiffrer les salaires
```

## Extension future

### Pour ajouter une feature

1. Ajouter modele si necessaire (models/*.py)
2. Ajouter service (db_service.py + file_service.py)
3. Ajouter UI (gui/app.py)
4. Ajouter tests (test.py)
5. Ajouter docs

### Exemple : Ajouter departement

```python
# 1. Model
class Employee:
    department: str  # Nouveau champ

# 2. Service
def add_employee_db(emp: Employee):
    # INSERT avec department

# 3. GUI
ttk.Label(form_frame, text="Departement")
self.entry_department = ttk.Entry(form_frame)
```

---

**Dernière mise à jour** : 2026-04-26
