# Static Analysis Issue Log

**Project:** `L5_37_todo_manager`  
**File reviewed:** `todo_manager.py`

The line numbers below refer to the original version of `todo_manager.py`. Use the saved baseline reports to confirm or adjust the line numbers after running the tools locally.

| Issue | Type / severity | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Unsafe pickle deserialization | Security / High | 36–43 | `pickle.load()` can execute code when loading an untrusted or tampered pickle file. | Replaced pickle persistence with JSON so saved tasks are treated as data. |
| Shell command injection risk | Security / High | 47–49 | Building a shell command by concatenating the email address can let shell metacharacters alter the command. | Use `subprocess.run()` with a list of arguments and no shell; reject newline characters in the address. |
| Mutable default argument | Correctness / Medium | 10 | The default `labels=[]` list is shared between calls and can lead to unexpected state. | Use `labels=None` and create a fresh list for each task. |
| Labels were not stored | Correctness / Medium | 11–14 | The original function appends the priority to labels but does not include labels in the task dictionary. | Store a copy of labels in each task and keep priority separate. |
| Invalid priority crashes sorting | Reliability / Medium | 25–27 | A priority not present in `PRIORITY_ORDER` raises `KeyError` during sorting. | Validate and normalize priority when adding a task. |
| Task IDs could be reused | Reliability / Medium | 11 | `len(tasks) + 1` may reuse an existing ID when IDs are not contiguous. | Generate the next ID using `max(TASKS, default=0) + 1`. |
| Search miss is implicit | Maintainability / Low | 30–34 | The function implicitly returns `None` when no title matches. | Document and explicitly return `None`; add a return type. |
| Random choice on an empty list | Reliability / Medium | 63 | `random.choice([])` raises `IndexError` when there are no pending tasks. | Check the list before choosing a suggestion. |
| Files use platform-default encoding | Portability / Low | 36–45 | Text file encoding is not specified consistently. | Specify UTF-8 for file reads and writes. |
| Demo runs during import | Maintainability / Low | 73 | Importing the module also runs the demonstration. | Guard the entry point with `if __name__ == "__main__":`. |
| Naming and documentation inconsistent | Style / Low | Throughout | CamelCase function names and limited documentation make the file less consistent with Python conventions. | Use `snake_case`, docstrings, type hints, and consistent formatting. |

## Verification checklist

- [ ] Run Pylint, Bandit, and Flake8 against the original file and save the baseline reports before replacing it.
- [ ] Run all three tools against the revised file and save the after reports.
- [ ] Review any remaining warnings rather than suppressing them blindly.
- [ ] Verify Pylint is above 9.5, or document any remaining justified warnings.
- [ ] Verify Bandit findings and Flake8 style errors are addressed.
- [ ] Run `python todo_manager.py` and confirm the demonstration completes.
- [ ] Update line numbers using the actual tool reports.
