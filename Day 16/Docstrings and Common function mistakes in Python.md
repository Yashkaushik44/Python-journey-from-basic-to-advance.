#                                                           Docstrings and Common function mistakes in Python

---

# Docstrings

It is a documentation string placed right under the function definition to explain what a function does. It is best used to improve code readability and debugging easy.

```python
#example

def add(a, b):

	"""Returns the sum of two numbers."""
	return a + b
```

---

# Function type annotations 

It specify what data types the function's parameters expect and what type of value it returns.

```python
#this is the syntax for type annotations in python. I used <> to insert and it should not be treated as syntax.

def <function_name>(<variable_name1> : <variable_data_type1>, <variable_name2> : <variable_data_type2>) -> <return_value_data_type>:

	<code_block>

```

```python
#example

def add(a : int, b : int) -> int:

	return a + b
```

---

# Common function mistakes

## Mutable Default Arguments

It happens when a default parameter value like a list or dict is created once at function definition time, causing state to persist and shared across every call that omits that argument.

```python
#example

def append_item(itemm, target_list = []): #shared list is mutaed across calls

	target_list.append(item)
	
	return target_list
```

## Scope Bugs

It occur when trying to modify  a global variable inside a function without declaring it `global`, causing python to treat it as a local variable before it is defined.

```python
#example

count = 0

def increment():
	
	count += 1
```
