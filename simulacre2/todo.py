import argparse
import csv
import os

def create_parser():
    parser = argparse.ArgumentParser(description="TODO program")
    parser.add_argument("action", type=str, choices=["add", "list"])
    parser.add_argument("title", type=str, nargs="?")
    parser.add_argument("-d", "--description", type=str)
    parser.add_argument("-p", "--priority", type=int)
    parser.add_argument("-f", "--filepath", type=str, default="/home/jpuigcerver/.todo.csv")
    return parser


class Task:
    def __init__(self, title, description="", priority=1):
        self.title = title
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"P{self.priority} - {self.title} - {self.description}"


def load_tasks(filepath):
    tasks = []
    if not os.path.isfile(filepath):
        print(f"{filepath} doesnt exist")
        return tasks

    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["title"]
            description = row["description"]
            priority = row["priority"]
            t = Task(title, description, priority)
            tasks.append(t)
    return tasks


def list_tasks(filepath, priority=None):
    tasks = load_tasks(filepath)

    if len(tasks) == 0:
        print("No tasks found")
        return

    for i, t in enumerate(tasks):
        if priority and t.priority != priority:
            continue

        print(f"{i}: {t}")


def save_task(filepath, task):
    with open(filepath, mode='a') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "description", "priority"])
        writer.writerow({'title': task.title, 'description': task.description, 'priority': task.priority})


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    if args.action == "add":
        if args.title == None:
            print("Title must be set in 'add' action.")
            exit(1)

        priority = 1
        if args.priority:
            priority = args.priority

        task = Task(args.title, args.description, priority)
        save_task(args.filepath, task)

    elif args.action == "list":
        list_tasks(filepath=args.filepath, priority=args.priority)
    else:
        print("ACTION NOT SUPPORTED")