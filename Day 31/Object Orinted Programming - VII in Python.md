#                                                                                              Generators in Python
---

# Generators, `yield` and Lazy Evaluation

Generators are used to generate values one at a time rather than generating and storing all the values at once. A generator function is a function which contains the `yield` keyword. When we call a generator function it returns a generator object without executing the code inside the function.

**`yield`** is used to return a value and pause the execution of the generator function. Unlike `return` which terminates the function, `yield` preserves the local variables and the state of the function so its execution can be continued from where it was paused.

```python
#example

def numbers():

	for i in range(3):

		yield i

a = numbers()

print(next(a)) #0
print(next(a)) #1

for i in a:

	print(i) #2
```

We can also use multiple `yield` statements in a generator function. If a `return` statement is executed inside the generator it terminates the generator without yielding the return value.

A generator object is an iterator but not every iterator is a generator. Once all the values are generated and the generator finishes its execution, calling `next()` raises `StopIteration`. We have to call the generator function again to create a new generator object.

**Lazy Evaluation** is used to delay the computation of a value until the value is required. Unlike eager evaluation where the values are computed beforehand, generators compute their values as we iterate over them. This allows us to generate finite or infinite sequences without having to store all the generated values in memory at once.

---

# `yield from` and Generator Expressions

**`yield from`** is used to yield values from another iterable or generator. Unlike `yield` which yields the iterable itself as a single value, `yield from` yields the individual values of that iterable.

```python
#example

def numbers():

	yield from [1, 2]
	yield 3

def values():

	yield from numbers()
	yield from (4, 5)

for i in values():

	print(i)
```

For yielding values, `yield from` works similar to a `for` loop containing a `yield` statement. Once the iterable is exhausted the execution of the outer generator continues. If we use `yield from` with another generator function, its return value can be stored using `value = yield from generator()` but that return value is not yielded.

Generator expressions are used to create generator objects using a syntax similar to list comprehensions but with parentheses instead of square brackets. Unlike list comprehensions they generate the resulting values one at a time instead of creating a list of all the values.

```python
#example

a = (i ** 2 for i in range(5) if i % 2 == 0)

print(next(a)) #0

for i in a:

	print(i) #4 and 16 on separate lines
```

The iterable in the first `for` clause is evaluated and its iterator is created when we create the generator expression. The remaining iteration, conditions and resulting values are evaluated as we iterate over the generator.

We can also use multiple `for` clauses in a generator expression. Once the generator is exhausted we cannot iterate over its values again. Functions like `sum()`, `min()` and `max()` can directly take a generator expression as an argument. If it is the only argument passed to the function we don't have to use an extra pair of parentheses.

```python
#example

print(sum(i for i in range(5))) #10
```
