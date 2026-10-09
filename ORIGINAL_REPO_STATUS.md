# Repository audit status

The public repository was inspected on 2026-10-09. The connected GitHub identity reports `pull: true` and `push: false`; these are local prepared replacements and have **not** been committed to GitHub.

## High-confidence defects observed in the original files

- `Python Basics/calculator.py`: division used the wrong operand and checked the wrong value for a zero divisor.
- `Practice/calender.py`: imported `calender` instead of Python's standard-library `calendar` module.
- `Python Basics/Assignment.py`: used `in` against an integer password (raising `TypeError`) and calculated the 10% discount incorrectly.
- `Python/eval_func.py`: evaluated untrusted input using `eval(input(...))`.
- `Python/parsing.py`: treated `bool("False")` as if it would parse the textual value; any non-empty string is truthy.
- `15July2026/packing.py`: shadowed the built-in `list` name.
- `8July2026/nested_dict.py`: contained invalid syntax (`company[]`) and a misspelled `empid` key.
- `8July2026/new.py`: used Python 2 syntax (`raw_input` and a print statement), which fails in Python 3.
- `22July2026/new1.py`: contained truncated code and syntax errors.
- `21July2026/nestedfun.py`: its counter example recursively called itself instead of incrementing an enclosing counter.
- `14July2026/function2.py`: a print statement after `return` was unreachable.
- `30June2026/if_elif.py`: ATM example could print a negative balance after an invalid withdrawal, and age bands had boundary inconsistencies.
- `Python Basics/ifelif.py`: ATM logic deducted money even on failure and did not allow exact-balance withdrawals.
- `Python Basics/strings.py`: comments listed wrong results for `find("h")` and `split("a")`.
- `6July2026/list.py`: hard-coded the list length instead of using `len()`.
- `17July2026/Pass_all_arg.py`: called a function without supplying the required second positional argument.
- `14July2026/tempCodeRunnerFile.py` and `Practice/__pycache__/calender.cpython-314.pyc` are temporary/generated files and should not be committed.

## Prepared changes

The bundle contains 26 replacement targets (24 source/documentation/configuration replacements plus the local helper and status file), including a revised README, `.gitignore`, source comments, input validation, and selected lesson logic fixes. The helper can copy replacements into a local Git clone and remove the known temporary/generated files. It does not move the dated folders, to avoid breaking the user's existing lesson paths.

This is a targeted corrective patch, **not** a claim that every one of the repository's 56 Python files has been rewritten or runtime-tested. Please review the diff and run the lessons before committing.
