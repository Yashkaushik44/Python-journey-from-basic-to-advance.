#                                                                       Object Oriented Programming in Python
---

# Introduction to OOP

OOP is used to organise code around the real world entities called "objects" rather than just functions logic. It bundles related data and behaviours together so your programs are easier to manage, reuse and scale.

```python
#syntax

class <class_name>:

	<code_block>
```

---

# `self`, `__init__()` and dunder

**`self`** is used as an reference to the specific instance of the class currently executing the code. 

**`__init__()`** is used to initialise objects and self in the class.

dunder is the double underscore we used to enclose the `init` function. It is used to specify a built in Python function.

```python
#example

class Test:

	def __init__(self, name):
	
		self.name = name
```
---

# Attributes and methods

Attributes are the variables attached to an object or class that store its specific data and characteristics.

Methods are the functions defined inside a class that describe the behaviour and actions an object can perform. 

```python
#example

class Car:

	def __init__(self, brand, colour):
	
		#attributes
		
		self.brand = brand
		self.colour = colour
		self.speed = 0
		
	#Methods
	
	def accelerate(self, acceleration):
	
		self.speed += acceleration
		
		print(f"{self.brand} accelerated to {self.speed} km/h")
```
