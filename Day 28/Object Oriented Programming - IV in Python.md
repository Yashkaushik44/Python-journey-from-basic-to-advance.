#                                                                       Object Oriented Programming - IV in Python
---

# Polymorphism

**Polymorphism** means "many forms". It allows the same method or operation to work with different types of objects, even when their behaviour is different.

Polymorphism is useful when we want to use different objects through the same method without writing separate code for each object.

```python
#example

class Dog:

	def sound(self):
	
		print("Bark")

class Cat:

	def sound(self):
	
		print("Meow")


def make_sound(animal):

	animal.sound()

make_sound(Dog())
make_sound(Cat())
```

```text
Bark
Meow
```

Here, both objects have a `sound()` method. The `make_sound()` function calls the method of the object passed to it. The two classes do not need to inherit from the same parent class.

---

# Polymorphism through inheritance and method overriding

Polymorphism can also be achieved through **inheritance** and **method overriding**. A child class can define its own version of a method inherited from the parent class.

When we call that method, Python finds the method according to the actual object's class and its method lookup order.

```python
#example

class Animal:

	def sound(self):
	
		print("Animal sound")

class Dog(Animal):

	def sound(self):
	
		print("Bark")

class Cat(Animal):

	def sound(self):
	
		print("Meow")

animals = [Animal(), Dog(), Cat()]

for animal in animals:

	animal.sound()
```

```text
Animal sound
Bark
Meow
```

Here, `Dog` and `Cat` override the `sound()` method. The same call produces different results depending on the object. Overriding is one way to use polymorphism, but polymorphism does not always require inheritance.

---

# Polymorphism with built-in functions and operators

Some built-in Python functions work with different object types. For example, **`len()`** returns the number of items in a string, list or other supported object.

```python
#example

print(len("Python"))
print(len([10, 20, 30]))
print(len({"name": "Yash", "age": 18}))
```

```text
6
3
2
```

**Operator overloading** allows an operator to perform operations based on the objects used with it. The `+` operator can add numbers or join strings.

```python
#example

print(10 + 20)
print("Hello" + " Python")
```

```text
30
Hello Python
```

This is different from defining several methods with the same name inside one class. Python does not use traditional method overloading by keeping multiple method definitions with the same name. A later definition normally replaces the earlier one in that class.

---

# Duck typing

**Duck typing** means using an object based on the methods and behaviour it supports rather than checking which class it belongs to.

Objects do not need to share the same parent class. They only need to support the operations expected by the code using them.

```python
#example

class PDF:

	def open(self):
	
		print("Opening PDF")

class Image:

	def open(self):
	
		print("Opening image")


def open_file(file):

	file.open()

open_file(PDF())
open_file(Image())
```

```text
Opening PDF
Opening image
```

Here, `PDF` and `Image` are unrelated classes. Both support the `open()` method, so the same function can work with either object without checking its class.

Having a method with the same name is not always enough. The method must also accept the arguments and perform the behaviour expected by the calling code.

---

# Duck typing and error handling

Duck typing normally uses an object's methods directly. If the expected method does not exist, Python can raise an **`AttributeError`**.

**EAFP** stands for "Easier to Ask Forgiveness than Permission". It means trying an operation and handling an expected error if that operation fails.

```python
#example

class PDF:

	def open(self):
	
		print("Opening PDF")

class Text:

	def read(self):
	
		print("Reading text")


def open_file(file):

	try:
		file.open()
	except AttributeError:
		print("This object does not support open()")

open_file(PDF())
open_file(Text())
```

```text
Opening PDF
This object does not support open()
```

Here, the function tries to call `open()` instead of checking whether the object belongs to a particular class. We handle the missing method instead of allowing the program to stop.

We can also check an object's type before using it, but duck typing focuses on supported behaviour. Error handling is still necessary when an operation may fail. We should not ignore unrelated errors.

---

# Inheritance and the `is-a` relationship

**Inheritance** allows a child class to reuse or extend the attributes and methods of a parent class. It represents an **`is-a`** relationship when the child object can be used as the type of its parent.

```python
#example

class Animal:

	def eat(self):
	
		print("Animal is eating")

class Dog(Animal):

	def bark(self):
	
		print("Dog is barking")

dog = Dog()

dog.eat()
dog.bark()
```

```text
Animal is eating
Dog is barking
```

Here, a `Dog` is an `Animal`. The `Dog` class reuses the `eat()` method and adds its own `bark()` method.

Inheritance is useful when classes have a genuine parent-child relationship. However, a child class depends on the structure and behaviour of its parent. Changes to the parent can affect the child, so inheritance should not be used only to reuse a few methods.

---

# Composition and the `has-a` relationship

**Composition** means creating a class that contains and uses objects of other classes. It represents a **`has-a`** relationship rather than an `is-a` relationship.

One object can call the methods of another object to perform part of its work. This is called **delegation**.

```python
#example

class Engine:

	def start(self):
	
		print("Engine started")

class Car:

	def __init__(self):
	
		self.engine = Engine()
	
	def start(self):
	
		self.engine.start()
		print("Car is ready")

car = Car()
car.start()
```

```text
Engine started
Car is ready
```

Here, a `Car` has an `Engine`. The `Car` object uses the `Engine` object's `start()` method instead of inheriting from `Engine`.

Composition allows us to combine smaller objects to create larger functionality. It can make components easier to replace or reuse, although the containing class still depends on the component's expected behaviour.

---

# Composition vs. Inheritance

**Inheritance** is used when one class is a type of another class. It reuses behaviour through a parent-child relationship.

**Composition** is used when one object contains another object as a part of its functionality. It reuses behaviour by calling methods on the contained object.

The following example shows an object using an inherited method.

```python
#example

class Printer:

	def print_document(self):
	
		print("Printing document")

class OfficePrinter(Printer):

	pass

printer = OfficePrinter()
printer.print_document()
```

```text
Printing document
```

Here, `OfficePrinter` inherits the behaviour of `Printer`. However, if we want to create an office machine that **has a printer**, composition can represent that relationship more clearly.

```python
#example

class Printer:

	def print_document(self):
	
		print("Printing document")

class OfficeMachine:

	def __init__(self, printer):
	
		self.printer = printer
	
	def print_document(self):
	
		self.printer.print_document()

machine = OfficeMachine(Printer())
machine.print_document()
```

```text
Printing document
```

Here, `OfficeMachine` contains a `Printer` object and delegates printing to it. We can replace the printer with another object that supports a compatible `print_document()` method.

This also allows **polymorphism through composition**, because different components can be used through the same expected method.

```python
#example

class InkPrinter:

	def print_document(self):
	
		print("Printing with ink")

class LaserPrinter:

	def print_document(self):
	
		print("Printing with laser")

class OfficeMachine:

	def __init__(self, printer):
	
		self.printer = printer
	
	def print_document(self):
	
		self.printer.print_document()

machine1 = OfficeMachine(InkPrinter())
machine2 = OfficeMachine(LaserPrinter())

machine1.print_document()
machine2.print_document()
```

```text
Printing with ink
Printing with laser
```

The principle **"Favor composition over inheritance"** means we should consider composition when behaviour can be built from independent components instead of forcing a parent-child relationship.

Composition is not always better than inheritance. Use inheritance for a genuine `is-a` relationship where the child supports the parent's expected behaviour. Use composition when an object needs another object to perform part of its work. Both can also be used together when appropriate.
