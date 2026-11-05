
#                                                                                         Python Strings and Built-in Functions

---

# Python Built-in Functions

Built-in functions are functions that are already available in Python, we don't have to import or create them. We just call them by their name.

**Note:-** A function is called on its own like `print()`, whereas a method belongs to a data type and is called using a dot like `name.upper()`. We will see methods in the string topics.

---

## enumerate()

`enumerate()` gives us both the index and the value while looping over an iterable (list, string, etc.). We use it when we need the position of an item along with the item itself.

```python
#syntax

enumerate(iterable, start=0)
```

```python
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

'''
output

0 apple
1 banana
2 mango
'''
```

By default the index starts from `0`. We can change this using the optional `start` parameter.

```python
fruits = ["apple", "banana", "mango"]

for number, fruit in enumerate(fruits, start=1):
    print(number, fruit)

'''
output

1 apple
2 banana
3 mango
'''
```

---

## zip()

`zip()` combines elements of two or more iterables, the first elements are paired together, then the second elements and so on. It returns an iterator of tuples, so we convert it into a list using `list()` to see the result.

```python
#syntax

zip(iterable1, iterable2, ...)
```

```python
names = ["Aman", "Riya", "Karan"]
marks = [85, 92, 78]

for name, mark in zip(names, marks):
    print(name, mark)

'''
output

Aman 85
Riya 92
Karan 78
'''

print(list(zip(names, marks))) # [('Aman', 85), ('Riya', 92), ('Karan', 78)]
```

If the iterables have different lengths, `zip()` stops at the shortest one. The extra elements of the longer iterable are ignored.

```python
numbers = [1, 2, 3]
letters = ["a", "b"]

print(list(zip(numbers, letters))) # [(1, 'a'), (2, 'b')]
```

In the above example `3` was ignored because `letters` has only two elements.

---

## reversed()

`reversed()` goes through an iterable in reverse order, from the last element to the first. It returns a reverse iterator, not a list.

```python
#syntax

reversed(sequence)
```

```python
numbers = [1, 2, 3, 4]

rev = reversed(numbers)

print(rev)       # <list_reverseiterator object at 0x...>
print(list(rev)) # [4, 3, 2, 1]
print(numbers)   # [1, 2, 3, 4]
```

The first print shows an iterator object, so we use `list()` to see its values. The original `numbers` list is not changed.

**Note:-** An iterator can be used only once. After we go through it, it becomes empty.

---

## sorted()

`sorted()` returns a new sorted list from the items of an iterable. The original iterable is not modified.

```python
#syntax

sorted(iterable, reverse=False)
```

```python
numbers = [5, 2, 9, 1]

print(sorted(numbers))                # [1, 2, 5, 9]
print(sorted(numbers, reverse=True))  # [9, 5, 2, 1]
print(numbers)                        # [5, 2, 9, 1]
```

By default `sorted()` sorts in ascending order. We use `reverse=True` for descending order.

**Note:-** `sorted()` always returns a list, even if we give it a string.

```python
print(sorted("python")) # ['h', 'n', 'o', 'p', 't', 'y']
```

---

# Introduction to Strings

## What is a string?

A string is a sequence of characters (letters, numbers, symbols, spaces) enclosed in quotes. We use strings to store and work with text like names, messages and sentences.

```python
name = "Python"

print(name)       # Python
print(type(name)) # <class 'str'>
```

## Single, double and triple quotes

We can create a string using single quotes `' '`, double quotes `" "` or triple quotes `''' '''` / `""" """`.

```python
name1 = 'Python'
name2 = "Python"

message = """This is a
multi line string"""

print(message)

'''
output

This is a
multi line string
'''
```

- Single and double quotes work the same way and are used for one line strings.
- Triple quotes are used for strings that span multiple lines.

**Note:-** If our text contains a single quote, we can enclose it in double quotes.

```python
sentence = "It's a nice day"
```

---

## String Indexing

Every character in a string has a position number called an index. We can use the index inside `[]` to get a single character.

### Positive indexing

Positive indexing starts from `0` at the first character and moves forward.

```python
name = "Python"

#  P  y  t  h  o  n
#  0  1  2  3  4  5

print(name[0]) # P
print(name[3]) # h
print(name[5]) # n
```

### Negative indexing

Negative indexing starts from `-1` at the last character and moves backward.

```python
name = "Python"

#   P   y   t   h   o   n
#  -6  -5  -4  -3  -2  -1

print(name[-1]) # n
print(name[-2]) # o
print(name[-6]) # P
```

**Warning :-** Using an index that does not exist gives an `IndexError`.

```python
name = "Python"

print(name[6]) # IndexError: string index out of range
```

---

# String Slicing and Immutability

## String Slicing

Slicing is used to get a part of a string instead of a single character. We use it when we need a portion of the text, like the first few letters or the last word.

```python
#syntax

string[start:stop:step]
```

- `start` is the index where the slice begins. It is included. Default is `0`.
- `stop` is the index where the slice ends. It is **excluded**. Default is the end of the string.
- `step` decides how many characters to move each time. Default is `1`.

```python
text = "Programming"

#  P  r  o  g  r  a  m  m  i  n  g
#  0  1  2  3  4  5  6  7  8  9  10

print(text[0:4])  # Prog
print(text[:3])   # Pro
print(text[3:])   # gramming
print(text[-3:])  # ing
```

In `text[0:4]` the characters at index `0, 1, 2, 3` are taken. Index `4` is not included because the stop index is excluded.

### Slicing with a step

```python
text = "Programming"

print(text[::2])   # Pormig
print(text[2:8:2]) # orm
```

In `text[::2]` we take every second character, so the indexes are `0, 2, 4, 6, 8, 10`.

### Reversing a string

A negative step moves backward. Using `-1` as the step reverses the string.

```python
text = "Programming"

print(text[::-1]) # gnimmargorP
```

**Note:-** Slicing never gives an `IndexError` if the range is too big, it just returns whatever is available.

---

## String Immutability

Immutable means cannot be changed. Strings in Python are immutable, so once a string is created we cannot change its characters directly.

```python
name = "Python"

name[0] = "J" # TypeError: 'str' object does not support item assignment
```

To get a modified string, we have to create a new string and store it in a variable.

```python
name = "Python"

new_name = "J" + name[1:] # we are joining "J" with everything after the first character

print(new_name) # Jython
print(name)     # Python
```

The original string `name` is still the same, we created a completely new string.

---

# String Methods

A method is a function that belongs to a data type and is called using a dot, like `string.method()`.

**Note:-** String methods do not change the original string because strings are immutable. They return a new value, so we have to store it in a variable if we want to use it.

---

## strip()

`strip()` removes the whitespace (spaces, tabs, new lines) from the start and the end of a string. The spaces in the middle are not removed.

```python
text = "   hello world   "

result = text.strip()

print(f"[{result}]") # [hello world]
```

- `lstrip()` removes whitespace only from the left (leading) side.
- `rstrip()` removes whitespace only from the right (trailing) side.

```python
text = "   hello   "

print(f"[{text.lstrip()}]") # [hello   ]
print(f"[{text.rstrip()}]") # [   hello]
```

---

## replace()

`replace()` replaces every occurrence of a substring with another substring.

```python
#syntax

string.replace(old, new, count)
```

`count` is optional. It decides how many occurrences will be replaced.

```python
text = "I like Java"

print(text.replace("Java", "Python")) # I like Python

word = "banana"

print(word.replace("a", "o"))    # bonono
print(word.replace("a", "o", 2)) # bonona
```

---

## find()

`find()` gives the index of the first occurrence of a substring. If the substring is not found, it returns `-1`.

```python
#syntax

string.find(substring)
```

```python
text = "hello world"

print(text.find("world"))  # 6
print(text.find("o"))      # 4 (first occurrence only)
print(text.find("python")) # -1
```

---

## split()

`split()` breaks a string into parts and returns them as a list.

```python
#syntax

string.split(separator)
```

The `separator` is optional. If we don't give one, the string is split at whitespace.

```python
sentence = "I love python"

print(sentence.split()) # ['I', 'love', 'python']

data = "apple,banana,mango"

print(data.split(",")) # ['apple', 'banana', 'mango']
```

---

## join()

`join()` joins the elements of an iterable into a single string. It is the opposite of `split()`.

```python
#syntax

separator.join(iterable)
```

The separator is written before `.join()` because `join()` is a string method. The string it is called on is the one that goes between the elements.

```python
words = ["Python", "is", "fun"]

print(" ".join(words)) # Python is fun
print("-".join(words)) # Python-is-fun
print("".join(words))  # Pythonisfun
```

**Warning :-** `join()` only works when all the elements are strings. A list like `[1, 2, 3]` gives a `TypeError`.

---

# String Formatting

String formatting is used to put values of variables inside a string. Python has three ways to do it.

---

## f-Strings

f-strings are the easiest way to put variables inside a string. We write `f` before the quotes and put the variable inside `{}`.

```python
#syntax

f"text {variable}"
```

```python
name = "Aman"
age = 20

print(f"My name is {name} and I am {age} years old.")

# output: My name is Aman and I am 20 years old.
```

We can also write expressions inside `{}`.

```python
a = 5
b = 3

print(f"{a} + {b} = {a + b}") # 5 + 3 = 8
```

We can control decimal places using `:.2f`.

```python
price = 49.5

print(f"Price: {price:.2f}") # Price: 49.50
```

---

## format()

The `format()` method replaces the `{}` placeholders in a string with the values given inside it.

```python
#syntax

"text {}".format(value)
```

```python
name = "Aman"
age = 20

print("My name is {} and I am {} years old.".format(name, age))

# output: My name is Aman and I am 20 years old.
```

The values are placed in order. We can also use index numbers to change the order.

```python
print("{1} is {0} years old.".format(age, name)) # Aman is 20 years old.
```

Named placeholders make the code easier to read.

```python
print("Name: {n}, Age: {a}".format(n=name, a=age)) # Name: Aman, Age: 20
```

---

## % Formatting

`%` formatting is the old way of formatting strings. We write a format specifier in the string and give the values after the `%` operator.

- `%s` is used for strings.
- `%d` is used for integers.
- `%f` is used for floats.

```python
name = "Aman"
age = 20
height = 5.8

print("My name is %s and I am %d years old." % (name, age))
# output: My name is Aman and I am 20 years old.

print("Height: %.1f" % height) # Height: 5.8
```

`%.1f` means one digit after the decimal point. By default `%f` shows six digits, so `"%f" % 3.5` gives `3.500000`.

**Note:-** f-strings are preferred in modern Python because they are shorter, easier to read and we can write the variable directly inside the string. With `%` and `format()` we have to keep track of the order of values separately.