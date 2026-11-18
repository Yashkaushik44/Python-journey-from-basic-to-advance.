#                                                                                         File handling in Python
---
# Reading and writing Text Files

## Opening a file 

To work on a file we need to first open a file in a operating mode like `r, w, a, r+, w+, a+`.

```python
#syntax

file = open("filename.txt", "mode") # This is an old method and very unsafe

file.close()
```

### Issues with opening file with the old method

If you don't close the file the following issues can happen:-

- Data loss:- After the program is exited all the data in the buffer will be lost including the data in the file.

- Resource Exhaustion:- Each open file holds a file descriptor. The OS limits how many a process can hold. In a long running program opening files without closing them will eventually hit that limit and raise.

Because of the above issues we prefer the newer method. 

# Opening a file with `with`

This is the newer method of opening a file because it does not require to manually close the file. It automatically closes the file after the work is finished. 

```python 
#syntax

with open("filename.txt", "mode") as file_name:
```

## Reading in the file

We use `r` to read the file content.

```python
#example

with open("testfile.txt", "r") as test_file: # this opens the file in read mode
```

We use `r+` to read and write in the file at the same time. Read first then write.

**note**:- If the file does not exist or the file is not in the current directory then it will raise `FileNotFoundError`.
## Writing in the file

We use `w` to write in the file.

```python
#example

with open("testfile.txt", "w") as test_file:
```

We use `w+` to write and read in the file at the same time. Write first then read.

**note:-** When using `w or w+` mode the previous content is overwritten. If the file does not exist then it creates the file with the filename it was used to open.

## Appending in a file 

We use `a` to append in the file.

```python
#example

with open("testfile.txt", "a") as test_file:
```

We use `a+` to append and read in the file at the same time. Append first then read.

note:- It will append to the existing data in the file unlike the `w` method. If the file does not exist then it creates the file with the filename it was used to open.