import json
import os
from task_manager.logger import setup_logger


TASKS_FILE = os.getenv("TASKS_FILE_PATH", "tasks.json")
logger = setup_logger()

def load_tasks():
    """Charge les tâches depuis le fichier JSON."""
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Sauvegarde la liste de tâches dans le fichier JSON."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
    logger.info("Tâches sauvegardées.")

def add_task(description, priority):
    """Ajoute une nouvelle tâche avec description et priorité."""
    tasks = load_tasks()
    task_id = (tasks[-1]["id"] + 1) if tasks else 1
    task = {
        "id": task_id,
        "description": description,
        "priority": priority
    }
    tasks.append(task)
    save_tasks(tasks)
    logger.info(f"Tâche ajoutée : {task}")
    return task

def list_tasks():
    """Retourne la liste des tâches."""
    tasks = load_tasks()
    logger.info("Liste des tâches récupérée.")
    return tasks

def delete_task(task_id):
    """Supprime la tâche dont l'ID est fourni."""
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        logger.warning(f"Aucune tâche trouvée avec l'ID {task_id}.")
        print(f"Aucune tâche trouvée avec l'ID {task_id}.")
    else:
        save_tasks(new_tasks)
        logger.info(f"Tâche supprimée avec l'ID {task_id}.")
        print(f"Tâche supprimée avec l'ID {task_id}.")
