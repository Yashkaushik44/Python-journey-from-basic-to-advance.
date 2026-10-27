
#                                                                                               Python syntax and fundamentals
---

# Print():- 

## Hello world!

To print a statement in python, we use `print()` function. As the name suggest the `print()` function is very self explanatory, it does what it says.

```python
print("Hello World!")
```

	The name of "" symbol is double quotes.
	
When printing words we have to enclose them in  `""`, this is the syntax for printing a word through the print statement. Everything enclosed in `""` will be printed as it is.

---

# What is \n ?

`\n` stands for escape sequence that moves the cursor or text to the next line. In this syntax `\` is a escape character and it is used to give certain character special meaning inside a string.

---

# sep and end

### sep

sep stands for separate. It is used in python print statement to separate two different objects. 

```python
#Example:-

print("Hello", "World", sep=" ") #output Hello World
```

In the above example the two words Hello and World are being separated by a backspace.


### end

end stands for ending and like the name suggests it is used to when you want to add something at the end of your output. 

```python 
#Example:-

print("This is my python journey", end="!") #output This is my python journey!
```

In the above example `!` was added at the end. By default the print statement adds `\n` in the end.

---
# Single and multi line comments

### Why to use comments?

Comments are used to write text in the code, it is mainly used to explain and describe a code block. 

```python
#This is a single line comment 
```

note:- A single line comment is best used to give a quick one line summary of a specific code.

```python
'''
This is a multi line code
'''
```

Unlike single line comment, multi line comments are enclosed between triple quotes(''').

note:- Multi line comments are best used to describe a long summary, function, specify instruction or add long notes in the code file.

---
# Variable

Variable's in python are the same as variable's in maths. Variable can be visualise as an empty box where you can store anything you want.

### Rules for creating a variable

There are some rules to create a variable in python.

- Variable name can only start from alphabets and `_`
- Variable name can not contain whitespace and special characters except `_` 
- Variable name cannot be a keyword

```python
#example of a variable

num_1 = 3
```

---

# Input 

By using `input()` function we can ask the user for their input and store it in a variable.

```python 
#syntax

name = input("Enter your name: ")
```

The above line of code will prompt the user for their name and then store it in the `name` variable.

---

# Keywords

Keywords are reserved words in python that have predefined meaning and cannot be used as variables and identifiers. 

There are 33 keywords in python.

You can use the below code in your VS Code or any other IDE to check all the keywords in python.

```python
import keyword

print(keyword.kwlist)

'''
output

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

''' 
```

---

# Data types

Data types define the type of value a variable can store.

**There are mainly four types of data types**:-

1. Integer :- every non decimal number. It can be negative, positive and zero.
2. Float :- every decimal number. It can be negative, positive and zero. It can even be 1.0, 0.0, 5.0, -9.0 and etc.
3. String:- It is a sequence of alphabets or characters enclosed in quotes(""). example:- "Hello World!"
4. Boolean:- They are True and False value.

```python
num_1 = 4 # integer

num_2 = 4.1 # float

name = "User121" #string

# Below are boolean value.
learning = True

rest = False 
```

