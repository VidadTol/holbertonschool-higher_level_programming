<div align= "center">
  <h1>Python- Exceptions</h1>
</div>

This repository presents projects on exception handling in Python. It includes various operations and manipulations to understand and exploit exception mechanisms efficiently.

# Resources

👉 [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)  
👉 [Learn to Program 11 Static & Exception Handling ](https://www.youtube.com/watch?v=7vbgD-3s-w4)  

# General 

### Why Python programming is awesome?
Python programming is awesome because of its simplicity, readability, and versatility. It has a vast standard library and an active community, making it an ideal choice for both beginners and experts.

### What’s the difference between errors and exceptions?
Errors are issues in the code that prevent it from running correctly. Exceptions are a subset of errors that the program can catch and handle, allowing the control flow to be maintained.

### What are exceptions and how to use them?
Exceptions are abnormal events that occur during the execution of a program and interrupt the normal flow of instructions. To use exceptions in Python, we employ `try`, `except`, `else`, and `finally` blocks.

### When do we need to use exceptions?
Exceptions should be used when we need to handle unforeseen or abnormal situations in the program, such as input/output errors, calculation errors, or network connection errors.

### How to correctly handle an exception?
To handle an exception correctly, we use a try block to `wrap` the code that might cause an exception, and one or more except blocks to handle specific exceptions. A `finally` block can be used to execute cleanup code, whether an exception occurred or not.

### What’s the purpose of catching exceptions?
The purpose of catching exceptions is to allow the program to continue running even if an error occurs, providing a mechanism to manage these errors in a controlled and informative way.

### How to raise a builtin exception?
To raise a builtin exception, we use the raise statement followed by the exception name.

### When do we need to implement a clean-up action after an exception?
We need to implement a clean-up action after an exception when there are resources to release or states to reset, such as closing files, releasing memory, or resetting variables.  

# Requirements

- Allowed editors: ```vi, vim, emacs```  
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)  
- All your files should end with a new line  
- The first line of all your files should be exactly `#!/usr/bin/python3`  
- A `README.md` file, at the root of the folder of the project, is mandatory  
- Your code should use the pycodestyle (version 2.7.*)  
- All your files must be executable  
- The length of your files will be tested using ```wc```  

# Exercices

| Filename | Description |
| -------- | ----------- |
| `0. Safe list printing` | That prints `x` elements of a list. |
| `1. Safe printing of an integers list` | That prints an integer with `"{:d}".format()`. |
| `2. Print and count integers` | That prints the first `x` elements of a list and only integers.|
| `3. Integers division with debug` | That divides 2 integers and prints the result.|
| `4. Divide a list` | That divides element by element 2 lists. |
| `5. Raise exception` | That raises a type exception. |
| `6. Raise a message` | That raises a name exception with a message. |

<p align="center">
  <img src="https://i.imgur.com/J1oVLId.jpeg" name="logo Holberton"/>
</p>
