<div align= "center">
  <h1>Python-more_data_structures</h1>
</div>

The Python - Other Data Structures: Set, Dictionary repository presents projects on data structures in Python, specifically sets and dictionaries. It includes various operations and manipulations that allow to understand and exploit these data structures in an efficient way.

# Resources

* [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
* [Lambda, filter, reduce and map](https://python-course.eu/advanced-python/lambda-filter-reduce-map.php)
* [Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)

# General 

### Why Python programming is awesome ?  
Python's simplicity and readability make it an ideal choice for both beginners and experienced developers. It is incredibly versatile, with applications ranging from web development to data science, machine learning, automation, and more. Python's extensive standard library and vibrant ecosystem of third-party packages, along with its large and supportive community, further enhance its appeal. Additionally, Python is cross-platform, meaning it works seamlessly on various operating systems.

###  What are sets and how to use them ?
Sets are unordered collections of unique elements. They are useful for storing unique items and performing operations such as union, intersection, and difference. Sets can be created using curly braces {} or the set() function.

### What are the most common methods of set and how to use them ? 
Common methods of sets include:

```add(element)```: Adds an element to the set.

```remove(element)```: Removes an element from the set, raising an error if the element is not found.

```discard(element)```: Removes an element from the set if it is present.

```union(other_set)```: Returns a new set with elements from both sets.

```intersection(other_set)```: Returns a new set with elements common to both sets.

```difference(other_set)```: Returns a new set with elements in the set but not in other_set.

```symmetric_difference(other_set)```: Returns a new set with elements in either set but not in both.

### When to use sets versus lists ?
Sets are ideal when you need unique elements or fast membership testing. Lists are preferable when you need an ordered collection of elements, allow duplicates, or require indexed access to elements.

### How to iterate into a set ?
Iteration through a set is straightforward using a for loop.

### What are dictionaries and how to use them ?
Dictionaries are unordered collections of ```key-value pairs```. They are useful for storing data that can be quickly looked up by a unique key. Dictionaries can be created using curly braces ```{}``` with key-value pairs separated by colons, or the ```dict()``` function.

### When to use dictionaries versus lists or sets ? 
Dictionaries are best used when you need a key-value pair structure or fast lookups by unique keys. Lists are suitable for ordered collections of elements or allowing duplicates. Sets are useful for collections of unique elements or fast membership testing.

### What is a key in a dictionary ?
A key in a dictionary is a unique identifier used to access the associated value. Keys must be immutable, such as strings, numbers, or tuples.

### How to iterate over a dictionary ?
You can iterate over a dictionary's keys, values, or key-value pairs using a for loop.

### What is a lambda function ?
A ```lambda function``` is a small anonymous function defined with the lambda keyword. It can take any number of arguments but has only one expression.

### What are the map, reduce and filter functions:

```map(function, iterable)```: Applies a function to all items in an iterable and returns a map object.

```filter(function, iterable)```: Filters items in an iterable based on a function that returns True or False and returns a filter object.

```reduce(function, iterable)```: Applies a rolling computation to sequential pairs of values in an iterable, available in the functools module.

# Requirements

- Allowed editors: ```vi, vim, emacs```  
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)  
- All your files should end with a new line  
- The first line of all your files should be exactly ```#!/usr/bin/python3```  
- A README.md file, at the root of the folder of the project, is mandatory  
- Your code should use the pycodestyle (version 2.7.*)  
- All your files must be executable  
- The length of your files will be tested using ```wc```  

# Exercices

| Filename | Description |
| -------- | ----------- |
| `0. Squared simple` | Computes the square value of all integers of a matrix. |
| `1. Search and replace` | Replaces all occurrences of an element by another in a new list. |
| `2. Unique addition` | Adds all unique integers in a list (only once for each integer) |
| `3. Present in both` | Returns a set of common elements in two sets. |
| `4. Only differents` | Returns a set of all elements present in only one set. |
| `5. Number of keys` | Returns the number of keys in a dictionary. |
| `6. Print sorted dictionary` | Prints a dictionary by ordered keys. |
| `7. Update dictionary` | Replaces or adds key/value in a dictionary. |
| `8. Simple delete by key` | Deletes a key in a dictionary. |
| `9. Multiply by 2` | Returns a new dictionary with all values multiplied by 2 |
| `10. Best score` | Returns a key with the biggest integer value. |
| `11. Multiply by using map` | Returns a list with all values multiplied by a number without using any loops. |
| `12. Roman to Integer` | Technical interview preparation |
