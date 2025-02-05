<div align= "center">
  <h1>Python OOP - Abtract Class, Interface, Subclassing</h1>
</div>

# Resources 👀

 👉 [Python 3 Object-Oriented Programming](https://docs.python.org/3/tutorial/classes.html)  
 👉 [ABC — Abstract Base Classes](https://docs.python.org/3/library/abc.html)  
 👉 [Real Python - Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)  
 👉 [Corey Schafer - OOP Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
 👉 [sentdex - Python OOP Tutorial](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfhTF3Zfyzc_yD-Mq9iTp4G)


# Introduction:
Welcome to this set of exercises aimed at honing your understanding and application of Object-Oriented Programming (OOP) concepts in Python. Through these exercises, you will delve into abstract classes, interfaces, duck typing, and subclassing standard base classes among other crucial OOP concepts. By the end of these exercises, you should be proficient in employing OOP principles to design, implement, and test Python programs.

# Learning Objectives:
`Abstract Classes`: Understand and apply abstract classes to define common interfaces while enforcing certain levels of class completeness.  
`Interfaces and Duck Typing`: Grasp the concept of interfaces and duck typing to ensure that objects adhere to a specific contract or protocol.  
`Subclassing Standard Base Classes`: Learn to extend standard base classes like lists, dictionaries, and iterators to create custom data structures with specialized behavior.  
`Method Overriding`: Employ method overriding to alter or enhance the behavior of base class methods.  
`Multiple Inheritance`: Understand and apply multiple inheritance to form complex relationships between classes.  
`Mixins`: Utilize mixins to compose behavior across unrelated classes.

# Exercices

| Filename | Objective |
| -------- | ----------- |
| `0. Abstract Animal Class and its Subclasses` | Create an abstract class named Animal using the ABC package with an abstract method called sound. Create two subclasses of Animal: Dog and Cat. Implement the sound method in each subclass to return the strings “Bark” and “Meow” respectively.|
| `1. Shapes, Interfaces, and Duck Typing` | Create an abstract class Shape with abstract methods area and perimeter, implement Circle and Rectangle inheriting from Shape, write a shape_info function to display their area and perimeter, and test this function with instances of Circle and Rectangle. |
| `2. Extending the Python List with Notifications` | Create a class named VerboseList that extends the Python list class. This custom class should print a notification message every time an item is added (using the append or extend methods) or removed (using the remove or pop methods).|
| `3. CountedIterator - Keeping Track of Iteration` | Create a class named CountedIterator that extends the built-in iterator obtained from the iter function. The CountedIterator should keep track of the number of items that have been iterated over. Specifically, you will need to override the __next__ method to increment a counter each time an item is fetched.|
| `4. The Enigmatic FlyingFish - Exploring Multiple Inheritance` | Construct a FlyingFish class that inherits from both a Fish class and a Bird class. Within FlyingFish, override methods from both parents. The goal is to comprehend multiple inheritance and how Python determines method resolution order..|
| `5. The Mystical Dragon - Mastering Mixins` | Design two mixin classes, SwimMixin and FlyMixin, each equipped with methods swim and fly respectively. Next, construct a class Dragon that inherits from both these mixins. Your aim is to show that a Dragon instance can both swim and fly.|


<p align="center">
  <img src="https://i.imgur.com/J1oVLId.jpeg" name="logo Holberton"/>
</p>