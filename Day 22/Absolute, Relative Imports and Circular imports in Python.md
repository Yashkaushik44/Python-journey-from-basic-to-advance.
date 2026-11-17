#                                         Absolute, Relative Imports and Circular imports in Python

---

# Absolute import

It specifies the full path to a module starting from the project's root directory.

```python
# example

from my_project.utils.helpers import format_date
```

---

# Relative Import 

It specifies the path to a module relative to the current file's location using dots( `.` for current folder and `..` for parent folder)

```python
#example
from .helpers import format_date
```

---

# Circular Import

Occurs when two or more modules depend on each other directly or indirectly causing and `ImportError` because Python tries to load an incomplete module. 

```python
#example
from module_a import func_a # failes if module_a simultaneously imports module_b
```
