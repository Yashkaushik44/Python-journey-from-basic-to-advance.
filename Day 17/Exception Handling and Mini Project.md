
#                                                                                 Exception Handling and Mini Project 

---

# Exception Handling

It is used to catch and handle know errors gracefully and preventing the program from crashing.

```python 
#Below is the syntax of error handling in Python. I used <> to insert and this should not be treated as syntax.

try: #tries the suspected code block

	<Code_Block>
	
except <suspected_error_type>: # runs if the code gives error

	<code_block>
	
finally: # will run no matter if the code gives error or not

	<code_block>
```

**Note:-** You need to use `try` and `except` as a pair but `finally` is not mandatory. Except block can be multiple but try and finally should only be one

```python
#example

try:

	denominator = int(input("Enter the denominator: "))
	
	print(10 / denominator)
	
except ValueError:
	
	print("Enter only integer value")
	
except ZeroDivisionError:

	print("Cannot divide by zero")
	
finally: 

	print("Thanks for using my notes!")
```

## Custom Exception (raise)

The raise statement lets you manually trigger an exception when a n invalid condition occurs in your code.

```python 
#example

def check_age(age):

    if age < 0:
    
        raise ValueError("Age cannot be negative!")
        
    return age

check_age(-1)
```

---

# Mini Project - Modular Calculator

![Modular Calculator Code](Modular_calculator.py)






