
#                                                                                Arguments and keyword arguments in python

---

# `*args`

`*args` is used to pack multiple extra positional arguments into a tuples inside a function definition. 

```python
#example

def calculate_sum(*args): #it can take any number of argumnets up front.
	
	return sum(args) 
	
print(calculate_sum(10, 20, 34))
```

Note: Use the `*args` argument when you don't know how many arguments a function will receive upfront.

---

# `**kwargs`

`**kwargs` is used to collect any number of keyword arguments into a dictionary.

```python
#example

def print_profile(**kwargs): 

	for key, value in kwargs.items():
	
		print(f"{key} : {value}")
		
print_profile(name = "User", role = "Student")
```

Note: Use `**kwargs` when you need to pass keys and values as arguments.

---

# Argument Unpacking

We use `*` for converting arguments into tuples and `**` into dictionary inside the function. 

---

# Positional Only Parameters `/`

We use  `/`  to accept only the arguments with their values not by their positional argument name.

```python
#example

def power(base, exponent, /): 

	return base ** exponent
	
power(2, 3) # Valid 

#(calling power(base=2, exponent=3) raises an error)
```

---

# Keyword Only parameters `*`

We use `*` to accept arguments with there positional argument name stated explicitly.

```python 
#example

def greet(*, name, message): 

	print(f"{message}, {name}")

greet(name="User", message="Hello") # Valid 

#(calling greet("User", "Hello") raises an error)

```

