#                                                                                         Dictionaries and Mutability in Python 
---

# Dictionaries: Keys, Values, and Key-Value Pairs

Dictionaries are used to store data values in key-value pairs. You can think of them like a real-life dictionary where a word (the key) has a specific meaning (the value). We use them to store related information together.

A dictionary is created using curly brackets `{}`. Inside, each key is connected to its value by a colon `:`. 

**Note:-** Dictionary keys must be unique and hashable (like strings or integers). The values, however, can be of any data type and can be duplicated.

```python
# Dictionary creation
student = {
    "name": "User",
    "age": 20,
    "course": "Python"
}

# Accessing dictionary values using keys
print(student["name"]) # output: User

# Adding a new key-value pair
student["grade"] = "A"

# Modifying an existing key-value pair
student["age"] = 21

print(student) # output: {'name': 'User', 'age': 21, 'course': 'Python', 'grade': 'A'}
```

---

# Dictionary Methods

Python provides several built-in methods to work with dictionaries easily. 

- `get()`
	This retrieves a value using a key. The main difference between using square brackets `[]` and `get()` is how they handle missing keys. If a key is missing, `[]` gives an error, but `get()` safely returns `None`.

- `update()`
	This adds new key-value pairs to the dictionary or modifies existing ones if the key already exists.

- `pop()`
	This removes a specific key-value pair and returns its value. If the key is missing, it will throw an error.

- `keys()`
	This retrieves a list-like object containing all the keys in the dictionary.

- `items()`
	This retrieves a list-like object containing all the key-value pairs as tuples.

```python
data = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Using get()
print(data.get("model")) # output: Mustang
print(data.get("color")) # output: None (No error is thrown)

# Using update()
data.update({"color": "Red", "year": 2020})
print(data["year"]) # output: 2020

# Using pop()
removed_value = data.pop("brand")
print(removed_value) # output: Ford

# Using keys()
print(data.keys()) # output: dict_keys(['model', 'year', 'color'])

# Using items()
print(data.items()) # output: dict_items([('model', 'Mustang'), ('year', 2020), ('color', 'Red')])
```

---

# Nested Lists, Tuples, Sets, and Dictionaries

Nested data structures are simply data structures stored inside other data structures. We use them to organize complex data.

- **Nested lists:** A list inside another list.
- **Nested tuples:** A tuple inside another tuple.
- **Nested dictionaries:** A dictionary inside another dictionary.
- **Nested sets:** A set inside another set. 

**Warning :-** Sets cannot contain mutable (unhashable) elements like lists, dictionaries, or even other standard sets. They can only contain immutable structures like tuples.

To access nested elements, we just chain the brackets one after another.

```python
# Nested List
numbers = [1, 2, [3, 4, 5]]
print(numbers[2][0]) # output: 3

# Nested Dictionary
students = {
    "student1": {"name": "Alice", "age": 22},
    "student2": {"name": "Bob", "age": 24}
}
print(students["student2"]["name"]) # output: Bob

# Combining different data structures
mixed_data = {
    "fruits": ["Apple", "Banana"],
    "coordinates": (10.5, 20.0)
}
print(mixed_data["fruits"][1]) # output: Banana

# Nested Set using tuples (since lists are not allowed inside sets)
unique_pairs = {(1, 2), (3, 4)}
print(unique_pairs) # output: {(1, 2), (3, 4)}
```

---

# Mutable vs. Immutable Objects

In Python, every piece of data is an object. The type of object determines if its internal state can be changed after it is created.

- **Mutable objects:** These are objects whose values can be changed after they are created. Examples include lists, dictionaries, and sets.
- **Immutable objects:** These are objects whose values cannot be changed once created. Examples include integers, floats, strings, booleans, and tuples.

Modifying a mutable object changes the original data. Reassigning a variable is different; it simply points the variable name to a completely new value.

**Note:-** While a tuple itself is immutable, if it contains a mutable object (like a list), that specific list inside the tuple can still be modified.

```python
# Modifying a mutable object (List)
fruits = ["Apple", "Mango"]
fruits[0] = "Orange" # This modifies the original list
print(fruits) # output: ['Orange', 'Mango']

# Reassigning an immutable object (String)
name = "User"
# name[0] = "L" # This would cause an error because strings are immutable
name = "Loser" # This creates a completely new string and reassigns the variable
print(name) # output: Loser

# Immutable tuple containing a mutable list
my_tuple = (1, 2, [3, 4])
my_tuple[2][0] = 99 # We can change the list inside the tuple
print(my_tuple) # output: (1, 2, [99, 4])
```