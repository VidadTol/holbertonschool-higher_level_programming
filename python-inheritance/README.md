<div align= "center">
  <h1>Python - Inheritance</h1>
</div>

# Resources 👀

 👉 [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)  
 👉 [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)  
 👉 [Inheritance in Pythons](https://www.packtpub.com/en-us/learning/how-to-tutorials/inheritance-python/)  
 👉 [Learn to Program 10 : Inheritance Magic Methods ](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

# General

### What is a superclass, baseclass or parentclass?

A superclass (or base class or parent class) is a class from which other classes inherit attributes and methods.

### What is a subclass?

A subclass is a class that inherits attributes and methods from another class, known as its superclass.

### How to list all attributes and methods of a class or instance?

Use the `dir()` function to list all attributes and methods of a class or instance.

### When can an instance have new attributes?

An instance can have new attributes when they are dynamically added after the instance has been created.

### How to inherit class from another?

Use the class definition syntax with the name of the superclass in parentheses.

### How to define a class with multiple base classes?

Define the class with multiple base classes by listing them in parentheses, separated by commas.

### What is the default class every class inherit from?

The default class every class inherits from is `object`.

### How to override a method or attribute inherited from the base class?

Override a method or attribute by defining it again in the subclass with the same name.

### Which attributes or methods are available by heritage to subclasses?

Public and protected attributes and methods are available by inheritance to subclasses.

### What is the purpose of inheritance?

The purpose of inheritance is to enable code reuse, modularity, and the creation of class hierarchies that define generic and specific behaviors.

### What are, when and how to use isinstance, issubclass, type and super built-in functions?

`isinstance(obj, class)`: Checks if obj is an instance of class or a subclass of class.

`issubclass(sub, super)`: Checks if sub is a subclass of super.

`type(obj)`: Returns the type of obj.

`super()`: Returns an object representing the superclass and is used to call its methods.

# Requirements

## Python Scripts

- Allowed editors: `vi, vim, emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## Python Test Cases
- Allowed editors: `vi, vim, emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)`' and `python3 -c print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# Exercices

| Filename | Description |
| -------- | ----------- |
| `0. Lookup` | Returns the list of available attributes and methods of an object. |
| `1. Real definition of a rectangle` | Defines a class Rectangle with private instance attributes width and height, with validation. |
| `2. Area and Perimeter` | Adds public methods area() and perimeter() to calculate the rectangle's area and perimeter.|
| `3. String representation` | Adds __str__() method to print the rectangle using the # character|
| `4. Eval is magic` | Adds __repr__() method to return a string representation of the rectangle for recreation.|
| `5. Detect instance deletion` | Adds __del__() method to print a message when an instance of Rectangle is deleted.|
| `6. How many instances` | Adds a public class attribute number_of_instances to track the number of instances created.|
| `7. Change representation` | Adds a public class attribute print_symbol to define the symbol used to print the rectangle.|
| `8. Compare rectangles` | Adds a static method bigger_or_equal() to return the bigger rectangle based on area.|
| `9. A square is a rectangle` | Adds a class method square() to return a new Rectangle instance where width and height are equal.|

<p align="center">
  <img src="https://i.imgur.com/J1oVLId.jpeg" name="logo Holberton"/>
</p>
