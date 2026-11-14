#                                        Generator expressions and Nested Comprehensions in Python

---

# Generator Expressions

Creates items one by one only when you actually ask for them, saving computer memory compared to building a full list upfront.

```python
#example

squares = (x * x for x in range(5)) # generates on demand
```

---

# Nested Comprehensions

A compact way to put one loop inside another on a single line, usually to flatten a list of lists into one simple list.

```python
flat = [num for row in [[1,2], [3,4]] for num in row] #output: [1, 2, 3, 4]
```

---

# map(), filter(),  any() and all()

- map()  :- Takes a rule(function) and applies that exact same change to every single item in a list. 
	```python
	doubled = list(map(lambda x : x * 2, [1, 2, 3])) #output: [2, 4, 6]
	```
	
- filter():- Tests every item in a list and keeps only the ones that pass True/False condition.
	```python
	evens = list(filter(lambda x : x % 2 == 0, [1, 2, 3, 4])) #output: [2, 4]
	```
	
- any():- Checks a group of items and returns `True` if at least one of them is true.
	```python
	winner = any([False, False, True]) #output: True
	```
	
- all() :- Checks a group of items and returns `True` only if every single one  of them is true.
	```python
	ready = all([True, True, False]) #output: False
	```