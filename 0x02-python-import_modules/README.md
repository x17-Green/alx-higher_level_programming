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
```
[green@xero 0x02-python-import_modules]$ cat add_0.py 
───────┬────────────────────────────────────────────────────────────────────────────────────
       │ File: add_0.py
───────┼────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ def add(a, b):
   3   │     return (a + b)
───────┴────────────────────────────────────────────────────────────────────────────────────
[green@xero 0x02-python-import_modules]$ ./0-add.py 
1 + 2 = 3
[green@xero 0x02-python-import_modules]$ 

```
- Solution File: [0-add.py](./0-add.py)
  - Module File: [add_0.py](./add_0.py)

<hr>

### `1.` My first toolbox!
> Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.
- Do not use the function `print` (with string format to display integers) more than 4 times
- You have to define:
  - the value `10` to a variable `a`
  - the value `5` to a variable `b`
  - and use those two variables only, as arguments when calling functions (including `print`)
- `a` and `b` must be defined in 2 different lines: `a = 10` and another `b = 5`
- Your program should call each of the imported functions. See example below for format
- the word `calculator_1` should be used only once in your file
- You are not allowed to use `*` for importing or `__import__`
- Your code should not be executed when imported
```
[green@xero 0x02-python-import_modules]$ cat calculator_1.py 
───────┬───────────────────────────────────────────────────────────────────────────────────────────
       │ File: calculator_1.py
───────┼───────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ def add(a, b):
   3   │     return (a + b)
   4   │ 
   5   │ 
   6   │ def sub(a, b):
   7   │     return (a - b)
   8   │ 
   9   │ 
  10   │ def mul(a, b):
  11   │     return (a * b)
  12   │ 
  13   │ 
  14   │ def div(a, b):
  15   │     return int(a / b)
───────┴───────────────────────────────────────────────────────────────────────────────────────────
[green@xero 0x02-python-import_modules]$ ./1-calculation.py 
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
[green@xero 0x02-python-import_modules]$
```
- Solution File: [1-calculation.py](./1-calculation.py)
  - Module File: [calculator_1.py](./calculator_1.py)

<hr>

### `2.` How to make a script dynamic!
> Write a program that prints the number of and the list of its arguments.
- The output should be:
  - Number of argument(s) followed by `argument` (if number is one) or `arguments` (otherwise), followed by
  - `:` (or `.` if no arguments were passed) followed by
  - a new line, followed by (if at least one argument),
  - one line per argument:
    - the position of the argument (starting at `1`) followed by `:`, followed by the argument value and a new line
- Your code should not be executed when imported
- The number of elements of `argv` can be retrieved by using: `len(argv)`
- You do not have to fully understand lists yet, but imagine that `argv` can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.
```
[green@xero 0x02-python-import_modules]$ ./2-args.py
0 arguments.
[green@xero 0x02-python-import_modules]$ ./2-args.py Hello
1 argument:
1: Hello
[green@xero 0x02-python-import_modules]$ ./2-args.py Hello This is My Python Argument Project File
8 arguments:
1: Hello
2: This
3: is
4: My
5: Python
6: Argument
7: Project
8: File
[green@xero 0x02-python-import_modules]$
```
- Solution File: [2-args.py](./2-args.py)

<hr>

### `3.` Infinite addition
> Write a program that prints the result of the addition of all arguments
- The output should be the result of the addition of all arguments, followed by a new line
- You can cast arguments into integers by using `int()` (you can assume that all arguments can be casted into integers)
- Your code should not be executed when imported
```
```
Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:
```

```
Remember how you did (or did not) do it in C? `#pythoniscool`
![cat_meow](../memes/meow.jpg)

- Solution File: []()
