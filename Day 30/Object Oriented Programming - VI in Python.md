#                                                                       Abstract Base Classes, Iterables and Iterators in Python
---

# Abstract Base Classes and Interfaces with `abc`

An abstract base class is a class used to define a common set of methods for the classes inheriting from it. It can be created by importing `ABC` from the `abc` module.

**`@abstractmethod`** is used to specify a method as an abstract method. A class cannot be instantiated until all of its abstract methods are implemented as concrete methods.

Abstract base classes can also contain attributes and concrete methods. An abstract method itself can contain a block of code.

```python
#example

from abc import ABC, abstractmethod

class Vehicle(ABC):

	@abstractmethod
	def start(self):
	
		pass
	
	def stop(self):
	
		print("Vehicle stopped")

class Car(Vehicle):

	def start(self):
	
		print("Car started")

car = Car()

car.start()
car.stop()
```

Python does not have a separate `interface` keyword. Abstract base classes can be used as interfaces to specify the methods a derived class should implement. They do not check whether the implemented methods have the same parameters or perform the intended action.

---

# Iterables vs. Iterators: `iter()` and `next()`

An iterable is an object from which we can obtain an iterator. Lists, tuples, strings, sets and dictionaries are examples of iterables.

An iterator is an object used to return successive values while keeping track of its current position. Every iterator is an iterable but not every iterable is an iterator.

**`iter()`** is used to obtain an iterator from an iterable object. If an iterator itself is passed to `iter()` it returns the same iterator.

**`next()`** is used to retrieve the next value from an iterator. It raises a `StopIteration` exception when there are no more values to return. We can also pass a default value to `next()` which is returned when the iterator is exhausted.

```python
#example

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator)) #10
print(next(iterator)) #20
print(next(iterator)) #30
print(next(iterator, 0)) #0
```

Calling `iter()` again on the exhausted iterator does not reset its position. We can obtain a new iterator by passing the list to `iter()` again.

A `for` loop obtains an iterator from the iterable and retrieves its values until the `StopIteration` exception is raised. The exception is handled by the loop itself.

---

# The Iterator Protocol and Custom Iterators

The iterator protocol is a set of rules followed by an iterator object. It consists of the `__iter__()` and `__next__()` methods.

**`__iter__()`** is used to return the iterator object itself.

**`__next__()`** is used to return the next value and raise a `StopIteration` exception when there are no more values to return.

```python
#example

class Counter:

	def __init__(self, limit):
	
		self.limit = limit
		self.count = 1
	
	def __iter__(self):
	
		return self
	
	def __next__(self):
	
		if self.count > self.limit:
		
			raise StopIteration
		
		value = self.count
		self.count += 1
		
		return value

counter = Counter(3)

iterator = iter(counter)

print(next(iterator)) #1

for value in iterator:

	print(value)
```

The `count` attribute is used to store the current position of the iterator. Once the count exceeds the limit the iterator continues to raise `StopIteration` whenever `__next__()` is called.

An iterable does not need to have a `__next__()` method. We can create a custom iterable by defining an `__iter__()` method which returns a separate iterator object.

```python
#example

class Numbers:

	def __init__(self, numbers):
	
		self.numbers = numbers
	
	def __iter__(self):
	
		return iter(self.numbers)

numbers = Numbers([10, 20, 30])

for value in numbers:

	print(value)

for value in numbers:

	print(value)
```

Here a new iterator is returned every time `__iter__()` is called, allowing us to iterate over the same object again from the beginning.
