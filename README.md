# Gestion des Employés 👥

Application de gestion des employés avec interface graphique Python (Tkinter) et support de deux modes de stockage.

## 🎯 Fonctionnalités

- ✅ **Ajouter** un nouvel employé
- ✅ **Modifier** les informations d'un employé
- ✅ **Supprimer** un employé
- ✅ **Afficher** la liste complète des employés
- ✅ **Basculer** entre deux modes de stockage :
  - **Mode DATABASE** : SQLite (recommandé)
  - **Mode FICHIER** : Fichier texte CSV

## 🛠️ Installation

### Prérequis
- Python 3.8+
- Tkinter (inclus avec Python sur Windows et macOS)

### Étapes d'installation

1. **Cloner ou télécharger le projet**
```bash
cd Employee
```

2. **Aucune dépendance externe requise** (Tkinter et SQLite sont inclus)

## 🚀 Utilisation

### Lancer l'application
```bash
python main.py
```

### Interface utilisateur

1. **Formulaire d'ajout/modification**
   - Remplissez tous les champs (ID, Nom, Poste, Salaire)
   - Cliquez sur "Ajouter" pour ajouter un nouvel employé
   - Sélectionnez un employé dans la liste et cliquez "Modifier" pour le mettre à jour
   - Cliquez "Supprimer" pour supprimer l'employé sélectionné

2. **Basculer entre les modes**
   - Cliquez sur le bouton "Mode: DATABASE" / "Mode: FICHIER" pour changer de mode
   - Le changement est immédiat et recharge la liste

## 📁 Structure du projet

```
Employee/
├── main.py                 # Point d'entrée de l'application
├── gui/
│   ├── __init__.py
│   └── app.py             # Interface graphique (Tkinter)
├── models/
│   ├── __init__.py
│   └── employee.py        # Modèle de données Employee
├── services/
│   ├── __init__.py
│   ├── db_service.py      # Service de base de données (SQLite)
│   └── file_service.py    # Service fichier (CSV)
└── README.md              # Documentation
```

## 🗄️ Modes de stockage

### Mode DATABASE (SQLite)
- Stockage dans `employees.db`
- Plus rapide et fiable
- Supporte les opérations CRUD complètes
- **Recommandé pour une utilisation en production**

### Mode FICHIER
- Stockage dans `employees.txt`
- Format simple CSV
- Facile à lire/modifier manuellement
- Parfait pour prototypage rapide

## 📋 Format des données (Mode FICHIER)

Chaque ligne du fichier `employees.txt` suit ce format :
```
ID,Nom,Poste,Salaire
E001,Alice Dupont,Developer,3500.0
E002,Bob Martin,Manager,4500.0
```

## 🐛 Gestion des erreurs

L'application gère automatiquement :
- ✅ Champs manquants
- ✅ Salaires invalides (non-numériques)
- ✅ IDs dupliqués
- ✅ Fichiers/DB inaccessibles

## 💡 Exemples d'utilisation

### Ajouter un employé
1. Remplissez le formulaire avec : E001, Alice Dupont, Developer, 3500
2. Cliquez "Ajouter"
3. L'employé apparaît dans la liste

### Modifier un employé
1. Cliquez sur l'employé dans la liste
2. Les champs se remplissent automatiquement
3. Modifiez les informations
4. Cliquez "Modifier"

### Supprimer un employé
1. Cliquez sur l'employé dans la liste
2. Cliquez "Supprimer"
3. Confirmez la suppression

## ⚙️ Configuration

### Modifier le chemin de la base de données
Éditez `services/db_service.py` :
```python
DB_PATH = "chemin/vers/ma/database.db"
```

### Modifier le fichier d'employés
Éditez `services/file_service.py` :
```python
FILE_NAME = "chemin/vers/mon/fichier.txt"
```

## 🔒 Validations

- **ID** : Ne peut pas être vide, doit être unique
- **Nom** : Ne peut pas être vide
- **Poste** : Ne peut pas être vide
- **Salaire** : Doit être un nombre positif

## 📝 Licence

Ce projet est fourni sans restrictions de licence.

## 🤝 Support

Pour des problèmes ou suggestions, vous pouvez :
- Vérifier la console pour les messages d'erreur détaillés
- Consulter les logs du fichier d'erreur (si implémenté)
- Réinitialiser le formulaire avec le bouton "Réinitialiser"
