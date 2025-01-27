<div align= "center">
  <h1>Python - classes</h1>
</div>

# Resources 👀

 👉 [Object Oriented Programming ](https://python.swaroopch.com/oop.html)  
 👉 [Object Oriented Programming ](https://python-course.eu/oop/object-oriented-programming.php)  
 👉 [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)  
 👉 [Object Oriented Programming ](https://www.youtube.com/watch?v=1AGyBuVCTeE)
 👉 [Python Classes and Objects ](https://www.youtube.com/watch?v=apACNr7DC_s)
 👉 [Object Oriented Programming ](https://www.youtube.com/watch?v=-DP1i2ZU9gk)


# General
### What is OOP?  
OOP (Object-Oriented Programming) is a programming paradigm based on the concept of objects, which can contain data and code to manipulate that data.

### “First-class everything”?
In Python, "first-class everything" means that all entities (functions, classes, modules, etc.) are first-class objects, meaning they can be passed as arguments, returned from functions, and assigned to variables.

### What is a class?
A class is a blueprint or template for creating objects. It defines attributes and behaviors that the objects created from the class will have.

### What is an object and an instance?
An object is a concrete instance of a class. An instance is an individual copy of the class with specific values.

### What is the difference between a class and an object or instance?
A class is a blueprint, while an object (or instance) is a concrete copy created from that class with actual values.

### What is an attribute?
An attribute is a variable that belongs to a class or an instance of a class. It stores specific data related to the class or instance.

### What are and how to use public, protected and private attributes?
Public attributes: Accessible from anywhere. No leading underscore.

Protected attributes: Intended for internal use, indicated by a single leading underscore.

Private attributes: Intended to be inaccessible outside the class, indicated by double leading underscores, subject to name mangling.

### What is self?
self is a reference to the current instance of the class. It is used to access the attributes and methods of the class within its methods.

### What is a method?
A method is a function defined inside a class that operates on the attributes of the instance of the class.

### What is the special init method and how to use it?
The __init__ method is a constructor that is called when you create a new instance of a class. It initializes the object's attributes.

### What is Data Abstraction, Data Encapsulation, and Information Hiding?
Data Abstraction: Hiding complex implementation details and showing only the essential features.

Data Encapsulation: Bundling data and methods that operate on that data within a single unit (class).

Information Hiding: Restricting access to certain parts of an object to prevent unauthorized modifications.

### What is a property?
A property is an attribute of a class that uses methods to control access (read/write) to a private value.

### What is the difference between an attribute and a property in Python?
An attribute is a variable belonging to a class or an instance, while a property uses methods to access a private value.

### What is the Pythonic way to write getters and setters in Python?
The Pythonic way to write getters and setters is by using the @property decorator for getters and @attribute.setter decorator for setters.

### How to dynamically create arbitrary new attributes for existing instances of a class?
You can add new attributes to an instance by assigning a value to a new attribute using dot notation.

### How to bind attributes to object and classes?
Attributes can be bound to instances by defining them in the constructor, and to classes by defining them at the class level.

### What is the dict of a class and/or instance of a class and what does it contain?
__dict__ is a dictionary that contains the attributes of a class or an instance.

### How does Python find the attributes of an object or class?
Python looks for attributes in the __dict__ of the instance, then the class, and finally in the parent classes if they exist.

### How to use the getattr function?
getattr is used to access an attribute of an object using its name as a string, optionally providing a default value if the attribute does not exist.

# Requirements

- Allowed editors: `vi, vim, emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
The length of your files will be tested using wc
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

# Exercices

| Filename | Description |
| -------- | ----------- |
| `0. My first square` | Write an empty class Square that defines a square:. |
| `1. Square with size` | Write a class Square that defines a square by: (based on 0-square.py) |
| `2. Size validation` | TWrite a class Square that defines a square by: (based on 1-square.py)|
| `3. Area of a square` | Write a class Square that defines a square by: (based on 2-square.py)|
| `4. Access and update private attribute` | Write a class Square that defines a square by: (based on 3-square.py) |
| `5. Printing a square` | Write a class Square that defines a square by: (based on 4-square.py)|
| `6. Coordinates of a square` | Directory containing unit tests for each function. |


<p align="center">
  <img src="https://i.imgur.com/J1oVLId.jpeg" name="logo Holberton"/>
</p>
