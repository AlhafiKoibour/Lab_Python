# Demarrage Rapide - Employee Manager

## 5 minutes pour commencer

### 1. Lancer l'application
```bash
python main.py
```

### 2. Remplir le formulaire
Entrez les informations d'un employe :
- **ID** : E001 (identifiant unique)
- **Nom** : Alice Dupont
- **Poste** : Developer
- **Salaire** : 3500

### 3. Cliquer "Ajouter"
L'employe apparait dans la liste

### 4. Interagir avec les donnees

#### Modifier
1. Cliquez sur l'employe dans la liste
2. Les champs se remplissent
3. Modifiez les informations
4. Cliquez "Modifier"

#### Supprimer
1. Cliquez sur l'employe
2. Cliquez "Supprimer"
3. Confirmez

#### Changer de mode
Cliquez "Mode: DATABASE" pour basculer entre :
- **DATABASE** : SQLite (rapide, recommande)
- **FICHIER** : CSV (lisible, portable)

---

## Problemes courants

### "Champs obligatoires"
Assurez-vous que tous les champs sont remplis avant d'ajouter

### "Le salaire doit etre un nombre"
Entrez un nombre valide (ex: 3500.50)

### "Aucun employe a modifier"
Selectionnez un employe dans la liste avant de modifier

---

## Structure des fichiers

```
Employee/
├── main.py                 # Lancer depuis ici
├── config.py               # Parametres (optionnel)
├── requirements.txt        # Dependances (aucune!)
├── README.md              # Documentation complete
├── test.py                # Tests unitaires
│
├── gui/
│   └── app.py             # Interface graphique
├── models/
│   └── employee.py        # Modele de donnees
└── services/
    ├── db_service.py      # SQLite (RECOMMANDE)
    └── file_service.py    # CSV
```

---

## Fichiers generes automatiquement

```
Employee/
├── employees.db           # Base de donnees SQLite (si mode DATABASE)
└── employees.txt          # Fichier CSV (si mode FICHIER)
```

---

## Raccourcis clavier (futur)

- `Ctrl+N` : Nouvel employe
- `Ctrl+S` : Sauvegarder
- `Ctrl+D` : Supprimer selection
- `Ctrl+Q` : Quitter

---

## Modes de stockage

| Feature | DATABASE (SQLite) | FICHIER (CSV) |
|---------|------------------|---------------|
| Vitesse | Tres rapide      | Rapide        |
| Fiabilite | Excellente     | Bonne         |
| Portable | Bon             | Excellent     |
| Editable manuellement | Non | Oui |
| Recommande | OUI | Non |

---

## Parametrage avance

Modifiez `config.py` pour :
- Changer les couleurs
- Modifier les limites de validation
- Configurer le logging
- Changer le chemin des donnees

---

## Aide & Support

1. Lancer les tests : `python test.py`
2. Consulter README.md pour la documentation complete
3. Verifier que Python 3.8+ est installe
4. S'assurer que Tkinter est disponible (inclus par defaut)

---

**Bon usage!**
