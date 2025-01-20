<div align= "center">
  <h1>Python - Data Structures: Lists, Tuples</h1>
</div>

This repository features projects on Python data structures, such as lists and tuples, including various operations and manipulations.

# General 

### What are lists and how to use them ?
*Lists are ordered and mutable collections of elements. They can store elements of different types and are created using square brackets [].*

### What are the differences and similarities between strings and lists ?
*Both strings and lists are sequences that can be indexed and iterated. Strings are immutable, while lists are mutable. Lists can contain elements of different types, whereas strings contain only characters.*

### What are the most common methods of lists and how to use them ?
*Common methods include ```append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), and copy()```.*

### How to use lists as stacks and queues ?
*Lists can be used as stacks with ```append()``` and ```pop()```. They can be used as queues with ```append()``` and ```pop(0)```, though collections.deque is recommended for optimal performance in queues.*

### What are list comprehensions and how to use them ?
*List comprehensions provide a concise way to create lists using expressions and loops. Example: ```[x*2 for x in range(10)]```.*

### What are tuples and how to use them ?
*Tuples are similar to lists but are immutable. They are created using parentheses ```()``` and can store elements of different types.*

### When to use tuples versus lists ?
*Use tuples for immutable collections and lists for mutable collections. Tuples are often used as dictionary keys or for fixed data sets.*

### What is a sequence ?
*A sequence is an ordered collection of elements that supports indexing and iteration. ```Lists```, ```strings```, and ```tuples``` are examples ```of sequences.```*

### What is tuple packing ?
*Tuple packing is the process of combining multiple values into a single tuple. Example: ```t = 1, 2, 3.```*

### What is sequence unpacking ?
*Sequence unpacking is the process of extracting values from a sequence and assigning them to variables. Example: ```a, b, c = t.```*

### What is the del statement and how to use it ?
*The ```del``` statement is used to delete objects, such as list elements, variables, or object attributes. Example: del a[0].*

# Requirements
### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly ```#!/usr/bin/python3```
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc  


# Exercices

| Filename | Description |
| -------- | ----------- |
| `0-print_list_integer.py` | Prints all integers in a list. |
| `1-element_at.py` | Retrieves an element from a list like in C. |
| `2-replace_in_list.py` | Replaces an element of a list at a specific position. |
| `3-print_reversed_list_integer.py` | Prints all integers of a list, in reverse order. |
| `4-new_in_list.py` | Replaces an element in a list without modifying the original list. |
| `5-no_c.py` | Removes all characters 'c' and 'C' from a string. |
| `6-print_matrix_integer.py` | Prints a matrix of integers. |
| `7-add_tuple.py` | Adds two tuples. |
| `8-multiple_returns.py` | Returns the length of a string and its first character in a tuple. |
| `9-max_integer.py` | Finds the biggest integer in a list. |
| `10-divisible_by_2.py` | Finds all multiples of 2 in a list. |
| `11-delete_at.py` | Deletes the item at a specific position in a list. |
| `12-switch.py` | Switches the value of two variables. |


