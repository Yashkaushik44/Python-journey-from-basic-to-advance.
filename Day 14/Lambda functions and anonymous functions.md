
#                                                                          Lambda Functions and Anonymous Functions

---

# Lambda function

It is used to implicitly return a result without using an explicit `return` statement or multi-line code block.

 `syntax-`
 
`lambda parameters: expression`

```python
#example is created by using min() built in function

people = {"Rahul" : 25, "Ansh" : 19, "Yash" : 18, "Lakshay" : 17}

youngest = min(people, key = lambda person: people[person]) #lambda functon extract the age of all the people
print(youngest) #output : Lakshay
```
---
# Anonymous Function(Lambda Function)

A function defined without using def keyword. It is used for temporary inline use or passed directly as an argument.

```python
#this example is given by using filter() built in function

numbers = [1,2,3,4,5]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)
```

filter() is a built in function which is used to extract specific data from list, tuple or set that satisfy a specific condition ignoring the rest.

**note** :- Lambda function and anonymous functions are same.