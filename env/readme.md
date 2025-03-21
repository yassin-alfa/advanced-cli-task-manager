# Advanced CLI Task Manager

## Introduction
Ce projet est un outil en ligne de commande permettant de gérer des tâches (ajout, liste, suppression) via un fichier JSON, avec journalisation et tests unitaires.

## Installation
1. **Cloner le dépôt**  
```bash
git clone <URL_DU_DEPOT>
cd advanced_cli_task_manager
```

2. **Créer et activer un environnement virtuel**  
```bash
python -m venv env
```
- Sur Windows (PowerShell) :
```powershell
.\env\Scripts\Activate.ps1
```
- Sur macOS/Linux :
```bash
source env/bin/activate
```

3. **Installer les dépendances** (si un fichier `requirements.txt` est fourni) :
```bash
pip install -r requirements.txt
```

4. **Vérifier le fichier de tâches**  
Assure-toi que le fichier `tasks.json` existe à la racine et contient :
```json
[]
```

## Utilisation
Les commandes principales sont :

- **Ajouter une tâche**  
```bash
python -m task_manager.cli add "Ma nouvelle tâche" -p 2
```

- **Lister les tâches**  
```bash
python -m task_manager.cli list
```

- **Supprimer une tâche**  
```bash
python -m task_manager.cli delete 1
```

## Tests Unitaires
Pour lancer les tests unitaires, exécutez la commande suivante à la racine du projet :
```bash
python -m unittest discover tests
```
Les tests vérifieront le bon fonctionnement des fonctions d'ajout et de suppression de tâches.
