<div align= "center">
  <h1>Python - Test-driven development</h1>
</div>

# Resources

👉 [doctest — Test interactive Python examples ](https://docs.python.org/3/library/doctest.html)  
👉 [doctest – Testing through documentation ](https://pymotw.com/3/doctest/)  
👉 [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)  



General

### Why is Python programming awesome?
Python is awesome because of its simple syntax, versatility in various fields (web, AI, data science), vast community, and rich libraries.

### What’s an interactive test?
An interactive test is where the developer directly interacts with the program to verify its behavior in real time, often in a REPL interpreter.

### Why are tests important?
Tests are important to detect errors, ensure code quality, facilitate maintenance, and document program behavior.

### How to write docstrings to create tests?
Docstrings include descriptions and usage examples within functions, classes, and modules, enabling the use of doctest.

### How to write documentation for each module and function?
Use docstrings to document the purpose, parameters, and return values of each module and function.

### What are the basic option flags to create tests?
Basic options include using unittest, doctest, and pytest to write and execute tests.

### How to find edge cases?
Analyze the function's requirements to identify extreme values and special conditions that might cause issues.


# Requirements

#### Python Scripts

- Allowed editors: ```vi, vim, emacs```  
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)  
- All your files should end with a new line  
- The first line of all your files should be exactly `#!/usr/bin/python3`  
- A `README.md` file, at the root of the folder of the project, is mandatory  
- Your code should use the pycodestyle (version 2.7.*)  
- All your files must be executable  
- The length of your files will be tested using ```wc``` 

#### Python Test Cases

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your functions should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!

# Exercices

| Filename | Description |
| -------- | ----------- |
| `0. Integers addition` | That adds 2 integers. |
| `1. Divide a matrix` | That divides all elements of a matrix. |
| `2. Say my name` | That prints My name is <first name> <last name>.|
| `3. Print square` | That prints a square with the character #.|
| `4. Text indentation` | That prints a text with 2 new lines after each of these characters: ., ? and : |
| `5. Max integer - Unittest` | you will write unittests for the function def max_integer(list=[]):.|
| `tests/` | Directory containing unit tests for each function. |

<p align="center">
  <img src="https://i.imgur.com/J1oVLId.jpeg" name="logo Holberton"/>
</p>
