# Guide de Contribution

Merci de votre interet pour contribuer a Employee Manager !

## Comment contribuer

### 1. Signaler un bug
- Ouvrir une issue avec le titre clair
- Inclure : description, etapes pour reproduire, version Python
- Joindre des captures d'ecran si pertinent

### 2. Proposer une feature
- Discuter d'abord dans une issue
- Decrire le cas d'usage et les benefices
- Consulter ROADMAP.md pour voir si deja planifie

### 3. Soumettre du code

#### Preparation
```bash
# Cloner le repo
git clone <repo>
cd Employee

# Creer une branche
git checkout -b feature/ma-feature
# ou
git checkout -b fix/mon-bug
```

#### Style de code
```python
# Suivre PEP 8
# Utiliser type hints
def add_employee_db(emp: Employee) -> None:
    """Ajouter un employe a la BD."""
    pass

# Nommer les variables clairement
MAX_RETRY_ATTEMPTS = 3
```

#### Tester votre code
```bash
# Lancer les tests
python test.py

# Lancer les tests specifiques
pytest test.py::test_db_service -v

# Verifier la couverture
pytest --cov=. test.py
```

#### Soumettre une PR
1. Committer avec messages clairs :
   ```
   git commit -m "Feat: ajouter recherche d'employes"
   git commit -m "Fix: correction bug validation salaire"
   ```

2. Pousser et ouvrir une Pull Request
3. Attendre la review et repondre aux commentaires

---

## Structure du projet

```
Employee/
├── main.py               # Point d'entree
├── config.py             # Configuration
├── test.py              # Tests
├── gui/                 # Interface
│   ├── __init__.py
│   └── app.py           # Classe principale EmployeeApp
├── models/              # Donnees
│   ├── __init__.py
│   └── employee.py      # Modele Employee
└── services/            # Logique metier
    ├── __init__.py
    ├── db_service.py    # SQLite
    └── file_service.py  # CSV
```

---

## Code patterns

### Ajouter une feature

**1. Modele (models/employee.py)**
```python
class Employee:
    def nouvelle_methode(self) -> str:
        """Description."""
        pass
```

**2. Service (services/db_service.py)**
```python
def nouvelle_fonction(emp: Employee) -> bool:
    """Faire quelque chose."""
    try:
        # Implementation
        return True
    except Exception as e:
        print(f"Erreur: {e}")
        return False
```

**3. GUI (gui/app.py)**
```python
def on_nouvel_bouton(self):
    """Callback du nouveau bouton."""
    try:
        # Valider inputs
        if not self.entry_id.get():
            messagebox.showwarning("Alerte", "Remplissez ID")
            return
        
        # Faire l'action
        # Rafraichir l'UI
        self.refresh_list()
    except Exception as e:
        messagebox.showerror("Erreur", str(e))
```

---

## Checklist avant PR

- [ ] Code suit PEP 8 (indentation, noms, etc)
- [ ] Tests passes : `python test.py`
- [ ] Pas de hardcoded values (utiliser config.py)
- [ ] Docstrings pour fonctions/classes
- [ ] Gestion d'erreurs completes
- [ ] Pas de fichiers inutiles
- [ ] Commit message clair
- [ ] Branche a jour avec main

---

## Commandes utiles

```bash
# Linter le code
flake8 .

# Formater le code
black .

# Tester syntaxe
python -m py_compile *.py

# Lancer l'app
python main.py

# Lancer tests complets
python test.py && pytest .
```

---

## Types de contributions bienvenues

### Code
- Bug fixes
- Features de la ROADMAP
- Optimisations
- Meilleure gestion d'erreurs

### Documentation
- Traduire README/QUICKSTART
- Ajouter exemples
- Clarifier sections confuses
- Documenter cas limites

### Tests
- Tests unitaires
- Tests d'integration
- Tests de stress
- Edge cases

### Design
- Icones
- Themes
- UX improvements
- Accessibilite

---

## Ressources

- **Python docs** : https://docs.python.org/3/
- **Tkinter guide** : https://docs.python.org/3/library/tkinter.html
- **SQLite** : https://www.sqlite.org/docs.html
- **PEP 8** : https://pep8.org/
- **Type hints** : https://docs.python.org/3/library/typing.html

---

## Questions ?

Ouvrir une issue ou contacter les mainteneurs.

**Merci d'avance !**
