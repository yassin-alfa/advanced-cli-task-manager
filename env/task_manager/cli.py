import argparse
from task_manager.core import add_task, list_tasks, delete_task
from task_manager.logger import setup_logger


logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Commandes disponibles")

    add_parser = subparsers.add_parser("add", help="Ajouter une tâche")
    add_parser.add_argument("description", type=str, help="Description de la tâche")
    add_parser.add_argument("-p", "--priority", type=int, default=1, help="Priorité de la tâche")

    list_parser = subparsers.add_parser("list", help="Lister toutes les tâches")

    delete_parser = subparsers.add_parser("delete", help="Supprimer une tâche")
    delete_parser.add_argument("task_id", type=int, help="ID de la tâche à supprimer")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description, args.priority)
    elif args.command == "list":
        tasks = list_tasks()
        for task in tasks:
            print(task)
    elif args.command == "delete":
        delete_task(args.task_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
