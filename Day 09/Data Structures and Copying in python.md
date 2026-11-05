#                                                                                          Copying and Data Structures in Python with Practice Exercise
---

# Copying Objects

Copy module is used in python to duplicate objects instantly and move forward to the next statement. 

```python
import copy

original_list = [1, 2, 3]

new_list = copy.copy(original_list)

print(new_list) #output: [1, 2, 3]
```

In the above programme, the should ideally use assignment but we are using copy module when duplicating so, when the value of original changes the code will keep the new list safe.

---

# Shallow Copy

Shallow copy is used to copy the outer object and moves to insert references for the nested objects.

```python 
import copy

list1 = [[1, 2], [3, 4]]

list2 = copy.copy(list1)

list1[0][0] = 99

print(list2) #output: [[99, 2], [3, 4]]
```

In the above code, ideally the output should have been independent but because of `copy.copy` statement, the code will share nested mutable objects and move forward.

---

# Deep Copy

Deep copy function copies everything completely, it is only used as a deep duplicator when fully independent copies are syntactically required but its shared references are yet to be broken.

```python
import copy

list1 = [[1, 2], [3, 4]]

list2 = copy.deepcopy(list1)

list1[0][0] = 99

print(list2)#output: [[1, 2], [3, 4]]
```

In the above code, we created a nested list but hasn't written shared references, but to make it exist as a completely independent copy without an error we used `copy.deepcopy`.

---

# Lists

List keyword is used in python to store multiple items instantly and move forward to change them later. 

```python
my_list = [10, 20, 30]

my_list.append(40)

print(my_list) #output: [10, 20, 30, 40]
```

In the above programme, the should ideally keep three numbers but we are using append when adding items so, when the value of `40` is added the code will expand.

---

# Tuples

Tuple is used to store fixed data and moves to the next statement without allowing changes.

```python 
my_tuple = (10, 20, 30)

print(my_tuple[1]) #output: 20
```

In the above code, ideally the output should have been changeable but because of `()` brackets statement, the code will keep the data permanent and move forward.

---

# Sets

Set function removes duplicates automatically, it is only used as a collection when unique items are syntactically required but its specific order is yet to be determined.

```python
my_set = {10, 20, 20, 30}

print(my_set)#output: {10, 20, 30}
```

In the above code, we created a group with duplicates but hasn't written it's logic to filter them manually, but to make it unique in the code without an error we used `{}` set brackets.

---

# Dictionaries

Dictionary is used in python to store data in key-value pairs instantly and move forward to fast lookups. 

```python
my_dict = {"id": 101, "name": "John"}

print(my_dict["name"]) #output: John
```

In the above programme, the should ideally search through a list but we are using dictionary keys when looking up data so, when the key `"name"` is called the code will output the value.

---

# Choosing Data Structures

Choosing guide does nothing but helps you pick, it is only used as a reference when specific data management is syntactically required but its exact type is yet to be chosen.

1. Use Lists when data needs to change and order matters.
2. Use Tuples when data is fixed and should never change.
3. Use Sets when you need to remove duplicates instantly.
4. Use Dictionaries when fast lookups using keys are required.

---

# Data Structures Mini Project

Mini project is used to combine data structures and moves to the next iteration of the student system.

```python 
active_ids = {101, 102} 

school_subjects = ("Math", "Science") 

student_1 = {"id": 101, "name": "Alice"} 

all_students = [student_1] 

for student in all_students:

	if student["id"] in active_ids:
	
		print(student["name"]) #output: Alice
```
