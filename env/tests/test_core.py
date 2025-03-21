import os
import json
import unittest
from task_manager.core import add_task, load_tasks, delete_task

# Fichier de test pour isoler les données
TEST_TASKS_FILE = "test_tasks.json"

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Définir la variable d'environnement pour utiliser le fichier de test
        os.environ["TASKS_FILE_PATH"] = TEST_TASKS_FILE
        # Créer le fichier de test avec une liste vide
        with open(TEST_TASKS_FILE, "w") as f:
            json.dump([], f)

    def tearDown(self):
        # Supprimer le fichier de test après chaque test
        if os.path.exists(TEST_TASKS_FILE):
            os.remove(TEST_TASKS_FILE)

    def test_add_task(self):
        # Ajouter une tâche et vérifier qu'elle a bien été enregistrée
        task = add_task("Test task", 2)
        tasks = load_tasks()
        self.assertTrue(any(t["id"] == task["id"] for t in tasks))
        self.assertEqual(task["description"], "Test task")
        self.assertEqual(task["priority"], 2)

    def test_delete_task(self):
        # Ajouter une tâche, puis la supprimer et vérifier qu'elle n'existe plus
        task = add_task("Task to delete", 1)
        tasks = load_tasks()
        self.assertTrue(any(t["id"] == task["id"] for t in tasks))
        delete_task(task["id"])
        tasks_after_delete = load_tasks()
        self.assertFalse(any(t["id"] == task["id"] for t in tasks_after_delete))

if __name__ == "__main__":
    unittest.main()
