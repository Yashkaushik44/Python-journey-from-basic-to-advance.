#                                                           File Handling - II in Python
---
# File and Directory Operations with `pathlib`

## What file and directory operations are

File and directory operations are actions performed on the file system to inspect, create, read, modify, move, or delete files and folders.

## Introduction to the `pathlib` module

`pathlib` is a built-in Python module that provides an object-oriented way to represent and work with file system paths.

```
#syntax

from pathlib import Path
```

### Why `pathlib` is useful compared with traditional path handling

Traditional path handling relies on string manipulation and the `os.path` module, which requires passing path strings into separate functions.

- `pathlib` represents paths as `Path` objects with built-in methods and properties.
    
- It automatically handles path separators across different operating systems like Windows (`\`) and Linux or macOS (`/`).
    
- It reduces errors caused by manual string concatenation.
    

## Creating a `Path` object

We create a `Path` object by passing a path string to `Path()`.

```
#example

from pathlib import Path

file_path = Path("data/notes.txt")
print(file_path)
```

```
#output

data/notes.txt
```

**note:-** Creating a `Path` object does not create the actual file or folder on the disk. It only creates an object representing the path.

## Relative and absolute paths

- **Relative path:-** A path that starts from the current working directory, such as `data/notes.txt`.
    
- **Absolute path:-** A complete path that starts from the root directory or drive letter, such as `/home/user/project/data/notes.txt` or `C:\Users\user\project\data\notes.txt`.
    

We use `resolve()` to convert a relative path into an absolute path.

```
#example

from pathlib import Path

rel_path = Path("data/notes.txt")
abs_path = rel_path.resolve()
print(abs_path)
```

## Accessing the current working directory and home directory

We use `Path.cwd()` to get the current working directory and `Path.home()` to get the current user's home directory.

```
#example

from pathlib import Path

print(Path.cwd())
print(Path.home())
```

```
#output

/home/user/project
/home/user
```

## Joining paths using `/`

`Path` objects override the `/` operator so we can join folders and filenames cleanly without worrying about operating system slashes.

```
#example

from pathlib import Path

base_dir = Path("project_files")
file_path = base_dir / "reports" / "summary.txt"
print(file_path)
```

```
#output

project_files/reports/summary.txt
```

## Accessing path components

A `Path` object provides attributes to extract different parts of a path:

- `name`:- Returns the final component of the path including the extension.
    
- `stem`:- Returns the filename without the extension.
    
- `suffix`:- Returns the file extension including the dot.
    
- `parent`:- Returns the directory containing the file or folder.
    

```
#example

from pathlib import Path

file_path = Path("project_files/reports/summary.txt")

print(file_path.name)
print(file_path.stem)
print(file_path.suffix)
print(file_path.parent)
```

```
#output

summary.txt
summary
.txt
project_files/reports
```

## Checking paths

Before performing operations on a path, we can check if it exists and whether it is a file or a directory.

- `exists()`:- Returns `True` if the path exists on the filesystem, otherwise `False`.
    
- `is_file()`:- Returns `True` if the path exists and is a file.
    
- `is_dir()`:- Returns `True` if the path exists and is a directory.
    

```
#example

from pathlib import Path

target = Path("data/notes.txt")

print(target.exists())
print(target.is_file())
print(target.is_dir())
```

## Creating directories using `mkdir()`

We use `mkdir()` to create a new directory.

```
#syntax

path_object.mkdir(parents=False, exist_ok=False)
```

- `parents=True`:- Creates any missing parent directories along the path. If `False`, missing parent folders will raise `FileNotFoundError`.
    
- `exist_ok=True`:- Prevents raising `FileExistsError` if the directory already exists.
    

```
#example

from pathlib import Path

folder = Path("project_files/logs/2026")
folder.mkdir(parents=True, exist_ok=True)
```

## Creating files

We can create an empty file using `touch()`, or create a file by writing content to it using `write_text()`.

```
#example

from pathlib import Path

new_file = Path("project_files/logs/2026/app.log")
new_file.touch(exist_ok=True) # creates an empty file if it does not exist
```

## Reading and writing text files with `pathlib`

`pathlib` provides direct methods to read and write text without manually calling `open()`.

### Writing text using `write_text()`

`write_text()` opens the file, writes the string, and closes the file automatically.

```
#example

from pathlib import Path

note_file = Path("project_files/notes.txt")
note_file.write_text("Hello Python\nLearning pathlib.", encoding="utf-8")
```

**note:-** `write_text()` overwrites existing file content just like opening a file in `w` mode.

### Reading text using `read_text()`

`read_text()` opens the file, reads all content as a single string, and closes the file automatically.

```
#example

from pathlib import Path

note_file = Path("project_files/notes.txt")
content = note_file.read_text(encoding="utf-8")
print(content)
```

```
#output

Hello Python
Learning pathlib.
```

### Understanding file encodings and UTF-8

Text files store characters as bytes using a character encoding. `utf-8` is the standard encoding that supports almost all characters and symbols across languages. Always specify `encoding="utf-8"` when reading or writing text files to avoid platform-specific decoding errors.

## Listing directory contents using `iterdir()`

We use `iterdir()` to loop through all immediate files and subdirectories inside a directory.

```
#example

from pathlib import Path

folder = Path("project_files")

for item in folder.iterdir():
    print(item.name)
```

```
#output

logs
notes.txt
```

## Finding files using `glob()` and `rglob()`

We use `glob()` to search for files matching a pattern in the current directory, and `rglob()` to search recursively through all subdirectories.

```
#example

from pathlib import Path

folder = Path("project_files")

# Find all .txt files in project_files only
for txt_file in folder.glob("*.txt"):
    print(txt_file)

# Find all .log files in project_files and all subfolders
for log_file in folder.rglob("*.log"):
    print(log_file)
```

```
#output

project_files/notes.txt
project_files/logs/2026/app.log
```

## Renaming and moving files using `rename()` and `replace()`

Both `rename()` and `replace()` can rename a file or move it to a different directory.

- `rename()`:- Renames or moves the file. On Windows, it raises `FileExistsError` if the destination file already exists.
    
- `replace()`:- Renames or moves the file and unconditionally overwrites the destination file if it already exists across all operating systems.
    

```
#example

from pathlib import Path

source = Path("project_files/notes.txt")
destination = Path("project_files/archive_notes.txt")

if source.exists():
    source.replace(destination) # renames notes.txt to archive_notes.txt safely
```

**note:-** Moving or renaming files alters the filesystem immediately. Always verify the source exists and check whether overwriting the destination is intended.

## Deleting files and directories

Operations for deleting files and directories use different methods and have different requirements:

- `unlink()`:- Deletes a single file or symbolic link. It cannot delete a directory.
    
- `rmdir()`:- Deletes a directory. The directory must be completely empty, otherwise it raises `OSError`.
    

```
#example

from pathlib import Path

target_file = Path("project_files/logs/2026/app.log")
if target_file.is_file():
    target_file.unlink() # deletes the file app.log

empty_folder = Path("project_files/logs/2026")
if empty_folder.is_dir():
    empty_folder.rmdir() # deletes the empty folder 2026
```

**note:-** Deleting files and directories with `unlink()` and `rmdir()` permanently removes them without sending them to the Recycle Bin or Trash.

## Common path-related errors and handling them

Common exceptions when working with paths include:

- `FileNotFoundError`:- Raised when trying to read, rename, or delete a file or folder that does not exist.
    
- `FileExistsError`:- Raised when creating a directory with `mkdir()` without `exist_ok=True` when it already exists.
    
- `IsADirectoryError`:- Raised when trying to perform a file operation like `read_text()` or `unlink()` on a directory.
    
- `PermissionError`:- Raised when the program lacks permission to access or modify a file or folder.
    

```
#example

from pathlib import Path

missing_file = Path("project_files/missing.txt")

try:
    text = missing_file.read_text(encoding="utf-8")
except FileNotFoundError:
    print("The requested file does not exist.")
```

```
#output

The requested file does not exist.
```

# Reading and Writing CSV and JSON Files

## CSV Files

### What CSV files are

CSV stands for Comma-Separated Values. It is a plain text format used to store tabular data where each line represents a row and values in a row are separated by a delimiter, usually a comma.

Sample file `students.csv`:

```
name,age,grade
Alice,20,A
Bob,22,B
```

### Common use cases of CSV files

- Exporting and importing spreadsheet data.
    
- Storing simple tabular datasets for data analysis.
    
- Transferring records between databases and applications.
    

### Introduction to Python's `csv` module

Python provides the built-in `csv` module to read and write CSV files properly, handling commas inside quotes and line endings automatically.

```
#syntax

import csv
```

### Opening CSV files and the `newline=""` argument

When opening a CSV file with `open()`, always pass `newline=""` along with `encoding="utf-8"`.

```
#syntax

with open("students.csv", "r", newline="", encoding="utf-8") as file:
```

**note:-** The `csv` module performs its own newline handling. If `newline=""` is omitted, blank lines may appear between rows when writing CSV files on Windows, or line endings inside quoted fields may be corrupted.

### Reading CSV files using `csv.reader()`

`csv.reader()` reads each row of the CSV file as a list of strings.

```
#example

import csv

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

```
#output

['name', 'age', 'grade']
['Alice', '20', 'A']
['Bob', '22', 'B']
```

### Reading CSV files using `csv.DictReader()`

`csv.DictReader()` uses the first row of the CSV file as headers (field names) and reads each subsequent row as a dictionary.

```
#example

import csv

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["grade"])
```

```
#output

Alice A
Bob B
```

### Writing CSV files using `csv.writer()`

We open the file in `w` mode and use `csv.writer()` to write lists as rows.

- `writerow()`:- Writes a single row to the CSV file.
    
- `writerows()`:- Writes multiple rows (a list of lists) at once.
    

```
#example

import csv

rows = [
    ["name", "age", "grade"],
    ["Charlie", 21, "A"],
    ["Diana", 23, "B"]
]

with open("new_students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(rows[0])     # writes header row
    writer.writerows(rows[1:])   # writes remaining data rows
```

Content of created file `new_students.csv`:

```
name,age,grade
Charlie,21,A
Diana,23,B
```

### Writing dictionaries to CSV files using `csv.DictWriter()`

`csv.DictWriter()` writes dictionaries to a CSV file. It requires the `fieldnames` parameter to define the column headers and order, and `writeheader()` to write the header row.

```
#example

import csv

fieldnames = ["name", "age", "grade"]
students = [
    {"name": "Charlie", "age": 21, "grade": "A"},
    {"name": "Diana", "age": 23, "grade": "B"}
]

with open("dict_students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)
```

### Handling delimiters

If a file uses a separator other than a comma, such as a semicolon (`;`) or tab (`\t`), pass the `delimiter` parameter to the reader or writer.

```
#example

import csv

with open("data_semicolon.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(row)
```

### Common CSV handling mistakes

- Forgetting `newline=""` inside `open()`, causing extra empty rows on Windows.
    
- Trying to split lines manually with `.split(",")`, which breaks when values contain commas inside quotes like `"Smith, John"`.
    
- Forgetting that `csv.reader()` reads all values, including numbers, as strings.
    

## JSON Files

### What JSON is

JSON stands for JavaScript Object Notation. It is a lightweight, human-readable text format used for storing and exchanging structured data.

Sample file `user.json`:

```
{
    "username": "alex_dev",
    "age": 25,
    "is_active": true,
    "skills": ["Python", "SQL"],
    "address": null
}
```

### Mapping JSON data types to Python data types

When Python reads or writes JSON, data types are converted between JSON and Python as follows:

- JSON `object` (`{}`) $\leftrightarrow$ Python `dict`
    
- JSON `array` (`[]`) $\leftrightarrow$ Python `list`
    
- JSON `string` (`"text"`) $\leftrightarrow$ Python `str`
    
- JSON `number` (`10`, `3.14`) $\leftrightarrow$ Python `int` or `float`
    
- JSON `true` / `false` $\leftrightarrow$ Python `True` / `False`
    
- JSON `null` $\leftrightarrow$ Python `None`
    

### Introduction to Python's `json` module

Python provides the built-in `json` module to work with JSON files and JSON strings.

```
#syntax

import json
```

### Reading JSON files using `json.load()`

`json.load()` reads JSON data from an open file object and converts it into a Python object.

```
#example

import json

with open("user.json", "r", encoding="utf-8") as file:
    user_data = json.load(file)

print(type(user_data))
print(user_data["username"])
print(user_data["skills"])
```

```
#output

<class 'dict'>
alex_dev
['Python', 'SQL']
```

### Writing JSON files using `json.dump()`

`json.dump()` converts a Python object into JSON format and writes it directly to an open file object.

- `indent`:- Formats the JSON output with the specified number of spaces for readability.
    
- `sort_keys`:- Sorts dictionary keys alphabetically when set to `True`.
    
- `ensure_ascii`:- When `True` (default), escapes non-ASCII characters like accented letters into `\uXXXX` sequences. Setting it to `False` writes the actual characters directly.
    

```
#example

import json

profile = {
    "username": "renée",
    "age": 28,
    "is_active": True,
    "skills": ["Python", "Git"]
}

with open("profile.json", "w", encoding="utf-8") as file:
    json.dump(profile, file, indent=4, sort_keys=True, ensure_ascii=False)
```

Content of created file `profile.json`:

```
{
    "age": 28,
    "is_active": true,
    "skills": [
        "Python",
        "Git"
    ],
    "username": "renée"
}
```

### Converting between Python objects and JSON strings (`dumps()` and `loads()`)

The functions ending with `s` operate on strings in memory rather than files:

- `json.dumps()`:- Converts a Python object into a JSON-formatted string.
    
- `json.loads()`:- Parses a JSON-formatted string into a Python object.
    

```
#example

import json

data = {"status": "ok", "count": 3}

# Python dict to JSON string
json_string = json.dumps(data)
print(type(json_string), json_string)

# JSON string back to Python dict
parsed_data = json.loads(json_string)
print(type(parsed_data), parsed_data["count"])
```

```
#output

<class 'str'> {"status": "ok", "count": 3}
<class 'dict'> 3
```

### Handling JSON parsing errors

If a file or string contains invalid JSON syntax (such as trailing commas or single quotes instead of double quotes), `json.load()` and `json.loads()` raise `json.JSONDecodeError`.

```
#example

import json

bad_json = '{"name": "Alex",}' # invalid trailing comma

try:
    result = json.loads(bad_json)
except json.JSONDecodeError as error:
    print("Invalid JSON format:", error)
```

```
#output

Invalid JSON format: Expecting property name enclosed in double quotes: line 1 column 17 (char 16)
```

### Python objects supported in JSON and common mistakes

JSON can only directly serialize `dict`, `list`, `tuple` (converted to JSON array), `str`, `int`, `float`, `bool`, and `None`.

Common mistakes when handling JSON:

- Trying to serialize unsupported Python objects like `set`, `datetime`, or custom class instances, which raises `TypeError`.
    
- Confusing `json.load()` (reads from a file) with `json.loads()` (reads from a string), or `json.dump()` (writes to a file) with `json.dumps()` (returns a string).
    
- Using single quotes in manual JSON strings; JSON requires double quotes for keys and strings.
    

## Difference between CSV and JSON

- **Structure:-** CSV stores flat, two-dimensional rows and columns. JSON stores nested, hierarchical key-value pairs and lists.
    
- **Data Types:-** CSV stores everything as plain text strings. JSON preserves numbers, booleans, `null`, arrays, and nested objects.
    
- **When to use CSV:-** Use CSV for simple tabular records, spreadsheets, and flat datasets where every row has the exact same columns.
    
- **When to use JSON:-** Use JSON for configuration files, nested data structures, API responses, and data exchanged between different programming languages.
    

# Serialization vs. Deserialization and Pickle Security

## What serialization and deserialization mean

- **Serialization:-** The process of converting an in-memory Python object into a format (such as a string or sequence of bytes) that can be saved to a file or transmitted over a network.
    
- **Deserialization:-** The reverse process of reading that stored or transmitted data and reconstructing the original Python object in memory.
    

### Why serialization is useful

- Saving program state, user sessions, or trained data structures to disk so they persist after the program stops.
    
- Sending structured data between different programs or across a network.
    

### Common serialization formats

- **JSON:-** A text-based, human-readable format supported across almost all programming languages.
    
- **Pickle:-** A Python-specific binary format used to serialize Python objects.
    

## Introduction to Python's `pickle` module

`pickle` is a built-in Python module that converts Python objects into a byte stream and reconstructs them back into Python objects.

```
#syntax

import pickle
```

**note:-** Unlike JSON, Pickle produces binary data (bytes), not human-readable text. Files used with Pickle must be opened in binary modes: `wb` for writing bytes and `rb` for reading bytes.

## Serializing and deserializing with files (`dump()` and `load()`)

- `pickle.dump()`:- Serializes a Python object and writes the bytes to an open binary file.
    
- `pickle.load()`:- Reads bytes from an open binary file and deserializes them back into a Python object.
    

```
#example

import pickle

session_data = {
    "user_id": 101,
    "roles": {"admin", "editor"}, # sets are supported by pickle
    "scores": (95, 88, 92)
}

# Serialize to a binary file
with open("session.pkl", "wb") as file:
    pickle.dump(session_data, file)

# Deserialize from the binary file
with open("session.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)
print(type(loaded_data["roles"]))
```

```
#output

{'user_id': 101, 'roles': {'admin', 'editor'}, 'scores': (95, 88, 92)}
<class 'set'>
```

## Converting objects to bytes in memory (`dumps()` and `loads()`)

- `pickle.dumps()`:- Serializes a Python object into a `bytes` object in memory.
    
- `pickle.loads()`:- Deserializes a `bytes` object back into a Python object.
    

```
#example

import pickle

numbers = [10, 20, 30]

raw_bytes = pickle.dumps(numbers)
print(type(raw_bytes))

restored_numbers = pickle.loads(raw_bytes)
print(restored_numbers)
```

```
#output

<class 'bytes'>
[10, 20, 30]
```

## Supported Python types and limitations of Pickle

- Pickle can serialize almost any built-in Python type (including `set`, `tuple`, `complex`, and `bytes`), as well as functions and instances of custom classes defined at the top level of a module.
    
- **Python-specific:-** Pickle is strictly specific to Python. Other programming languages cannot read Pickle files.
    
- **Version compatibility:-** Pickle files created in newer Python versions may not load in older Python versions, and changes to custom class definitions can break deserialization of older Pickle files.
    
- **Not human-readable:-** You cannot inspect or edit a `.pkl` file in a standard text editor.
    

## Comparing JSON and Pickle

- **Readability:-** JSON is human-readable text; Pickle is binary bytes.
    
- **Language Support:-** JSON is language-independent; Pickle works only in Python.
    
- **Supported Types:-** JSON supports basic types (`dict`, `list`, `str`, `int`, `float`, `bool`, `None`); Pickle supports almost all Python types including `set`, `tuple`, and custom objects.
    
- **Security:-** JSON is safe to parse from untrusted sources; Pickle is unsafe if the data comes from an untrusted source.
    

## Security risks of Pickle

**note:-** The `pickle` module is **not secure**. Never unpickle data received from an untrusted, unauthenticated, or tampered source.

### Why malicious Pickle data can execute arbitrary code

Unlike JSON, which only stores passive data values, the Pickle format acts like a mini stack-based instruction language that tells Python how to reconstruct objects by calling functions and class constructors.

Because deserialization executes embedded reconstruction instructions automatically during `pickle.load()` or `pickle.loads()`, a crafted or tampered Pickle byte stream can trigger arbitrary Python code execution on your machine before the function even returns. Storing Pickle data in a local file does not make it safe if that file came from the internet, another user, or an unverified location.

### Safe practices when handling serialized data

- Only use `pickle` when your own trusted Python application creates, stores, and reads the data in a secure environment.
    
- Never accept `.pkl` files or pickled bytes from external users, public uploads, or untrusted network connections.
    
- Prefer `json` (or CSV for tabular data) whenever your data consists of standard types (`dict`, `list`, `str`, `int`, `float`, `bool`, `None`) or needs to be shared safely across systems.