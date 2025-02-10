<div align= "center">
  <h1>Python- Input/Output</h1>
</div>


# General 

### Why is Python programming awesome?
Python is popular due to its simplicity, readability, and versatility. It's great for beginners and experts alike. Its extensive libraries and active community support a wide range of applications from web development to data science.

### How to open a file?
To open a file in Python, use the open function with the appropriate mode ('r' for reading, 'w' for writing, 'a' for appending, etc.) and specify the filename.

### How to write text in a file?
To write text to a file, open the file in write mode ('w') and use the write method to add the text.

### How to read the full content of a file?
To read the full content of a file, open the file in read mode ('r') and use the read method.

### How to read a file line by line?
To read a file line by line, open the file in read mode ('r') and iterate over each line using a loop.

### How to move the cursor in a file?
To move the cursor in a file, use the seek method with the desired byte offset.

### How to make sure a file is closed after using it?
To ensure a file is properly closed after using it, use the with statement, which handles opening and closing the file.

### What is and how to use the with statement?
The with statement simplifies exception handling by encapsulating common try/finally code patterns, ensuring that resources are properly cleaned up.

### What is JSON?
JSON (JavaScript Object Notation) is a lightweight data interchange format that's easy for humans to read and write, and easy for machines to parse and generate.

### What is serialization?
Serialization is the process of converting a data structure or object into a format that can be easily stored or transmitted.

### What is deserialization?
Deserialization is the process of converting serialized data back into a data structure or object.

### How to convert a Python data structure to a JSON string?
To convert a Python data structure to a JSON string, use the appropriate method from the json module.

### How to convert a JSON string to a Python data structure?
To convert a JSON string to a Python data structure, use the appropriate method from the json module.

### How to access command line parameters in a Python script?
To access command line parameters in a Python script, use the sys.argv list from the sys module.

# Requirements

- Allowed editors: ```vi, vim, emacs```  
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)  
- All your files should end with a new line  
- The first line of all your files should be exactly `#!/usr/bin/python3`  
- A `README.md` file, at the root of the folder of the project, is mandatory  
- Your code should use the pycodestyle (version 2.7.*)  
- All your files must be executable  
- The length of your files will be tested using ```wc```  

# Python Test Cases

- Allowed editors: `vi, vim, emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# Exercices

| Filename | Description |
| -------- | ----------- |
| `0. Read file` | Reads a text file (UTF8) and prints it to stdout. |
| `1. Write to a file` | Writes a string to a text file (UTF8) and returns the number of characters written. |
| `2. Append to a file` | Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.|
| `3. To JSON string` | Write a function that returns the JSON representation of an object (string). |
| `4. ` | |
| `5. ` | |
| `6. ` | |
| `7. ` | |
| `8. ` | |
| `9. ` | |
| `10. ` | |
| `11. ` | |
| `12. ` | |


<p align="center">
  <img src="https://i.imgur.com/J1oVLId.jpeg" name="logo Holberton"/>
</p>
