#                                                                                         Return Values and Scope in Python

---

# Return Values

Return statement is used in python to send a value back from a function to the place where the function was called. The value that is sent back is called the return value.

```python
def add(a, b):

	return a + b

result = add(2, 3)

print(result) #output: 5
```

In the above code, the function `add()` calculates `a + b` and sends it back using `return`, which is stored in the variable `result`. When `return` runs, the function ends instantly and any code written after it inside the function is not executed.

`print()` only displays a value on the screen while `return` sends the value back to the caller so that it can be stored or used further.

```python
def show(a, b):

	print(a + b)

def give(a, b):

	return a + b

x = show(2, 3) #output: 5

y = give(2, 3)

print(x) #output: None

print(y) #output: 5
```

In the above code, `show()` only prints `5` and returns nothing so `x` becomes `None`, but `give()` returns `5` so it is stored in `y`.

---

# return None

When a function does not have a `return` statement, python automatically returns `None`. `None` is a special value which means no value.

```python
def greet(name):

	print("Hello", name)

result = greet("Aman") #output: Hello Aman

print(result) #output: None
```

In the above code, `greet()` has no `return` statement so python returns `None` by default.

We can also write `return None` ourselves, it is the same as writing only `return`.

```python
def check(n):

	if n < 0:

		return None

	return n * 2

print(check(-5)) #output: None

print(check(4)) #output: 8
```

In the above code, when `n` is negative the function returns `None` and ends, otherwise it returns `n * 2`.

---

# Multiple Return Values

A function can return more than one value by separating them with commas. Python packs all of them into a single tuple and returns it.

```python
def calculate(a, b):

	return a + b, a - b, a * b

result = calculate(10, 5)

print(result) #output: (15, 5, 50)

print(type(result)) #output: <class 'tuple'>
```

In the above code, three values are returned but python sends them together as one tuple.

The returned values can be unpacked into separate variables, the number of variables must be equal to the number of returned values.

```python
add, sub, mul = calculate(10, 5)

print(add) #output: 15

print(sub) #output: 5

print(mul) #output: 50
```

In the above code, the tuple `(15, 5, 50)` is unpacked in order, so `add` gets `15`, `sub` gets `5` and `mul` gets `50`.

---

# Variable Scope

Scope decides in which part of the code a variable can be accessed. Python has four scopes: Local, Enclosing, Global and Built-in.

---

# Local Scope

A variable created inside a function is a local variable and it can only be used inside that function.

```python
def show():

	x = 10

	print(x) #output: 10

show()

print(x) #output: NameError: name 'x' is not defined
```

In the above code, `x` exists only inside `show()` so using it outside gives an error.

---

# Global Scope

A variable created outside all functions is a global variable and it can be accessed anywhere in the programme, including inside functions.

```python
x = 10

def show():

	print(x) #output: 10

show()

print(x) #output: 10
```

In the above code, `x` is global so the function can read it without any extra keyword.

---

# Enclosing Scope

When a function is defined inside another function, the outer function's variables are in the enclosing scope of the inner function. The inner function can read them.

```python
def outer():

	x = "enclosing"

	def inner():

		print(x) #output: enclosing

	inner()

outer()
```

In the above code, `x` is not inside `inner()` and not global, so python finds it in the enclosing function `outer()`.

---

# Built-in Scope

Built-in scope contains the names that python already provides like `print`, `len` and `range`. They can be used anywhere without creating them.

```python
numbers = [1, 2, 3]

print(len(numbers)) #output: 3
```

In the above code, `len` is not created by us, python finds it in the built-in scope.

---

# LEGB Rule

LEGB rule is the order in which python searches for a variable name: Local → Enclosing → Global → Built-in. Python stops at the first place where the name is found.

```python
x = "global"

def outer():

	x = "enclosing"

	def inner():

		x = "local"

		print(x) #output: local

	inner()

	print(x) #output: enclosing

outer()

print(x) #output: global
```

In the above code, all three variables have the same name `x` but each one lives in a different scope. Inside `inner()` python finds the local `x` first, inside `outer()` it finds the enclosing `x` and outside both it finds the global `x`.

---

# global Keyword

If we assign a value to a variable inside a function, python treats it as a new local variable, even if a global variable with the same name exists.

```python
x = 10

def change():

	x = 20

	print(x) #output: 20

change()

print(x) #output: 10
```

In the above code, `x = 20` created a new local `x` so the global `x` stayed `10`.

`global` keyword is used to tell python that the name inside the function refers to the global variable, so it can be reassigned.

```python
count = 0

def increase():

	global count

	count = count + 1

increase()

print(count) #output: 1
```

In the above code, `global count` makes the function change the global `count` instead of creating a local one.

Without `global`, the line `count = count + 1` would make `count` local and python would give `UnboundLocalError` because it is used before getting a value.

---

# nonlocal Keyword

`nonlocal` keyword is used inside a nested function to reassign a variable of the enclosing function.

```python
def outer():

	x = 10

	def inner():

		nonlocal x

		x = 20

	inner()

	print(x) #output: 20

outer()
```

In the above code, `nonlocal x` makes `inner()` change the `x` of `outer()`. Without it, `x = 20` would create a new local variable and `outer()` would print `10`.

`global` works with variables of the global scope while `nonlocal` works with variables of the enclosing function scope. `nonlocal` cannot be used for a global variable and the variable must already exist in an enclosing function, otherwise python gives `SyntaxError`.

Neither `global` nor `nonlocal` is needed to only read a variable, they are needed only when we want to reassign it.