#                                                                    List, set and dictionary Comprehensions

---

# List Comprehension

It is a short, single line way to create a new list by looping through items and applying a rule using square brackets.

```python
#example

numbers = [1, 2, 3, 4]

squares = [x * x for x in numbers] #output: a list of all the squared numbers in numbers list. [1, 4, 9, 16]
```

---

# Set Comprehension

Works same as List Comprehension but it uses curly braces instead to create a set that automatically removes duplicate values.

```python

#example

numbers = [1, 2, 2, 3, 3, 3]

unique_numbers = {x for x in numbers} # output: {1, 2, 3}
```

---

# Dictionary Comprehension

It is a quick one line way to build to a dictionary by creating key value pairs inside curly braces.

```python
#example

numbers = [1, 2, 3]

square_dict = {f"square of {x} is" : x * x for x in numbers} # output: {'square of 1 is': 1, 'square of 2 is': 4, 'square of 3 is': 9}
```