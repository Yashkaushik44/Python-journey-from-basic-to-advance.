#                                                                       Object Oriented Programming - V in Python
---

# Multiple Inheritance and Method Resolution Order (MRO)

Multiple inheritance is used to inherit attributes and methods from more than one parent class into a single child class.

Method Resolution Order (MRO) is the order in which Python looks for attributes and methods in a class and its parent classes. Python uses an algorithm called C3 linearization to determine this order.

**`mro()`** returns the MRO of a class as a list whereas **`__mro__`** returns it as a tuple.

```python
#example

class A:

	def display(self):
	
		print("Class A")

class B(A):

	def display(self):
	
		print("Class B")
		super().display()

class C(A):

	def display(self):
	
		print("Class C")
		super().display()

class D(B, C):

	pass

x = D()
x.display()

print(D.mro())
print(D.__mro__)
```

When two parent classes inherit from the same class and a child class inherits from both of them, it forms a diamond inheritance structure. In the above example the MRO of class `D` is D, B, C, A and object.

`super()` is used to access the next method in the MRO rather than just the method of its direct parent class. If all the classes use `super()` to call the next method except the last one, the method of class `A` is executed only once. Python does not automatically execute the `__init__()` of every parent class.

---

# Dunder Methods and Operator Overloading

Dunder methods are the special methods in Python which are enclosed with double underscores. They are used to define the behaviour of an object when certain operations are performed on it.

**`__str__()`** is used to return a readable string representation of an object when we use `print()` or `str()` on it.

**`__repr__()`** is used to return a more descriptive string representation of an object.

**`__len__()`** is used to return the length of an object as a non-negative integer when we use `len()` on it.

```python
#example

class Test:

	def __init__(self, name):
	
		self.name = name
		
	def __str__(self):
	
		return self.name
		
	def __repr__(self):
	
		return f"Test({self.name!r})"
		
	def __len__(self):
	
		return len(self.name)

x = Test("Python")

print(x)
print(repr(x))
print(len(x))
```

Operator overloading is used to define the behaviour of existing operators when they are used on the objects of a class.

**`__add__()`**, **`__sub__()`** and **`__mul__()`** are used to overload the `+`, `-` and `*` operators respectively.

**`__eq__()`** and **`__lt__()`** are used to overload the `==` and `<` operators respectively.

```python
#example

class Test:

	def __init__(self, num):
	
		self.num = num
		
	def __add__(self, other):
	
		if not isinstance(other, Test):
		
			return NotImplemented
			
		return Test(self.num + other.num)

x = Test(10)
y = Test(20)

z = x + y
print(z.num)
```

---

# Dataclasses, `Enum` and `NamedTuple`

**Dataclasses** are the classes in which we use the `@dataclass` decorator to automatically generate methods like `__init__()`, `__repr__()` and `__eq__()` rather than defining them ourselves. The attributes used as fields are defined using type annotations.

```python
#example

from dataclasses import dataclass, field

@dataclass
class Student:

	name: str
	age: int = 18
	subjects: list = field(default_factory=list)

x = Student("Alex")
print(x)
```

`default_factory` is used to create a separate default value for each object in case of mutable fields like lists. Dataclasses are mutable by default but we can use `@dataclass(frozen=True)` to restrict the reassignment of their fields.

**`Enum`** is used to define a fixed set of named members inside a class. Each member has a name and a value attached to it which can be accessed using `.name` and `.value` respectively.

```python
#example

from enum import Enum

class Colour(Enum):

	RED = 1
	GREEN = 2
	BLUE = 3

print(Colour.RED)
print(Colour.RED.name)
print(Colour.RED.value)

print(Colour.RED == Colour.GREEN)

for colour in Colour:

	print(colour.name)
```

**`NamedTuple`** is used to create tuples with names assigned to their individual fields. We can access the values using their field names as well as their index values but we cannot reassign the fields of the tuple.

```python
#example

from typing import NamedTuple

class Student(NamedTuple):

	name: str
	age: int

x = Student("Alex", 18)

print(x.name)
print(x[1])
```

The type annotations used in dataclasses and `NamedTuple` do not restrict the type of values passed to their fields during runtime.
