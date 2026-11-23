#                                                                       Object Oriented Programming - III in Python
---

# Encapsulation

Encapsulation is used to bundle related data and methods together inside a class. It also helps to control how the attributes of an object are accessed and modified.

Public attributes can be accessed directly from outside the class. Python does not require every attribute to have a separate getter or setter method.

```python
#example

class Student:

	def __init__(self, name, marks):
	
		self.name = name
		self.marks = marks

student = Student("Yash", 85)

print(student.name)
print(student.marks)
```

```text
Yash
85
```

---

# Public, protected and private naming conventions

**Public attributes** are the normal attributes that can be accessed using an object.

**`_variable`** uses a single leading underscore to indicate that an attribute is intended for internal use. It is a naming convention and does not prevent access from outside the class.

**`__variable`** uses two leading underscores to trigger name mangling inside a class. Python changes its name to include the class name, which helps to avoid accidental name conflicts.

Python does not enforce strict private access like some other programming languages. Name mangling does not make an attribute completely inaccessible.

```python
#example

class Bank:

	def __init__(self, balance):
	
		self.name = "Savings"
		self._account_type = "Personal"
		self.__balance = balance
	
	def show_balance(self):
	
		print(self.__balance)

account = Bank(5000)

print(account.name)
print(account._account_type)
account.show_balance()
print(account._Bank__balance)
```

```text
Savings
Personal
5000
5000
```

The `__balance` attribute is stored using the name `_Bank__balance`. Accessing it with `account.__balance` would raise an `AttributeError`.

---

# Getters and setters

**Getter methods** are used to retrieve the value of an attribute.

**Setter methods** are used to change the value of an attribute. They can also check whether the new value is valid before updating it.

```python
#example

class Bank:

	def __init__(self, balance):
	
		self._balance = balance
	
	def get_balance(self):
	
		return self._balance
	
	def set_balance(self, balance):
	
		if balance >= 0:
			self._balance = balance
		else:
			print("Invalid balance")

account = Bank(5000)

account.set_balance(7000)
print(account.get_balance())

account.set_balance(-100)
print(account.get_balance())
```

```text
7000
Invalid balance
7000
```

Here, the setter prevents negative values from replacing the existing balance. Getters and setters are useful when access needs extra behaviour, but they are not necessary for every attribute.

---

# Properties and `@property`

**`@property`** is a decorator used to access a method through attribute syntax. It allows us to add behaviour while reading an attribute without calling the method using `()`.

A property with a getter but no setter is read-only through that property. This does not mean that every underlying attribute of the object is immutable.

```python
#example

class Student:

	def __init__(self, name, marks):
	
		self.name = name
		self._marks = marks
	
	@property
	def marks(self):
	
		return self._marks

student = Student("Yash", 85)

print(student.marks)
```

```text
85
```

Here, `marks` is a property. We use `student.marks` instead of `student.marks()` to get its value. Assigning to `student.marks` would raise an `AttributeError` because the property has no setter.

---

# Property setters and validation

**`@property_name.setter`** is used to define what happens when a new value is assigned to a property. It can also validate the value before changing the object's data.

```python
#example

class Student:

	def __init__(self, name, marks):
	
		self.name = name
		self._marks = 0
		self.marks = marks
	
	@property
	def marks(self):
	
		return self._marks
	
	@marks.setter
	def marks(self, value):
	
		if 0 <= value <= 100:
			self._marks = value
		else:
			print("Invalid marks")

student = Student("Yash", 85)

student.marks = 95
print(student.marks)

student.marks = 120
print(student.marks)
```

```text
95
Invalid marks
95
```

The `marks` setter checks the new value before changing `_marks`. The `@property` method returns the current value when the attribute is accessed.

Properties also allow an ordinary attribute-style interface to remain the same even when the internal implementation changes.

---

# Computed properties and property deleters

A computed property returns a value calculated from other attributes rather than storing the result separately.

**`@property_name.deleter`** is used to define what happens when a property is deleted using `del`.

```python
#example

class Rectangle:

	def __init__(self, length, width):
	
		self.length = length
		self.width = width
	
	@property
	def area(self):
	
		return self.length * self.width

rectangle = Rectangle(10, 5)

print(rectangle.area)

rectangle.width = 8
print(rectangle.area)
```

```text
50
80
```

Here, the `area` property calculates its value each time it is accessed.

```python
#example

class Student:

	def __init__(self, name):
	
		self._name = name
	
	@property
	def name(self):
	
		return self._name
	
	@name.deleter
	def name(self):
	
		del self._name

student = Student("Yash")

del student.name

print(hasattr(student, "_name"))
```

```text
False
```

A property should not use the same attribute for its own storage, such as assigning `self.marks` inside the `marks` setter. Doing that would call the same setter again. Use a separate attribute like `self._marks` instead.

---

# Inheritance

Inheritance is used to create a new class from an existing class. The new class can reuse the attributes and methods of the existing class and add its own behaviour.

The existing class is called the **parent class** or **base class**. The new class is called the **child class** or **derived class**.

```python
#syntax

class Parent:

	pass

class Child(Parent):

	pass
```

```python
#example

class Animal:

	def __init__(self, name):
	
		self.name = name
	
	def show_name(self):
	
		print(self.name)

class Dog(Animal):

	def bark(self):
	
		print("Dog is barking")

dog = Dog("Bruno")

dog.show_name()
dog.bark()
```

```text
Bruno
Dog is barking
```

Here, `Dog` inherits `show_name()` and the attributes initialised by `Animal`. It also defines its own `bark()` method.

Inheritance is generally useful when a child class represents a type of its parent class, also called an **is-a relationship**. It supports code reuse, but not every relationship between two classes needs inheritance.

---

# Types of inheritance

**Single inheritance** is when a child class inherits from one parent class.

**Multilevel inheritance** is when a class inherits from another child class, forming a chain.

**Multiple inheritance** is when a child class inherits from more than one parent class.

**Hierarchical inheritance** is when multiple child classes inherit from the same parent class.

**Hybrid inheritance** is a combination of two or more inheritance structures.

```python
#example

#Single inheritance

class Animal:

	def eat(self):
	
		print("Eating")

class Dog(Animal):

	pass

Dog().eat()
```

```text
Eating
```

```python
#example

#Multilevel inheritance

class Animal:

	def eat(self):
	
		print("Eating")

class Mammal(Animal):

	pass

class Dog(Mammal):

	pass

Dog().eat()
```

```text
Eating
```

```python
#example

#Multiple inheritance

class Walker:

	def walk(self):
	
		print("Walking")

class Swimmer:

	def swim(self):
	
		print("Swimming")

class Duck(Walker, Swimmer):

	pass

duck = Duck()

duck.walk()
duck.swim()
```

```text
Walking
Swimming
```

```python
#example

#Hierarchical inheritance

class Animal:

	def eat(self):
	
		print("Eating")

class Dog(Animal):

	pass

class Cat(Animal):

	pass

Dog().eat()
Cat().eat()
```

```text
Eating
Eating
```

```python
#example

#Hybrid inheritance

class Animal:

	def eat(self):
	
		print("Eating")

class Walker(Animal):

	def walk(self):
	
		print("Walking")

class Swimmer(Animal):

	def swim(self):
	
		print("Swimming")

class Duck(Walker, Swimmer):

	pass

duck = Duck()

duck.eat()
duck.walk()
duck.swim()
```

```text
Eating
Walking
Swimming
```

---

# Method overriding

Method overriding is used when a child class defines a method with the same name as a method inherited from its parent class. The child class method takes precedence during normal method lookup.

It allows the child class to change or extend inherited behaviour without modifying the parent class.

```python
#example

class Animal:

	def sound(self):
	
		print("Animal makes a sound")

class Dog(Animal):

	def sound(self):
	
		print("Dog barks")

animal = Animal()
dog = Dog()

animal.sound()
dog.sound()
```

```text
Animal makes a sound
Dog barks
```

Here, `Dog` overrides the inherited `sound()` method. If the child class did not define `sound()`, it would use the inherited method instead. Python does not require an `override` keyword for ordinary method overriding.

---

# `super()`

**`super()`** is used to access methods through the class inheritance order. It is commonly used to call inherited behaviour from an overridden method.

It does not always refer directly to the immediate parent class. Python uses the Method Resolution Order (MRO) to determine where the next method is found.

```python
#example

class Animal:

	def sound(self):
	
		print("Animal makes a sound")

class Dog(Animal):

	def sound(self):
	
		super().sound()
		print("Dog barks")

dog = Dog()

dog.sound()
```

```text
Animal makes a sound
Dog barks
```

Here, `super().sound()` calls the next `sound()` method in the inheritance order before the child class prints its own message.

---

# `super()` and `__init__()`

**`super().__init__()`** is commonly used to run the inherited initialisation logic before adding new attributes in a child class.

If a child class defines its own `__init__()`, Python does not automatically run the parent class's `__init__()` separately. We can use `super()` to include that initialisation.

```python
#example

class Employee:

	def __init__(self, name):
	
		self.name = name

class Manager(Employee):

	def __init__(self, name, department):
	
		super().__init__(name)
		self.department = department

manager = Manager("Yash", "IT")

print(manager.name)
print(manager.department)
```

```text
Yash
IT
```

Here, `super().__init__(name)` initialises the inherited `name` attribute and the child class initialises `department`.

Calling `Employee.__init__(self, name)` explicitly is also possible, but it directly names the parent class and is not always interchangeable with `super()` in multiple inheritance.

---

# Method Resolution Order (MRO)

MRO is the order Python follows while looking for attributes and methods in a class and its inherited classes.

**`ClassName.mro()`** can be used to see that order.

```python
#example

class A:

	def show(self):
	
		print("A")

class B(A):

	def show(self):
	
		print("B")

class C(A):

	def show(self):
	
		print("C")

class D(B, C):

	pass

object = D()

object.show()
print([cls.__name__ for cls in D.mro()])
```

```text
B
['D', 'B', 'C', 'A', 'object']
```

Here, `D` finds the `show()` method in `B` first. Multiple inheritance can affect which method is selected when parent classes contain methods with the same name.

```python
#example

class A:

	def show(self):
	
		print("A")

class B(A):

	def show(self):
	
		print("B")
		super().show()

class C(A):

	def show(self):
	
		print("C")
		super().show()

class D(B, C):

	pass

D().show()
```

```text
B
C
A
```

Here, `super()` in `B` follows the MRO to `C`, then `super()` in `C` continues to `A`. This is why `super()` does not simply mean calling a named parent class.
