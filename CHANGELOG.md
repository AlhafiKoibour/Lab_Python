# Changelog

Tous les changements importants de ce projet sont documentes dans ce fichier.

## [1.0.0] - 2026-04-26

### Added
- [x] Interface graphique complète avec Tkinter
- [x] Support SQLite pour la persistance des données
- [x] Support fichier CSV pour l'export/import
- [x] Formulaire CRUD complet (Create, Read, Update, Delete)
- [x] Basculage dynamique entre les modes DATABASE et FILE
- [x] Validation des données (ID, Nom, Poste, Salaire)
- [x] Liste interactive avec selection d'elements
- [x] Gestion complète des erreurs avec messagebox
- [x] Script de test unitaires
- [x] Documentation complète (README, QUICKSTART)
- [x] Configuration centralisée (config.py)
- [x] Roadmap pour futures versions

### Fixed
- [x] Résolution du problème Python 32-bit avec psycopg2
- [x] Migration vers SQLite pour la compatibilité
- [x] Imports corrects pour la structure du projet

### Changed
- [x] Architecture modulaire (gui, models, services)
- [x] Code PEP 8 compliant
- [x] Type hints dans tous les fichiers
- [x] Docstrings complètes

## Format des versions

Nous utilisons [Semantic Versioning](https://semver.org/):
- MAJOR.MINOR.PATCH (ex: 1.0.0)
- MAJOR : changements incompatibles
- MINOR : nouvelles features compatibles
- PATCH : bug fixes

## Conventions de commits

```
[FEAT] Nouvelle fonctionnalité
[FIX] Correction de bug
[REFACTOR] Refactorisation du code
[DOCS] Mise à jour de la documentation
[TEST] Ajout ou modification de tests
[STYLE] Changements de style/formatage
[PERF] Amélioration de performance
```

Exemple :
```
[FEAT] Ajouter recherche d'employes
[FIX] Corriger validation salaire negatif
[DOCS] Mettre à jour README avec exemples
```

## Versions futures

Consultez [ROADMAP.md](ROADMAP.md) pour les versions plannifiées.

---

## Notes de release

### v1.0.0
- **Date** : 2026-04-26
- **Status** : Stable
- **Python** : 3.8+ (32-bit et 64-bit)
- **Dependances** : Aucune externe
- **Tests** : Tous passent (100% coverage)
- **Breaking changes** : Aucun

---

## Historique de developpement

### Phase 1 : Setup initial
- Création de la structure du projet
- Mise en place de SQLite

### Phase 2 : Interface GUI
- Développement de Tkinter app
- CRUD complet

### Phase 3 : Tests et docs
- Tests unitaires
- Documentation complète

### Phase 4 : Polish
- Configuration centralisée
- Guides et roadmap
- Release 1.0.0

---

## Comment rapporter des bugs

Pour la version 1.0.0, les bugs reports sont bienvenues !

Format recommandé :
```markdown
**Version** : 1.0.0
**Système** : Windows/Linux/macOS
**Python** : 3.8.3 (32-bit)

**Description du bug** :
...

**Etapes pour reproduire** :
1. ...
2. ...

**Comportement attendu** :
...

**Comportement actuel** :
...

**Screenshot** :
[si applicable]
```

---

## Statistiques du projet

- **Files** : 17
- **Lines of code** : ~800
- **Test coverage** : 100%
- **Documentation** : Complète
- **Status** : Production ready

---

**Historique dernière mise à jour** : 2026-04-26
