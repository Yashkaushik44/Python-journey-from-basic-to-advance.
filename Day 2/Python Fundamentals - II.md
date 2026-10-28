
#                                                                                         Python Basics
---

# Dynamic Typing

Dynamic typing means Python determines the type of a variable automatically at runtime, so you don't have to declare its data type when creating it.

```python 
#example :-

num = 8

name = "User"

boolean = True

decimal = 4.3
```

In the above example we didn't had to specify the data type manually like in C or C++.

## Type

`type()`  used to check the type of a variable or a piece of data.

```python 

x = 4

print(type(x)) #output <class 'int'>

print(type(4.3)) #output <class 'float'>

```

---

# None

`None` is a special constant that represents the absence of a value.

```python
name = None #we specified none because there were no other values to store in the name variable so, we made an empty variable by storing None.

name = "User"

print(name) #output User
```

---

# Type casting/Type conversion 

In python, we can change the data type of a data to a different data type by using certain functions.

- int()
- float()
- str() 
- bool()

```python
'''Variable declaration'''

num1_integer = 4

num2_float = 4.23

string = "Hello"

boolean = True

'''Type casting'''

# Into int
print(int(num2_float))    # 4
# print(int(string))      # ValueError: "Hello" cannot be converted to int
print(int(boolean))       # 1

# Into float
print(float(num1_integer))  # 4.0
# print(float(string))      # ValueError: "Hello" cannot be converted to float
print(float(boolean))       # 1.0

# Into string
print(str(num1_integer))  # "4"
print(str(num2_float))    # "4.23"
print(str(boolean))       # "True"

# Into boolean
print(bool(num1_integer))  # True
print(bool(num2_float))    # True
print(bool(string))        # True

```

---
# Operators

## Arithmetic operators

Arithmetic operators are maths operators used to perform arithmetic calculations.

**The following operators are in descending priority order**

- `()`
	anything inside the brackets will be given the highest priority.
	
- `**`
	this is the operator for power 
	`
- `+x, -x`
	these are unary number's -> -5, +8.
	
- ` *,  /, //, %`
	`*` -> This is the operator symbol used for multiplication
	`/` -> This is the operator symbol used for float division. (It will always return float value)
	`//` -> This is the operator symbol used for int division. (It will always return the nearest integer towards negative infinity)
	`%` -> This is the operator used for getting the remainder after division (Modulo operator). 
	
- `+, -`
	`+` -> This is the operator used for addition.
	`-` -> This is the operator used for subtraction.

If the priority of a set of operators are same then they will be solved from left to right.

```python 
'''example code'''

num = (5 + 5) - 5 * 4 ** 2 % 2 / 2

print(num) #output 10.0
```

## Assignment operators 

operators used for assigning values to a variable.

- `=`
	This is used to assign a value equal to a variable.
	
- `-=` 
	This is used to assign a value to a variable after subtracting the variable to the value.
	example:- `num = num - 3` and `num -= 3` are the same thing.
	
- `+=` 
	This is used to assign a value to a variable after adding the variable to the value.
	example:- `num = num + 3` and `num += 3` are the same thing.
	
- `*=`
	This is used to assign a value to a variable after multiplying the variable to the value.
	example:- `num = num * 2` and `num *= 2` are the same thing.
	
- `/=` 
	This is used to assign a value to a variable after float dividing the variable to the value.
	example:- `num = num / 2` and `num /= 2` are the same thing.
	
- `//=`
	This is used to assign a value to a variable after int dividing the variable to the value.
	example:- `num = num // 2` and `num //= 2` are the same thing.
	
- `%=`
	This is used to assign a value to a variable after getting the remainder of their division.
	example:- `num = num % 2` and `num %= 2`.


## Comparison Operators

Operators used to compare two values and return a Boolean result.

- `==`
	This checks if the left side value is equal's to the right side value.
	
- `!=`
	This checks if the left side value is **not equal's** to the right side value.
	
- `>` 
	This checks if the left side value is greater than the right side value.
	
- `<`
	This checks if the **right side** value is greater than the left side value,
	
- `>=` 
	This checks if the left side value is greater or equal to the right side value.
	
- `<=`
	This checks if the **right side** value is greater or equal to the left side value.



