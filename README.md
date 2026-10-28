# Lab 5: Static Code Analysis — To-Do List & Task Manager

**Main file:** `todo_manager.py`

## About the program

This task manager adds tasks with priorities, marks tasks complete, lists pending tasks by priority, searches by keyword, suggests a task, and saves or exports tasks.

## Setup

Install the analysis tools:

```bash
python -m pip install pylint bandit flake8
```

## Preserve baseline reports first

If you have not already done so, run the three tools against the original `todo_manager.py` and save their outputs before replacing it. The original reports are important for the lab's before-and-after comparison.

```bash
python -m pylint todo_manager.py > pylint_report.txt
python -m bandit -r todo_manager.py > bandit_report.txt
python -m flake8 todo_manager.py > flake8_report.txt
```

## Run the revised program

```bash
python todo_manager.py
```

The demo writes `tasks.json` and `tasks_export.json` in the current directory. The revised program uses JSON for persistence instead of loading pickle files.

## Analyze the revised code

Save the final reports under distinct names so they do not overwrite the baseline:

```bash
python -m pylint todo_manager.py > pylint_report_after.txt
python -m bandit -r todo_manager.py > bandit_report_after.txt
python -m flake8 todo_manager.py > flake8_report_after.txt
```

Review the reports and do not assume a target score or zero findings until you have run the tools locally. Tool versions may affect exact results.

## Deliverables

- `todo_manager.py`: revised program.
- `issues.md`: static-analysis issue log.
- `reflection.md`: draft reflection responses; align them with the exact questions in the handout.

See `issues.md` for the findings and verification checklist.
