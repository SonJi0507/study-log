head = list(range(99999999))[0]
head = next(iter(range(99999999)))
list(range(0))[0]
next(iter(range(0)))[0]

# Ruff RUF015 규칙 결과
"""
Ruff/ruff-prac/src/fix_safety.py:1:8: RUF015 Prefer `next(iter(range(99999999)))` over single element slice
Ruff/ruff-prac/src/fix_safety.py:3:1: RUF015 Prefer `next(iter(range(0)))` over single element slice
Found 2 errors.
No fixes available (2 hidden fixes can be enabled with the `--unsafe-fixes` option).
"""
