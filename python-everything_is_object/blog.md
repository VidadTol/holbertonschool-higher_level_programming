<p align="center">
  <img src="definition-outil-de-developpement-web.webp" alt="image de code sur pc" width="500" height="300"/>
</p>

<div align="center"> <h1>PYTHON EVERYTHING IS OBJECT</h1> </div>

<div align="center"> <h>Exploring the fundamental concepts of Python's object model

Mutable and Immutable Objects and Their Implications</h1> </div>

### Introduction

Python is a general-purpose language known for its simplicity and dynamism. An essential aspect of Python programming is understanding how objects are stored and manipulated. This article explores Python's handling of mutable and immutable objects and explains why their differences are important, particularly when arguments are passed to functions. Using relevant code snippets, we will unpack these concepts step by step.

### ID and Type

In Python, every object is defined by its type and identity. While the type() function provides the object's type, the id() function provides its unique memory address:

a = [1, 2, 3]  
print(type(a)) _# <class 'list'>_  
print(id(a)) _# 139926795932424_

<class 'list'> : Le type de l'objet a est une liste.  
139926795932424 : L'identifiant unique indique l'emplacement mémoire de a.

## Mutable Objects

Mutable objects are those whose contents can be modified after their creation. Lists, dictionaries, and sets are perfect examples:

a = [1, 2, 3]  
print(id(a)) _# 139926795932424_  
a.append(4)  
print(id(a)) _# 139926795932424_

139926795932424 : L'adresse mémoire reste la même après modification, ce qui montre que l'objet est modifié en place.

### Immutable Objects

Immutable objects, on the other hand, cannot be modified once created. Examples: tuples, strings, and numbers:

b = (1, 2)  
print(id(b)) _# 139926795932828_  
b += (3,) _# This creates a new tuple_  
print(id(b)) _# 139926795933120_

139926795932828 : Adresse mémoire initiale de b.
139926795933120 : Nouvelle adresse mémoire après modification, indiquant que l'objet original est remplacé par un nouveau.

### Why is this important?

The distinction between mutable and immutable objects fundamentally influences how Python handles them. Mutable objects allow in-place updates without recreating the object, while immutable objects ensure consistency and safety, especially in concurrent programming. Furthermore, Python uses this distinction for optimization purposes:

`Immutable objects,` such as integers, are sometimes reused for efficiency reasons.

`Mutable` objects are advantageous for data structures that require frequent modifications.

How Arguments Are Passed to Functions
Python passes arguments to functions as references. However, the behavior differs depending on the mutability:

`Mutable objects:`  
Changes made to the function affect the original object.

def modify_list(lst):  
 lst.append(4)

my\*list = [1, 2, 3]  
modify*list(my_list)  
print(my_list) *# [1, 2, 3, 4]\_

[1, 2, 3, 4] : La liste my_list est modifiée directement dans la fonction.

`Immutable objects:`  
Since they cannot be modified, functions create new objects when they attempt modifications.

def modify_tuple(tpl):  
 tpl += (4,)

my\*tuple = (1, 2, 3)  
modify*tuple(my_tuple)  
print(my_tuple) *# (1, 2, 3)\_

(1, 2, 3) : Le tuple original reste inchangé, même après l'appel de la fonction.

This behavior has important implications in large-scale projects where object modifications can lead to unexpected bugs.

Conclusion
The distinction between mutable and immutable objects is essential in Python programming. It determines the behavior and interactions of objects within the system. By mastering these concepts, you can write more efficient and bug-free code.
