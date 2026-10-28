"""A small task manager used to demonstrate static code analysis."""

import json
import random
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

TASKS: dict[int, dict[str, Any]] = {}
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def add_task(
    title: str,
    priority: str = "medium",
    labels: list[str] | None = None,
) -> int:
    """Add a task and return its ID."""
    normalized_priority = priority.lower()
    if normalized_priority not in PRIORITY_ORDER:
        valid_priorities = ", ".join(PRIORITY_ORDER)
        raise ValueError(f"Invalid priority. Choose one of: {valid_priorities}.")
    if not title.strip():
        raise ValueError("Task title cannot be empty.")

    task_id = max(TASKS, default=0) + 1
    TASKS[task_id] = {
        "title": title.strip(),
        "priority": normalized_priority,
        "labels": list(labels) if labels is not None else [],
        "done": False,
        "created": datetime.now().isoformat(timespec="seconds"),
    }
    return task_id


def complete_task(task_id: int) -> bool:
    """Mark a task complete; return False when its ID does not exist."""
    task = TASKS.get(task_id)
    if task is None:
        print(f"No task with id {task_id}")
        return False
    task["done"] = True
    return True


def pending_tasks() -> list[str]:
    """Return pending task titles, ordered by priority."""
    pending = [task for task in TASKS.values() if not task["done"]]
    pending.sort(key=lambda task: PRIORITY_ORDER[task["priority"]])
    return [task["title"] for task in pending]


def find_task(keyword: str) -> int | None:
    """Return the ID of the first title containing keyword, or None."""
    search_term = keyword.casefold()
    for task_id, task in TASKS.items():
        if search_term in task["title"].casefold():
            return task_id
    return None


def save_tasks(file_name: str = "tasks.json") -> None:
    """Save tasks as JSON instead of unsafe pickle data."""
    with Path(file_name).open("w", encoding="utf-8") as file:
        json.dump(TASKS, file, indent=2)


def load_tasks(file_name: str = "tasks.json") -> dict[int, dict[str, Any]]:
    """Load tasks from JSON and convert object keys back to integers."""
    with Path(file_name).open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise ValueError("The task file must contain a JSON object.")

    loaded_tasks: dict[int, dict[str, Any]] = {}
    for task_id, task in data.items():
        if not isinstance(task, dict):
            raise ValueError(f"Task {task_id} must be a JSON object.")
        loaded_tasks[int(task_id)] = task
    return loaded_tasks


def export_json(file_name: str = "tasks_export.json") -> None:
    """Export the current tasks as a readable JSON file."""
    with Path(file_name).open("w", encoding="utf-8") as file:
        json.dump(TASKS, file, indent=2)


def remind_by_email(address: str, file_name: str = "tasks.json") -> bool:
    """Send task data using the local mail command without invoking a shell."""
    if not address or any(character in address for character in "\r\n"):
        raise ValueError("A valid single-line email address is required.")

    try:
        task_data = Path(file_name).read_text(encoding="utf-8")
    except OSError as error:
        print(f"Could not read task data: {error}")
        return False

    try:
        result = subprocess.run(
            ["mail", "-s", "Pending tasks", address],
            input=task_data,
            text=True,
            check=False,
            capture_output=True,
        )
    except OSError as error:
        print(f"Could not start the mail command: {error}")
        return False

    if result.returncode != 0:
        print(f"Mail command failed: {result.stderr.strip()}")
        return False
    return True


def main() -> None:
    """Run a short demonstration of the task manager."""
    TASKS.clear()
    add_task("Submit lab report", "high", ["college"])
    add_task("Buy groceries")
    add_task("Call plumber", "low")
    add_task("Book train tickets", "high")
    complete_task(2)
    complete_task(99)

    print("Pending tasks:", pending_tasks())
    print("Task id for 'plumber':", find_task("plumber"))
    print("Task id for 'gym':", find_task("gym"))

    pending = pending_tasks()
    if pending:
        print("Try this next:", random.choice(pending))
    else:
        print("No pending tasks to suggest.")

    save_tasks()
    restored = load_tasks()
    print("Tasks restored from file:", len(restored))
    export_json()
    print("Exported tasks to tasks_export.json")


if __name__ == "__main__":
    main()
