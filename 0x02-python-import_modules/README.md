# 0x02. Python - import & modules 

:teacher: By: Guillaume

:gear: Weight: 1

:calendar: Project over - took place from Jan 4, 2024 6:00 AM to Jan 5, 2024 6:00 AM

:ballot_box_with_check: An auto review will be launched at the deadline

# Learning Resources
### Read or watch:
1. [Modules](https://docs.python.org/3/tutorial/modules.html)
1. [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
1. [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

### man or help:
`python3`

# Learning Objectives
> At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

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
- The first line of all your files should be exactly #!/usr/bin/python3
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle (version 2.8.*)`
- All your files must be executable
- The length of your files will be tested using wc

# Tasks

### `0.` Import a simple function from a simple file
> Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`
- You have to use `print` function with string format to display integers
- You have to assign:
  - the value `1` to a variable called `a`
  - the value `2` to a variable called `b`
  - and use those two variables as arguments when calling the functions `add` and `print`
- `a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`
- Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
- You can only use the word `add_0` once in your code
- You are not allowed to use `*` for importing or `__import__`
- Your code should not be executed when imported - by using `__import__`, like the example below

