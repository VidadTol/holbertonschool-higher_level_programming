<div align= "center">
  <h1>Python - More Classes and Objects</h1>
</div>

# Resources 👀

 👉 [Object Oriented Programming ](https://python.swaroopch.com/oop.html)  
 👉 [Object Oriented Programming ](https://python-course.eu/oop/object-oriented-programming.php)  
 👉 [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)  
 👉 [classmethods and staticmethods ](https://www.youtube.com/watch?v=rq8cL2XMM5M)
 👉 [Properties vs. Getters and Setters ](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
 👉 [str vs repr ](https://shipit.dev/posts/python-str-vs-repr.html)


# General

### Why is Python programming awesome?
Python programming is awesome because of its simple and readable syntax, extensive standard libraries, versatility in various domains (web development, data science, AI, etc.), and a strong, supportive community.

### What is OOP?
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects" which can contain data in the form of fields (attributes) and code in the form of procedures (methods).

### What does “first-class everything” mean?
In Python, everything is treated as an object, including functions, classes, and modules. This means you can assign them to variables, pass them as arguments, and return them from other functions.

### What is a class?
A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

### What is an object and an instance?
An object is an instance of a class. An instance is a specific realization of a class.

### What is the difference between a class and an object or instance?
A class is a blueprint or template, while an object or instance is a concrete entity created using the class.

### What is an attribute?
An attribute is a variable that belongs to a class or an instance of a class.

### What are public, protected, and private attributes, and how to use them?
Public attributes can be accessed from anywhere.

Protected attributes (prefix with a single underscore _) can be accessed within the class and its subclasses.

Private attributes (prefix with double underscores __) can be accessed only within the class where they are defined.

### What is self?
self is a reference to the current instance of the class. It is used to access attributes and methods of the class.

### What is a method?
A method is a function defined within a class that operates on instances of that class.

### What is the special `__init__` method and how to use it?
`__init__` is a special method known as the constructor. It is used to initialize the attributes of an instance when the instance is created.

### What is Data Abstraction, Data Encapsulation, and Information Hiding?
Data Abstraction: Hiding complex implementation details and showing only the necessary features of an object.

Data Encapsulation: Bundling data and methods that operate on the data within one unit, e.g., a class.

Information Hiding: Restricting direct access to some of an object's components, which is a principle of encapsulation.

### What is a property?
A property is a special attribute that allows you to define methods for reading, writing, and deleting an attribute's value.

### What is the difference between an attribute and a property in Python?
An attribute is a simple variable bound to an instance or class, while a property uses methods to control access to an attribute.

### What is the Pythonic way to write getters and setters in Python?
Use the `@property` decorator `for getters` and `@property_name.setter` `for setters`.

### What are the special `__str__` and `__repr__` methods and how to use them?
`__str__` returns a readable string representation of an object (used by print).

`__repr__` returns an official string representation of an object (used for debugging).

### What is the difference between `__str__` and `__repr__`?
`__str__` is meant for users (readable).

`__repr__` is meant for developers (official and unambiguous).

### What is a class attribute?
A class attribute is a variable defined at the class level and shared by all instances of the class.

### What is the difference between an object attribute and a class attribute?
An object attribute is specific to an instance, while a class attribute is shared among all instances of the class.

### What is a class method?
A class method is a method that takes the class as its first argument (usually named cls) and is defined with the `@classmethod` decorator.

### What is a static method?
A static method is a method that does not take an instance or class as its first argument and is defined with the @staticmethod decorator.

### How to dynamically create arbitrary new attributes for existing instances of a class?
Assign a new attribute directly to the instance:
`instance.new_attribute = value `

### How to bind attributes to objects and classes?
To bind an attribute to an instance:
`instance.attribute = value`
To bind an attribute to a class:
`Class.attribute = value`

### What is __dict__ of a class and of an instance of a class, and what does it contain?
`__dict__` is a dictionary that contains the attributes and their values for an instance or class.

### How does Python find the attributes of an object or class?
Python uses the attribute lookup chain, starting with the instance's attributes, then the class's attributes, and then the attributes of the parent classes.

### How to use the getattr function?
getattr is used to get the value of an attribute from an object using its name as a string:
`value = getattr(object, 'attribute_name', default_value)`

# Requirements

- Allowed editors: `vi, vim, emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
The length of your files will be tested using wc


# Exercices

| Filename | Description |
| -------- | ----------- |
| `0. Simple rectangle` | Defines an empty class Rectangle. |
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
