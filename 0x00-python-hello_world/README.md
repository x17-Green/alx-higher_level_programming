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
───────┬───────────────────────────────────────
       │ File: main.py
───────┼───────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ print("Best School")
───────┴───────────────────────────────────────
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
[green@xero 0x00-python-hello_world]$ ./6-concat.py 
Welcome to Holberton School!
[green@xero 0x00-python-hello_world]$ 
```
- Solution File: [6-concat.py](./6-concat.py)

### 7. Copy - Cut - Paste
> Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- `word_first_3` should contain the first 3 letters of the variable `word`
- `word_last_2` should contain the last 2 letters of the variable `word`
- `middle_word` should contain the value of the variable `word` without the first and last letters
```
[green@xero 0x00-python-hello_world]$ ./7-edges.py 
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
[green@xero 0x00-python-hello_world]$ 
```
- Solution File: [7-edges.py](./7-edges.py)

### 8. Create a new sentence
> Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line.
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals
```
[green@xero 0x00-python-hello_world]$ ./8-concat_edges.py 
object-oriented programming with Python
[green@xero 0x00-python-hello_world]$ wc -l 8-concat_edges.py 
5 8-concat_edges.py 
[green@xero 0x00-python-hello_world]$ 
```
- Solution File: [8-concat_edges.py](./8-concat_edges.py)

### 9. Easter Egg
> Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
  - Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)
```
[green@xero 0x00-python-hello_world]$ ./9-easter_egg.py 
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
[green@xero 0x00-python-hello_world]$ 
```
- Solution File: [9-easter_egg.py](./9-easter_egg.py)

### 10. Linked list cycle
**Technical interview preparation:**
  - You are not allowed to google anything
  - Whiteboard first
  - This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.

Write a function in C that checks if a singly linked list has a cycle in it.
  - Prototype: `int check_cycle(listint_t *list);`
  - Return: `0` if there is no cycle, `1` if there is a cycle

*Requirements:*
  - Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`
```
[green@xero 0x00-python-hello_world]$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
[green@xero 0x00-python-hello_world]$ ./cycle 
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
[green@xero 0x00-python-hello_world]$ 
```
- Solution File: [10-check_cycle.c](./10-check_cycle.c)
- Test files
  - [10-linked_lists.c](./10-linked_lists.c)
  - [10-main.c](./10-main.c)
- Header File: [lists.h](./lists.h)

### 11. Hello, write
> Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.
- Use the function `write` from the `sys` module
- You are not allowed to use `print`
- Your script should print to `stderr`
- Your script should exit with the status code `1`
```
[green@xero 0x00-python-hello_world]$ ./100-write.py 
and that piece of art is useful - Dora Korpar, 2015-10-19
[green@xero 0x00-python-hello_world]$ echo $?
1
[green@xero 0x00-python-hello_world]$ ./100-write.py 2> q
[green@xero 0x00-python-hello_world]$ cat q
───────┬───────────────────────────────────────────────────────────
       │ File: q
───────┼───────────────────────────────────────────────────────────
   1   │ and that piece of art is useful - Dora Korpar, 2015-10-19
───────┴───────────────────────────────────────────────────────────
(base) [green@xero 0x00-python-hello_world]$ 
```
- Solution File 1: [100-write.py](./100-write.py)
- Solution File 2: [q](./q)

### 12. Compile
> Write a script that compiles a Python script file.

> The Python file name will be stored in the environment variable `$PYFILE`

> The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)
```
[green@xero 0x00-python-hello_world]$ cat main.py
───────┬────────────────────────────────────────────────────────────
       │ File: main.py
───────┼────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ print("Best School")
───────┴────────────────────────────────────────────────────────────
[green@xero 0x00-python-hello_world]$ export PYILE=main.py
[green@xero 0x00-python-hello_world]$ ./101-compile 
Compiling main.py...
[green@xero 0x00-python-hello_world]$ ls
101-compile  main.py  main.pyc
[green@xero 0x00-python-hello_world]$ cat main.pyc | zgrep -c "Best School"
1
[green@xero 0x00-python-hello_world]$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
0000000 a7 0d 0d 0a 00 00 00 00 96 e0 a5 65 28 00 00 00
0000020 e3 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00
0000040 00 00 00 00 00 f3 1c 00 00 00 97 00 02 00 65 00
0000060 64 00 a6 01 00 00 ab 01 00 00 00 00 00 00 00 00
0000100 01 00 64 01 53 00 29 02 7a 0b 42 65 73 74 20 53
0000120 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69 6e 74 a9
0000140 00 f3 00 00 00 00 fa 07 6d 61 69 6e 2e 70 79 fa
0000160 08 3c 6d 6f 64 75 6c 65 3e 72 06 00 00 00 01 00
0000200 00 00 73 1b 00 00 00 f0 03 01 01 01 e0 00 05 80
0000220 05 80 6d d1 00 14 d4 00 14 d0 00 14 d0 00 14 d0
0000240 00 14 72 04 00 00 00
0000247
[green@xero 0x00-python-hello_world]$ 
```
- Solution FIle: [101-compile](./101-compile)
  - Test File: [main.py](./main.py)
- Compiled File: [main.pyc](./main.pyc)

### 13. ByteCode -> Python #1
- Write the Python function def `magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
  - Tip: [Python bytecode](https://intranet.alxswe.com/rltoken/B38QeZHREbvgq-wY7Ze3vQ)
- Solution File: [102-magic_calculation.py](./102-magic_calculation.py)

<br>

## Repo info:

- **GitHub repository:** [alx-higher_level_programming](../)
- **Directory:** [0x00-python-hello_world](./)
