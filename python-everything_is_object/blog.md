
<div align= "center">
  <h1>PYTHON EVERYTHING IS OBJECT</h1>
</div>

<div align= "center">
  <h>Exploring the fundamental concepts of Python's object model
  
  Mutable and Immutable Objects and Their Implications</h1>
</div>

<p align="center">
  <img src="r_208403_QPSN8.jpg" alt="image d'un chat" width="300" height="300"/>
</p>

## Introduction
Python is a general-purpose language known for its simplicity and dynamism. An essential aspect of Python programming is understanding how objects are stored and manipulated. This article explores Python's handling of mutable and immutable objects and explains why their differences are important, particularly when arguments are passed to functions. Using relevant code snippets, we will unpack these concepts step by step.

## ID and Type
In Python, every object is defined by its type and identity. While the `type()` function provides the object's type, the `id()` function provides its unique memory address:

`a = [1, 2, 3]`   
`print(type(a))` # Output: <class 'list'>   
`print(id(a))` # Output: 139926795932424 

***An object's identifier reflects its location in memory and remains constant until its reference is changed.***

## Mutable Objects
Mutable objects are those whose contents can be modified after their creation. Lists, dictionaries, and sets are perfect examples:

`a = [1, 2, 3]  `
`print(id(a))` # Output:139926795932424   
`a.append(4)`   
`print(id(a))` # Output: 139926795932424   

***As shown, the memory address remains unchanged when we modify the list a. This mutability allows for flexible and efficient data manipulation.***

## Immutable Objects

Immutable objects, on the other hand, cannot be modified once created. Examples: tuples, strings, and numbers:

`b = (1, 2)`   
`print(id(b))` # Output: 139926795932828   
`b += (3,)` # This creates a new tuple   
`print(id(b))` # Output: 139926795933120       (different ID)

***Any modification results in the creation of a new object, leaving the original unchanged. This characteristic guarantees immutability.***

`Why is this important ?`   

The distinction between mutable and immutable objects fundamentally influences how Python handles them. Mutable objects allow in-place updates without recreating the object, while immutable objects ensure consistency and safety, especially in concurrent programming. Furthermore, Python uses this distinction for optimization purposes:

***`Immutable objects, such as integers, are sometimes reused for efficiency reasons.`***

***`Mutable objects are advantageous for data structures that require frequent modifications.`***

## How Arguments Are Passed to Functions   
Python passes arguments to functions as references. However, the behavior differs depending on the mutability:

`Mutable objects:`    
- _Changes made to the function affect the original object._

`def modify_list(lst):`   
`lst.append(4)`

`my_list = [1, 2, 3]`    
`modify_list(my_list)`   
`print(my_list)` # Output: [1, 2, 3, 4]   

`Immutable objects:`   
- _Since they cannot be modified, functions create new objects when they attempt modifications._

`def modify_tuple(tpl):`   
`tpl += (4,)` 

`my_tuple = (1, 2, 3)`   
`modify_tuple(my_tuple)`   
`print(my_tuple) # Output: (1, 2, 3)`   

This behavior has important implications in large-scale projects where object modifications can lead to unexpected bugs.

## Conclusion
The distinction between mutable and immutable objects is essential in Python programming. It determines the behavior and interactions of objects within the system. By mastering these concepts, you can write more efficient and bug-free code.