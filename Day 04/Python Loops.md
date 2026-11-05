
#                                                                                       LOOPS and membership operators

---

# Membership operators

We use members operators to check if a particular value exists in a sequence, such as strings.

**There are two membership operators**:-

- `in`
	used to check if a value exists in a sequence like string.
	
- `not in
	used to check if a value does not exist in a sequence.


---
# Why do we use loops?

We use loops to automate repetitive tasks.

---

# for loop, iterator  and range() function

We use `for` loop to repeat a block of code for a fixed number of times or go through each item in a sequence.

`for` loop is finite loop and need a certain range to work, we use `range()` function for setting the range of the loop.

For accessing elements of a sequence one at a time we use loop initialised variable called iterators .  They are made when initialising the for loop and only exists in the loop.

```python
#this is the syntax for for loop. The <> symbol are used for input and should not be considered a syntax.

for <iterator> in range(<starting>, <ending>, <step>): #the loops works until ending - 1

	<code_block>
```

```python
#example

for i in range(1,10,2): 

	print(i) #output 1,3,5,7,9
```

**Note:-** The loop only work until  `<ending>`- 1.

In loop, starting is inclusive and ending is exclusive. 

`<step>` decides how much the number changes after each repetition of the loop. In this case, a step of `2` increases the number by 2 each time.

---

# while loop

While loop is used to repeat a code until the condition is True.
While loop are infinite loops and are based on conditions.

```python
#this is the syntax for while loop. The <> symbol are used for input and should not be considered a syntax.
while <condition>: 

	<code_block>
```

```python
num = 5

while num > 0:
	
	print(num) # output: 5, 4, 3, 2, 1
	
	num -= 1 # this subtract one from num everytime the loop works.
```

