import os
import yaml

GITLE_YAML = "gitle.yaml"

def load_tasks(config_path=GITLE_YAML):
    if not os.path.exists(config_path):
        return {}
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f) or {}
    return config.get('tasks', {})

def list_tasks(tasks):
    if not tasks:
        print("No tasks defined in gitle.yaml.")
        return
    print("Tasks defined in gitle.yaml:")
    for name, info in tasks.items():
        desc = info.get('description', '')
        cmd = info.get('command', '')
        print(f"- {name}: {desc}\n    command: {cmd}")
