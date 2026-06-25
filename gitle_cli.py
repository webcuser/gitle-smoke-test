import sys
from gitle_tasks import load_tasks, list_tasks

def main():
    if len(sys.argv) < 2:
        print("Usage: gitle_cli.py <command>")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "list-tasks":
        tasks = load_tasks()
        list_tasks(tasks)
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
