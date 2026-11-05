
#                                                                                                              Python lists, tuples and sets

---

# Lists

We use lists to store multiple values in a single variable. The values are stored in order and a list can have any data type in it.

For this we use square brackets `[]` and separate the values with commas.

```python
#this is the syntax for creating a list. We are using <> for getting your input in it and it is not a syntax

<list_name> = [<value1>, <value2>, <value3>]
```

**Note:-** Lists are mutable, which means you can change the values after creating the list.

example:-

```python
fruits = ["apple", "banana", "cherry", "mango", "orange"]

empty_list = [] #this creates an empty list

print(fruits) #output: ['apple', 'banana', 'cherry', 'mango', 'orange']
```

**Indexing:-**

Every value in a list has an index number which tells its position. Index starts from `0`, not from 1.

We can also use negative index to count from the end of the list. `-1` is the last value.

```python
fruits = ["apple", "banana", "cherry", "mango", "orange"]

print(fruits[0]) #output: apple, 0 is the first value

print(fruits[2]) #output: cherry

print(fruits[-1]) #output: orange, -1 is the last value

print(fruits[-2]) #output: mango
```

**Warning:-** If the index doesn't exist in the list, python will give an `IndexError`.

**Slicing:-**

Slicing is used to get a part of the list. It returns a new list.

```python
#this is the syntax for slicing. We are using <> for getting your input in it and it is not a syntax

<list_name>[<start> : <stop> : <step>]
```

- `start` is the index where the slice begins. It is included.
- `stop` is the index where the slice ends. It is not included.
- `step` is the number of values to jump. It is optional.

example:-

```python
fruits = ["apple", "banana", "cherry", "mango", "orange"]

print(fruits[1:4]) #output: ['banana', 'cherry', 'mango'], index 4 is not included

print(fruits[:2]) #output: ['apple', 'banana'], if start is not given it begins from 0

print(fruits[2:]) #output: ['cherry', 'mango', 'orange'], if stop is not given it goes till the end

print(fruits[::2]) #output: ['apple', 'cherry', 'orange'], takes every 2nd value
```

---

# List methods - append, extend, insert, remove

Methods are built-in functions that we use with a list to change it. We write them after the list name using a dot.

```python
#this is the syntax for using these methods. We are using <> for getting your input in it and it is not a syntax

<list_name>.append(<value>)

<list_name>.extend(<list>)

<list_name>.insert(<index>, <value>)

<list_name>.remove(<value>)
```

- `append()` adds one value at the end of the list.
- `extend()` adds all the values of another list at the end.
- `insert()` adds a value at the index we want.
- `remove()` removes the first matching value from the list.

example:-

```python
numbers = [1, 2, 3]

numbers.append(4) #adds 4 at the end
print(numbers) #output: [1, 2, 3, 4]

numbers.extend([5, 6]) #adds 5 and 6 one by one at the end
print(numbers) #output: [1, 2, 3, 4, 5, 6]

numbers.insert(1, 10) #adds 10 at index 1
print(numbers) #output: [1, 10, 2, 3, 4, 5, 6]

numbers.remove(10) #removes the value 10, not the index 10
print(numbers) #output: [1, 2, 3, 4, 5, 6]
```

**Note:-** `append()` adds the value you give as a single item, but `extend()` adds each item of the list separately.

```python
list1 = [1, 2]
list2 = [1, 2]

list1.append([3, 4]) #the whole list [3, 4] is added as one item
list2.extend([3, 4]) #3 and 4 are added separately

print(list1) #output: [1, 2, [3, 4]]
print(list2) #output: [1, 2, 3, 4]
```

**Warning:-** If the value is not in the list, `remove()` will give a `ValueError`. If the value is there more than once, only the first one is removed.

---

# List methods - pop, sort, reverse, copy

```python
#this is the syntax for using these methods. We are using <> for getting your input in it and it is not a syntax

<list_name>.pop(<index>)

<list_name>.sort()

<list_name>.reverse()

<list_name>.copy()
```

- `pop()` removes the value at the given index and also returns it. If we don't give an index, it removes the last value.
- `sort()` sorts the list from smallest to largest.
- `reverse()` reverses the order of the list.
- `copy()` creates a shallow copy of the list.

example:-

```python
numbers = [4, 1, 3, 2]

value = numbers.pop() #removes the last value and stores it in value
print(value) #output: 2
print(numbers) #output: [4, 1, 3]

value = numbers.pop(0) #removes the value at index 0
print(value) #output: 4
print(numbers) #output: [1, 3]
```

```python
numbers = [4, 1, 3, 2]

numbers.sort() #sorts the list from smallest to largest
print(numbers) #output: [1, 2, 3, 4]

numbers.sort(reverse=True) #sorts the list from largest to smallest
print(numbers) #output: [4, 3, 2, 1]

numbers = [4, 1, 3, 2]

numbers.reverse() #only flips the current order of the list
print(numbers) #output: [2, 3, 1, 4]
```

**Note:-** `sort()` arranges the values by their size, but `reverse()` only flips the order the list already has. Both of them change the original list and return `None`.

`copy()` creates a new separate list, so changing the copy will not change the original list.

```python
numbers = [1, 2, 3]

new_numbers = numbers.copy() #creates a separate copy
new_numbers.append(4)

print(numbers) #output: [1, 2, 3], the original list is not changed
print(new_numbers) #output: [1, 2, 3, 4]

same_numbers = numbers #this is not a copy, both variables point to the same list
same_numbers.append(99)

print(numbers) #output: [1, 2, 3, 99], the original list is also changed
```

---

# Tuples

A tuple is similar to a list but we cannot change it after creating it.

For this we use round brackets `()`.

```python
#this is the syntax for creating a tuple. We are using <> for getting your input in it and it is not a syntax

<tuple_name> = (<value1>, <value2>, <value3>)
```

example:-

```python
colors = ("red", "green", "blue")

empty_tuple = () #this creates an empty tuple

print(colors) #output: ('red', 'green', 'blue')

print(colors[0]) #output: red, indexing works the same as lists

print(colors[-1]) #output: blue
```

**Note:-** For a tuple with only one value, you have to put a comma after the value. Without the comma it is not a tuple.

```python
single = (5,) #this is a tuple
not_tuple = (5) #this is just an integer

print(type(single)) #output: <class 'tuple'>
print(type(not_tuple)) #output: <class 'int'>
```

**Immutability:-**

Immutable means we cannot change, add or remove the values of a tuple after creating it. We use tuples when we don't want the data to be changed by mistake.

```python
colors = ("red", "green", "blue")

colors[0] = "yellow" #this will give TypeError: 'tuple' object does not support item assignment
```

**Packing and unpacking:-**

Packing means putting multiple values in one tuple. Unpacking means taking the values out of a tuple and storing them in separate variables.

```python
person = "Yash", 20, "India" #packing, the brackets are optional here

print(person) #output: ('Yash', 20, 'India')

name, age, country = person #unpacking

print(name) #output: Yash
print(age) #output: 20
print(country) #output: India
```

**Warning:-** The number of variables must be equal to the number of values in the tuple, otherwise python will give a `ValueError`.

---

# Sets

A set is used to store multiple values, but it only stores unique values. It has no order and no index.

For this we use curly brackets `{}`.

```python
#this is the syntax for creating a set. We are using <> for getting your input in it and it is not a syntax

<set_name> = {<value1>, <value2>, <value3>}
```

**Note:-** Because sets have no order, we cannot use indexing like `numbers[0]` and the order of values can be different when you print a set.

**Uniqueness:-**

If a value is repeated, the set will keep only one of it.

```python
numbers = {1, 2, 2, 3, 3, 3}

print(numbers) #output: {1, 2, 3}, the duplicates are removed

numbers_list = [1, 2, 2, 3]

print(set(numbers_list)) #output: {1, 2, 3}, we can also convert a list into a set to remove duplicates
```

**Warning:-** An empty `{}` creates a dictionary and not a set. To create an empty set we have to use `set()`.

```python
empty_dict = {}
empty_set = set()

print(type(empty_dict)) #output: <class 'dict'>
print(type(empty_set)) #output: <class 'set'>
```

**Membership:-**

We use `in` and `not in` to check if a value is present in the set or not. It gives `True` or `False`.

```python
fruits = {"apple", "banana", "cherry"}

print("apple" in fruits) #output: True

print("mango" in fruits) #output: False

print("mango" not in fruits) #output: True
```

---

# Set operations

We use set operations to compare two sets and get a new set as the result.

**They are of 4 types:-**

- Union
- Intersection
- Difference
- Symmetric difference

```python
#this is the syntax for using set operations. We are using <> for getting your input in it and it is not a syntax

<set1> | <set2> #union, same as <set1>.union(<set2>)

<set1> & <set2> #intersection, same as <set1>.intersection(<set2>)

<set1> - <set2> #difference, same as <set1>.difference(<set2>)

<set1> ^ <set2> #symmetric difference, same as <set1>.symmetric_difference(<set2>)
```

- **Union** `|` gives all the values from both sets. The common values are not repeated.
- **Intersection** `&` gives only the values which are in both sets.
- **Difference** `-` gives the values which are in the first set but not in the second set.
- **Symmetric difference** `^` gives the values which are in one set but not in both.

example:-

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2) #output: {1, 2, 3, 4, 5, 6}

print(set1 & set2) #output: {3, 4}, only the common values

print(set1 - set2) #output: {1, 2}, values that are only in set1

print(set2 - set1) #output: {5, 6}, the order of sets matters in difference

print(set1 ^ set2) #output: {1, 2, 5, 6}, common values 3 and 4 are removed
```