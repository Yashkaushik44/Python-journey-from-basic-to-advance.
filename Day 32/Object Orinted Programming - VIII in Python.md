#                                                                                              Generators and Decorators in Python
---

# `yield from` and Generator Expressions in Depth

**`yield from`** is used to yield the individual values of another iterable. We can use it to yield values from multiple iterables without having to use a separate `for` loop for each iterable.

```python
#example

def numbers():

	yield from range(3)
	return 5

def values():

	a = yield from numbers()
	yield from [3, 4]
	yield a

print(list(values())) #[0, 1, 2, 3, 4, 5]
```

In the above example once all the values from `numbers()` are yielded, its return value is stored in `a` and the execution of `values()` continues. The return value of `numbers()` is yielded only because we have used a separate `yield` statement for it.

For yielding values, `yield from iterable` works similar to iterating over the iterable using a `for` loop and yielding each value. Unlike `yield from`, `yield` would yield the entire iterable as a single value.

Generator expressions can also contain conditional expressions and multiple `for` clauses. Similar to list comprehensions the condition written after the `for` clause is used to filter values whereas a conditional expression written before the `for` clause is used to determine the value to be generated.

```python
#example

a = (i + j for i in range(2) for j in range(2))

print(next(a)) #0
print(list(a)) #[1, 1, 2]
print(list(a)) #[]

b = (i if i % 2 == 0 else -i for i in range(4))

print(list(b)) #[0, -1, 2, -3]
```

Unlike a list comprehension, a generator expression returns a generator object instead of a list. The iterable in the first `for` clause is evaluated and its iterator is created when we create the generator expression but the remaining iteration and computation of values takes place as we iterate over it. Converting a generator object to a list consumes all its remaining values and we cannot generate those values again using the same generator object.

We can pass a generator expression directly to functions like `sum()`, `min()` and `max()`. If the generator expression is the only argument passed to the function we don't have to use an extra pair of parentheses.

```python
#example

print(sum(i for i in range(5))) #10
print(max((i for i in range(5)), default = 0)) #4
```

---

# Decorators: Functions as First-Class Objects

Functions in Python are first-class objects which means we can assign a function to a variable, pass it as an argument to another function and also return it from another function.

```python
#example

def greet():

	print("Hello")

def display(func):

	return func

a = greet
b = display(a)

b() #Hello
```

When we assign `greet` to `a` both of them refer to the same function object. Unlike `greet()` which calls the function, `greet` is used to refer to the function itself.

**Decorators** are callable objects which take another object as an argument and return an object which replaces it. A function decorator usually takes a function as an argument and returns another function which is used to extend or modify the behavior of the original function.

```python
#example

def decorator(func):

	def wrapper():

		print("Before calling the function")
		func()

	return wrapper

@decorator
def greet():

	print("Hello")

greet()
#Before calling the function
#Hello
```

In the above example the `wrapper()` function can access `func` even after `decorator()` has finished its execution as it forms a closure. We can also apply the decorator without using the `@` syntax by writing `greet = decorator(greet)` after defining `greet()` without the decorator.

The decorator is executed when the definition of the function being decorated is executed. The returned wrapper function is assigned to `greet` and it is the wrapper function which is executed every time we call `greet()`.

---

# Custom Decorators, `functools.wraps` and Decorator Arguments

When we use a decorator on a function which takes arguments, we can use `*args` and `**kwargs` in the wrapper function to receive the positional and keyword arguments and pass them to the original function. If the original function returns a value we can also return that value from the wrapper function.

```python
#example

def decorator(func):

	def wrapper(*args, **kwargs):

		print("Calling the function")
		return func(*args, **kwargs)

	return wrapper

@decorator
def add(a, b):

	return a + b

print(add(2, b = 3))
#Calling the function
#5

print(add.__name__) #wrapper
```

**`functools.wraps`** is used to preserve the attributes of the original function such as its name (`__name__`) and its docstring (`__doc__`). In the above example `add` refers to the wrapper function which is why its `__name__` is `wrapper` instead of `add`.

```python
#example

from functools import wraps

def decorator(func):

	@wraps(func)
	def wrapper(*args, **kwargs):

		return func(*args, **kwargs)

	return wrapper

@decorator
def add(a, b):

	"""Adds two values"""
	return a + b

print(add.__name__) #add
print(add.__doc__) #Adds two values
print(add.__wrapped__(2, 3)) #5
```

`wraps` also creates the `__wrapped__` attribute which refers to the original function in this example. We still have to pass the arguments and return the value from the wrapper function ourselves.

We can also pass arguments to a decorator itself. For this we can create another function which takes the decorator arguments and returns the decorator function. This function is called a decorator factory.

```python
#example

from functools import wraps

def message(text):

	def decorator(func):

		@wraps(func)
		def wrapper(*args, **kwargs):

			print(text)
			return func(*args, **kwargs)

		return wrapper

	return decorator

@message("Calling add")
def add(a, b):

	return a + b

print(add(2, 3))
#Calling add
#5
```

In the above example `message()` is called with the decorator argument when the definition of `add()` is executed. It returns the decorator which takes `add` as an argument and returns the wrapper function. The wrapper function can access `text` through the enclosing scope and receives the arguments `2` and `3` when we call `add()`.

Using `@message("Calling add")` works similar to writing `add = message("Calling add")(add)` after defining `add()` without the decorator. If we use multiple decorators on a function, the decorators are applied from bottom to top.
