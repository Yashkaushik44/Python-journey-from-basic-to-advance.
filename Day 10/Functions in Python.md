
#                                                                                                    FUNCTIONS in Python

---

# Introduction to functions

A function is a block of code that has a name and runs only when we call it.

# Why do we use functions?

We use functions to reuse the same code again and again without writing it every time.

---

# def keyword and function call

We use the `def` keyword to define (make) a function. The code inside the function is called the function body and it must be indented.

Defining a function does not run it. The function runs only when we call it by writing its name followed by `()`.

```python
#this is the syntax for a function. The <> symbol are used for input and should not be considered a syntax.

def <function_name>():

	<function_body>

<function_name>() #function call
```

```python
#example

def greet():

	print("Hello") #output: Hello
	print("Welcome to Python") #output: Welcome to Python

greet() #function call
greet() #we can call the function as many times as we want
```

**Note:-** Indentation decides which code is inside the function. The code that is not indented is outside the function.

How the code runs:-

- Python reads the `def` and stores the function, but does not run the body.
- When the function is called, Python goes inside the function and runs the body line by line.
- After the body ends, Python comes back and continues with the next line after the call.

```python
def greet():

	print("Inside the function")

print("Before the call") #output: Before the call

greet() #output: Inside the function

print("After the call") #output: After the call
```

---

# Parameters vs Arguments

- Parameters are the variables written inside the `()` while defining a function. They work as placeholders for the values the function will receive.
    
- Arguments are the actual values we pass inside the `()` while calling a function.
    

```python
def add(a, b): #a and b are parameters

	print(a + b)

add(5, 3) #5 and 3 are arguments, output: 8
```

When the function is called, the first argument is stored in the first parameter, the second argument in the second parameter and so on. In this case `a` becomes `5` and `b` becomes `3`.

```python
def introduce(name, age): #name and age are parameters

	print("My name is", name, "and I am", age, "years old")

introduce("Yash", 20) #output: My name is Yash and I am 20 years old
introduce("Rahul", 21) #output: My name is Rahul and I am 21 years old
```

**Note:-** The number of arguments should match the number of parameters, otherwise Python gives an error.

---

# Positional, Keyword and Default arguments

# Positional arguments

In positional arguments, the values are matched with the parameters according to their position (order).

```python
def introduce(name, age):

	print(name, age)

introduce("Yash", 20) #output: Yash 20

introduce(20, "Yash") #output: 20 Yash, the order is changed so the values go in the wrong parameters
```

# Keyword arguments

In keyword arguments, we write the parameter name with the value (`<parameter>=<value>`), so the order does not matter.

```python
def introduce(name, age):

	print(name, age)

introduce(age=20, name="Yash") #output: Yash 20
```

# Default arguments

A default argument is a parameter that has a default value. If we do not pass an argument for it, the default value is used.

```python
#this is the syntax for default arguments.

def <function_name>(<parameter>=<default_value>):

	<function_body>
```

```python
def greet(name, message="Hello"): #message has a default value

	print(message, name)

greet("Yash") #output: Hello Yash
greet("Yash", "Good morning") #output: Good morning Yash, the default value is replaced
```

# Rules

- Positional arguments must come before keyword arguments in a function call.

```python
def introduce(name, age):

	print(name, age)

introduce("Yash", age=20) #correct, output: Yash 20

introduce(name="Yash", 20) #error: positional argument follows keyword argument
```

- Parameters with default values must come after parameters without default values in a function definition.

```python
def greet(message="Hello", name): #error: non-default parameter follows default parameter

	print(message, name)
```

- We cannot give multiple values to the same parameter.

```python
def introduce(name, age):

	print(name, age)

introduce("Yash", name="Rahul") #error: multiple values for argument 'name'
```