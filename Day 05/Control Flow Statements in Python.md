
#                                                                                          Control Flow Statements in Python with Practice Exercise
---

# Break 

Break keyword is used in python to exit a loop instantly and move forward to the next statement. 

```python
for i in range(1, 10):

	if i == 8:
	
		break
		
	else:
	
		print(i) 
```

In the above programme, the should ideally give number from 1 to 9 but we are using break when `i == 8` so, when the value of `i` becomes `8` the code will terminate.

---

# Continue

Continue is used to skip iteration and moves to the next iteration of the loop.

```python 
for i in range(1, 10):

	if i == 7:
	
		continue
		
	else:
	
		print(i) #output: 1,2,3,4,5,6,8,9
```

In the above code, ideally the output should have been numbers 1-9 but because of `if i == 7:` statement, the code will skip `7` and move forward.

---

# Pass

Pass function does nothing, it is only used as a placeholder when code is syntactically required but its logic is yet to be written.

```python
for i in range(1, 5):

	if i == 3:
	
		pass
		
	else:
	
		print(i)#output: 1,2,4
```

In the above code, we created an if condition but hasn't written it's logic yet, but to make it exist in the code without an error we used `pass`.

---

# Practice Exercises

1. ![Calc.py](calc.py)
2. ![Number_guessing_game.py](number_guessing_game.py)
3. ![simple_patterns.py](patterns.py)
