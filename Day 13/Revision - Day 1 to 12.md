
#                                                                                           Python Revision - Days 1 to 12

---

# Basics

Python is a programming language. We write code in a file with .py extension and run it.

Variables store values. We do not need to write the data type.

```python
name = "Yash"
age = 20
```

---

# Strings

Strings are text. We can use single or double quotes.

```python
text = "Hello"
print(text[0]) #output: H
print(text[1:4]) #output: ell
```

Strings are immutable. We cannot change a character directly.

---

# Lists

Lists store multiple values and can be changed.

```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers) #output: [1, 2, 3, 4]
```

---

# Tuples

Tuples are like lists but cannot be changed after creation.

```python
point = (10, 20)
print(point[0]) #output: 10
```

---

# Sets

Sets store unique values only. Duplicates are removed automatically.

```python
values = {1, 2, 2, 3}
print(values) #output: {1, 2, 3}
```

---

# Dictionaries

Dictionaries store data in key-value pairs.

```python
student = {"name": "Yash", "age": 20}
print(student["name"]) #output: Yash
```

---

# Functions

A function is a block of code with a name. We define it with def and call it later.

```python
def greet():
	print("Hello")

greet()
```

Parameters are the names inside the function. Arguments are the values we pass when calling.

---

# *args and **kwargs

*args collects extra positional arguments into a tuple.  
**kwargs collects keyword arguments into a dictionary.

```python
def add(*args):
	return sum(args)

print(add(1, 2, 3)) #output: 6
```

---

# Return Values

return sends a value back from the function. Without it, the function returns None.

```python
def add(a, b):
	return a + b

result = add(2, 3)
print(result) #output: 5
```

---

# Scope

Scope decides where a variable can be used.

- Local: inside a function
    
- Enclosing: in an outer function
    
- Global: outside all functions
    
- Built-in: names already available in Python
    

LEGB is the order Python searches: Local → Enclosing → Global → Built-in.

---

# Copying

copy.copy() makes a shallow copy. Nested objects are still shared.  
copy.deepcopy() makes a full independent copy.