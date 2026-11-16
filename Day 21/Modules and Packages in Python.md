#                                                                                               Modules and Packages in Python
---
# Python Modules

A Python module is simply a single `.py` file containing Python code such as variables, functions, and classes.

Modules help organize large programs into smaller, manageable, and reusable files instead of writing everything inside one long script.

# Creating a Custom Python Module

To create a module, save your Python code in a file with a `.py` extension.

```
# math_tools.py

PI = 3.14159

def add(a, b):
    return a + b

class Calculator:
    def multiply(self, a, b):
        return a * b
```

# Importing a Module and Accessing Members

Use the `import` keyword to load an entire module into another file located in the same directory, and use dot notation (`.`) to access its variables, functions, or classes.

```
# main.py

import math_tools

print(math_tools.PI) #output: 3.14159
print(math_tools.add(4, 5)) #output: 9

calc = math_tools.Calculator()
print(calc.multiply(3, 4)) #output: 12
```

# Importing Specific Members and Using Aliases

- `from ... import ...` :- Imports only specific variables, functions, or classes directly into the current file so you do not need dot notation.
    
    ```
    	# main.py
    
    	from math_tools import PI, add
    
    	print(PI) #output: 3.14159
    	print(add(10, 20)) #output: 30
    ```
    
- `as` (Aliases) :- Gives a shorter or custom name to an imported module or member to save typing or avoid name conflicts.
    
    ```
    	# main.py
    
    	import math_tools as mt
    	from math_tools import Calculator as Calc
    
    	print(mt.add(2, 3)) #output: 5
    	c = Calc()
    	print(c.multiply(2, 5)) #output: 10
    ```
    
- Difference between `import module` and `from module import name` :- `import module` loads the whole module object and keeps its items under the module namespace (`module.name`), preventing name clashes. `from module import name` copies only the selected item directly into your current file's namespace (`name`), which can overwrite existing variables with the same name.
    

# `__name__` and `if __name__ == "__main__":`

Every Python module has a built-in `__name__` variable. When a file is run directly, Python sets `__name__` to `"__main__"`. When the file is imported as a module into another file, Python sets `__name__` to the module's filename.

The `if __name__ == "__main__":` block lets you keep test or script execution code inside a module without running it automatically when another file imports that module.

```
# math_tools.py

def square(n):
    return n * n

if __name__ == "__main__":
    print("Running directly:")
    print(square(4)) #output: 16
```

```
# main.py

import math_tools

# Nothing prints during import because __name__ in math_tools is "math_tools"
print(math_tools.square(5)) #output: 25
```

# How Python Locates Modules and `sys.path`

When you write an `import` statement, Python searches for the module in a specific order:

1. Built-in modules (such as `sys` or `math`).
    
2. Directories listed in `sys.path`, starting with the directory of the script being run, followed by installed standard library and third-party package folders.
    

```
# check_path.py

import sys

print(sys.path) #output: list of directory paths Python searches for modules
```

# Importing Modules from Different Directories

If a module lives in a separate folder that is not a package, Python will not find it unless that folder is added to `sys.path`.

```
project/
├── helpers/
│   └── greetings.py
└── app.py
```

```
# helpers/greetings.py

def say_hello(name):
    return f"Hello, {name}!"
```

```
# app.py

import sys
sys.path.append("helpers")

import greetings

print(greetings.say_hello("Alex")) #output: Hello, Alex!
```

# Common Import Mistakes

- Shadowing standard modules :- Naming your file `math.py` or `random.py` causes Python to import your file instead of the built-in module. Always use unique, descriptive filenames.
    
- Circular imports :- Occurs when `file_a.py` imports `file_b.py` while `file_b.py` also imports `file_a.py` at the top level, raising an `ImportError`. Fix this by moving shared code into a third module.
    
- `ModuleNotFoundError` :- Happens when the module name is misspelled or the file is not inside any directory listed in `sys.path`.
    

# Python Packages and Subpackages

A Python package is a folder used to group related modules together into a structured hierarchy.

- Module vs. Package :- A module is a single `.py` file, whereas a package is a directory containing multiple modules (and optionally subpackages).
    
- Why packages are useful :- They prevent naming collisions between modules (for example, `audio.utils` and `video.utils`) and keep large projects organized.
    
- Subpackages :- Packages nested inside another package to organize deeper layers of functionality.
    

```
shop/
├── __init__.py
├── pricing.py
└── payments/
    ├── __init__.py
    └── card.py
```

# Creating and Importing from Packages and Subpackages

Using the directory structure above, place functions inside the package and subpackage modules, then import them using dot notation from outside the `shop` folder.

```
# shop/pricing.py

def apply_tax(amount):
    return amount * 1.10
```

```
# shop/payments/card.py

def process_card(amount):
    return f"Charged ${amount:.2f} to card"
```

```
# main.py (located outside the shop folder)

import shop.pricing
from shop.payments import card
from shop.payments.card import process_card

total = shop.pricing.apply_tax(100)
print(total) #output: 110.0
print(card.process_card(total)) #output: Charged $110.00 to card
print(process_card(50)) #output: Charged $50.00 to card
```

# Absolute vs. Relative Imports

Inside a package, modules can import other modules from the same package in two ways:

- Absolute imports :- Specify the full path starting from the top-level package name. This is the recommended approach for clarity.
    
    ```
    	# shop/payments/card.py
    
    	from shop.pricing import apply_tax
    
    	def charge_with_tax(amount):
    	    final_amount = apply_tax(amount)
    	    return f"Total charged: ${final_amount:.2f}"
    ```
    
- Relative imports :- Use leading dots to refer to locations relative to the current module's position inside the package. A single dot (`.`) means the current package directory, and two dots (`..`) mean the parent package directory.
    
    ```
    	# shop/payments/card.py
    
    	from ..pricing import apply_tax # '..' moves up from payments/ to shop/
    	from . import refund # '.' refers to the current payments/ folder
    ```
    

# `__init__.py` and Package Initialization

`__init__.py` is a special file placed inside a package directory. When a package or any module inside it is imported for the first time, Python automatically executes the code inside `__init__.py`.

You can use `__init__.py` to expose selected functions, classes, or variables directly at the package level so users do not need to know the internal file layout.

```
# shop/__init__.py

from .pricing import apply_tax
from .payments.card import process_card
```

```
# main.py

import shop

# Accessible directly through the shop namespace because of __init__.py
print(shop.apply_tax(200)) #output: 220.0
print(shop.process_card(220)) #output: Charged $220.00 to card
```

# Regular Packages vs. Namespace Packages

- Regular Packages :- Directories that contain an `__init__.py` file (even if the file is empty). They run initialization code on import and are the standard choice for most Python projects.
    
- Namespace Packages :- Directories without an `__init__.py` file. Python 3.3+ automatically treats folders without `__init__.py` as namespace packages, allowing a single logical package name to span across multiple directories without running initialization code.
    

# Common Package Mistakes

- Running a file inside a package directly when it uses relative imports :- Running `python shop/payments/card.py` directly raises `ImportError: attempted relative import with no known parent package`. Always run from the root project folder using the `-m` flag (`python -m shop.payments.card`).
    
- Importing only the package name without exposing members :- Running `import shop` does not automatically import `shop.pricing` unless `pricing` is explicitly imported inside `shop/__init__.py` or imported directly via `import shop.pricing`.
    
- Forgetting the project root directory :- Import statements like `from shop import pricing` only work when Python is executed from the parent directory that contains the `shop/` folder.