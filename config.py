"""
Configuration de l'application Employee
Modifiez ce fichier pour personnaliser l'application
"""

# ===== DATABASE =====
# Chemin vers la base de donnees SQLite
DATABASE_PATH = "employees.db"

# ===== FICHIER =====
# Chemin vers le fichier CSV des employes
FILE_PATH = "employees.txt"

# ===== INTERFACE GRAPHIQUE =====
# Configuration de la fenetre principale
WINDOW_TITLE = "Gestion des Employes"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650

# Theme et couleurs
THEME_COLORS = {
    "primary": "#0078d4",      # Bleu
    "success": "#107c10",       # Vert
    "danger": "#d83b01",        # Rouge
    "warning": "#ffb900",       # Orange
    "background": "#f3f3f3",    # Gris clair
}

# Police par defaut
FONT_FAMILY = "Arial"
FONT_SIZE_NORMAL = 10
FONT_SIZE_TITLE = 16

# ===== COMPORTEMENT =====
# Mode par defaut (DATABASE ou FILE)
DEFAULT_MODE = "DATABASE"

# Afficher les confirmations avant suppression
CONFIRM_DELETE = True

# Nombre maximum d'employes a afficher
MAX_EMPLOYEES_DISPLAY = 1000

# ===== VALIDATION =====
# Longueur minimale/maximale pour les champs
MIN_ID_LENGTH = 1
MAX_ID_LENGTH = 50
MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 100
MIN_SALARY = 0.0
MAX_SALARY = 9999999.99

# ===== LOGGING =====
# Niveau de log (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL = "INFO"
LOG_FILE = "employee_app.log"
