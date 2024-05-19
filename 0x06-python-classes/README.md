# 0x06. Python - Classes and Objects

:gear: Weight: 1

:calendar: Project over - took place from Jan 23, 2024 6:00 AM to Jan 24, 2024 6:00 AM

:ballot_box_with_check: An auto review will be launched at the deadline

![oop-meme](../memes/oop-meme.jpg)

# Background Context
> OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum).

> As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

> Read or watch the below resources in the order presented.

# Learning Resources
### Read or watch:
1. [Object Oriented Programming](https://python.swaroopch.com/oop.html)(Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, `classmethod` and `staticmethod` yet)
1. [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)(Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The `__init__` Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
1. [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
1. [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE&)
1. [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
1. [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

# Learning Objectives
> At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- Why Python programming is awesome
- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the `__dict__` of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the `getattr` function

## Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

# Requirements
## General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

# More info
Documentation is now mandatory! Each module, class, and method must contain docstring as comments. [Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

# Tasks

### `0.` My first square 
> Write an empty class `Square` that defines a square:
- You are not allowed to import any module
Write an empty class Square that defines a square:

    You are not allowed to import any module
```
[green@xero 0x06-python-classes]$ cat 0-main.py 
───────┬─────────────────────────────────────────────────────────────────────────────────────
       │ File: 0-main.py
───────┼─────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ Square = __import__('0-square').Square
   3   │ 
   4   │ my_square = Square()
   5   │ print(type(my_square))
   6   │ print(my_square.__dict__)
───────┴─────────────────────────────────────────────────────────────────────────────────────
[green@xero 0x06-python-classes]$ ./0-main.py 
<class '0-square.Square'>
{}
[green@xero 0x06-python-classes]$ 
```
- Solution File: [0-square.py](./0-main.py)

<hr>

### `1.` Square with size
> Write a class `Square` that defines a square by: (based on `0-square.py`)
- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)
- You are not allowed to import any module

> Why?

- Why size is private attribute?

> The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.
```
[green@xero 0x06-python-classes]$ cat 1-main.py 
───────┬─────────────────────────────────────────────────────────────────────────────────────
       │ File: 1-main.py
───────┼─────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ Square = __import__('1-square').Square
   3   │ 
   4   │ my_square = Square(3)
   5   │ print(type(my_square))
   6   │ print(my_square.__dict__)
   7   │ 
   8   │ try:
   9   │     print(my_square.size)
  10   │ except Exception as e:
  11   │     print(e)
  12   │ 
  13   │ try:
  14   │     print(my_square.__size)
  15   │ except Exception as e:
  16   │     print(e)
───────┴─────────────────────────────────────────────────────────────────────────────────────
[green@xero 0x06-python-classes]$ ./1-main.py
<class '1-square.Square'>
{'_size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
[green@xero 0x06-python-classes]$ 
```
<hr>

### `2.` Size validation 
> Write a class `Square` that defines a square by: (based on `1-square.py`)
- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
  - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
  - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- You are not allowed to import any module
```
[green@xero 0x06-python-classes]$ cat 2-main.py 
───────┬───────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 2-main.py
───────┼───────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ Square = __import__('2-square').Square
   3   │ 
   4   │ my_square_1 = Square(3)
   5   │ print(type(my_square_1))
   6   │ print(my_square_1.__dict__)
   7   │ 
   8   │ my_square_2 = Square()
   9   │ print(type(my_square_2))
  10   │ print(my_square_2.__dict__)
  11   │ 
  12   │ try:
  13   │     print(my_square_1.size)
  14   │ except Exception as e:
  15   │     print(e)
  16   │ 
  17   │ try:
  18   │     print(my_square_1.__size)
  19   │ except Exception as e:
  20   │     print(e)
  21   │ 
  22   │ try:
  23   │     my_square_3 = Square("3")
  24   │     print(type(my_square_3))
  25   │     print(my_square_3.__dict__)
  26   │ except Exception as e:
  27   │     print(e)
  28   │ 
  29   │ try:
  30   │     my_square_4 = Square(-89)
  31   │     print(type(my_square_4))
  32   │     print(my_square_4.__dict__)
  33   │ except Exception as e:
  34   │     print(e)
───────┴───────────────────────────────────────────────────────────────────────────────────────────────
[green@xero 0x06-python-classes]$ ./2-main.py 
<class '2-square.Square'>
{'_size': 3}
<class '2-square.Square'>
{'_size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
[green@xero 0x06-python-classes]$
```
- Solution File: [2-square.py](./2-main.py)