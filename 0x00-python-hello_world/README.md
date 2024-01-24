# 0x00. Python - Hello, World
### Concepts
For this project, we expect you to look at this concept:

- [Python programming](https://intranet.alxswe.com/concepts/550)


![meme](/0x00-python-hello_world/meme.jpg)



### In a nutshell…
- Auto QA review: 0.0/89 mandatory & 0.0/27 optional
- Altogether:  0.0%
  - Mandatory: 0.0%
  - Optional: 0.0%
  - Calculation:  0.0% + (0.0% * 0.0%)  == 0.0%


# Learning Resources
### Read or watch:

 1. [The Python tutorial (only the first three chapters below)](https://intranet.alxswe.com/rltoken/JsFCs_NBzMAR7-XPAZ9BoA)
 2. [Whetting Your Appetite](https://intranet.alxswe.com/rltoken/kifRlLG2iMX5AZiW8lrCMg)
 3. [Using the Python Interpreter](https://intranet.alxswe.com/rltoken/RVpfAuagCo9SdfYeoHd6jg)
 4. [An Informal Introduction to Python (Read up until “3.1.2. Strings” included)](https://intranet.alxswe.com/rltoken/bVps0ZPWq7qVZ7vc-eJGTw)
 5. [How To Use String Formatters in Python 3](https://intranet.alxswe.com/rltoken/Ju0J8BxkuPX5yKZctyKfsQ)
 6. [Learn to Program](https://intranet.alxswe.com/rltoken/szBsJ-Qyig_RrImN7RGlOg)
 7. [Pycodestyle – Style Guide for Python Code](https://intranet.alxswe.com/rltoken/tgYt-0zVy1T4sDlE9ohxnA)

# Learning Objectives
```
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
```
## General
1. Why Python programming is awesome
1. Who created Python
1. Who is Guido van Rossum
1. Where does the name ‘Python’ come from
1. What is the Zen of Python
1. How to use the Python interpreter
1. How to print text and variables using print
1. How to use strings
1. What are indexing and slicing in Python
1. What is the official Python coding style and how to check your code with pycodestyle

### Copyright - Plagiarism
 - You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
 - You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
 - You are not allowed to publish any content of this project.
 - Any form of plagiarism is strictly forbidden and will result in removal from the program.

# Requirements
## Python Scripts
 - Allowed editors: vi, vim, emacs
 - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
 - All your files should end with a new line
 - The first line of all your files should be exactly #!/usr/bin/python3
 - A README.md file at the root of the repo, containing a description of the repository
 - A README.md file, at the root of the folder of this project, is mandatory
 - Your code should use the *pycodestyle* (version 2.8.*)
 - All your files must be executable
 - The length of your files will be tested using wc

## Shell Scripts
 - Allowed editors: vi, vim, emacs
 - All your scripts will be tested on Ubuntu 20.04 LTS
 - All your scripts should be exactly two lines long (wc -l file should print 2)
 - All your files should end with a new line
 - The first line of all your files should be exactly #!/bin/bash
 - All your files must be executable

## C Scripts
 - Allowed editors: vi, vim, emacs
 - All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
 - All your files should end with a new line
 - Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
 - You are not allowed to use global variables
 - No more than 5 functions per file
 - In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
 - The prototypes of all your functions should be included in your header file called lists.h
 - Don’t forget to push your header file
 - All your header files should be include guarded

# Pycodestyle

> Pycodestyle is now the new standard of Python style code

> Your code should use the *pycodestyle* (version 2.8.*)

# Tasks
### 0. Run Python file 
1. Write a Shell script that runs a Python script.
1. The Python file name will be saved in the environment variable $PYFILE
```
[green@xero 0x00-python-hello_world]$ cat main.py 
───────┬─────────────────────────────────────────────────────────────────────────────
       │ File: main.py
───────┼─────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ print("Best School")
───────┴─────────────────────────────────────────────────────────────────────────────
[green@xero 0x00-python-hello_world]$ export PYFILE=main.py
[green@xero 0x00-python-hello_world]$ ./0-run 
Best School
[green@xero 0x00-python-hello_world]$ 

```
- Solution File: [0-run](./0-run)
  - Test file: [main.py](./main.py)

### 1. Run inline
1. Write a Shell script that runs Python code.
1. The Python code will be saved in the environment variable $PYCODE
```
[green@xero 0x00-python-hello_world]$ export PYCODE='print(f"Best School: {88+10}")'
[green@xero 0x00-python-hello_world]$ ./1-run_inline 
Best School: 98
[green@xero 0x00-python-hello_world]$
```
- Solution File: [1-run-inline](./1-run_inline)

### 2. Hello, print
> Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
- Use the function `print`
```
[green@xero 0x00-python-hello_world]$ ./2-print.py 
"Programming is like building a multilingual puzzle
[green@xero 0x00-python-hello_world]$
```
- Solution File [2-print.py](./2-print.py)

### 3. Print integer
> Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable number, followed by `Battery street`, followed by a new line.
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)
- The output of the script should be:
  - the number, followed by `Battery street`,
  - followed by a new line
- You are not allowed to cast the variable `number` into a string
- Your code must be 3 lines long
- You have to use f-strings [tips](https://realpython.com/python-f-strings/)
```
[green@xero 0x00-python-hello_world]$ ./3-print_number.py 
98 Battery street
[green@xero 0x00-python-hello_world]$
```
- Solution File: [3-print_number.py](./3-print_number.py)

### 4. Print float
> Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py)
- The output of the program should be:
  - `Float:`, followed by the float with only 2 digits
  - followed by a new line
- You are not allowed to cast `number` to string
- You have to use f-strings
```
[green@xero 0x00-python-hello_world]$ ./4-print_float.py 
Float: 3.14
[green@xero 0x00-python-hello_world]$ 
```
- Solution File: [4-print_float.py](./4-print_float.py)

### 5. Print string
> Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py)
- The output of the program should be:
  - 3 times the value of `str`
  - followed by a new line
  - followed by the 9 first characters of `str`
  - followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long
```
[green@xero 0x00-python-hello_world]$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
[green@xero 0x00-python-hello_world]$ 
```
- Solution File: [5-print_string.py](./5-print_string.py)

### 6. Play with strings
> Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) to print Welcome to Holberton School!
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py)
- You are not allowed to use any loops or conditional statements.
- You have to use the variables `str1` and `str2` in your new line of code
- Your program should be exactly 5 lines long
```

```
- Solution File: [ ](./)



## Repo info:

- **GitHub repository:** [alx-higher_level_programming](../README.md)
- **Directory:** [0x00-python-hello_world](./README.md)
