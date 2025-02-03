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
| `1. My list` | Write a class MyList that inherits from list. |
| `2. Exact same object` | Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.|
| `3. Same class or inherit from` | Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.|
| `4. Only sub class of` | Write a function that returns True if an object inherits from a specified class; otherwise False.|
| `5. Geometry module` | Write an empty class BaseGeometry.|
| `6. Improve Geometry` | Public instance method that raises an Exception with the message `area() is not implemented`.|
| `7. Integer validator` | Create a class BaseGeometry with methods area(self) raising an exception `area() is not implemented` and integer_validator(self, name, value) ensuring value is a positive integer.|
| `8. Rectangle` | Creates a Rectangle class that inherits from BaseGeometry with private attributes width and height, without getter or setter, and which must be positive integers validated by integer_validator .|
| `9. Full rectangle` | Creates a Rectangle class that inherits from BaseGeometry with private width and height attributes, without getter or setter, validated as positive integers by integer_validator. Implements the area() method and makes print() and str() return the description [Rectangle] <width>/<height>.|
| `10. Square #1` | Creates a Square class that inherits from Rectangle with a private attribute size, without getter or setter, validated as a positive integer by integer_validator, and implements the area() method.|
| `11. ` | Creates a Square class that inherits from Rectangle with a private attribute size, without getter or setter, validated as a positive integer by integer_validator. Implements the area() method and makes print() and str() return the description [Square] <width>/<height>.|

<p align="center">
  <img src="https://i.imgur.com/J1oVLId.jpeg" name="logo Holberton"/>
</p>
