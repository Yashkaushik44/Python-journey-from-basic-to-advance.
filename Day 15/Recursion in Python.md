#                                                                                                     Recursion in Python
---

#  Recursion 

Calling a function in itself repetitively to perform a task is called recursion.

Recursion have two cases:-

- Base case
- Recursive call

---

# Base Case

The condition that terminates recursion by returning  a direct value without making further self-calls.

```python

def test(n);

	if n <= 1:
	
		return 1 #stops the calculaton here
```

**Warning :-** If no base case is specified at the time of recursion, the function will infinitely call itself. This case is called Infinite recursion. 

---

# Recursive call

The statement where a function calls itself with a reduced or modified argument to solve a smaller instance of the problem.

```python
def factorial(n):
	
	if n <= 1:
		
		return 1
		
	else:
	
		return n * factorial(n - 1) # this will keep repeating until the base case is met
```