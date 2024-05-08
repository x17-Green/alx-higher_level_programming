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
[green@xero 0x02-python-import_modules]$ ./3-infinite_add.py
Error: input an int: 0
[green@xero 0x02-python-import_modules]$ ./3-infinite_add.py 79 10
Total sum is = 89
[green@xero 0x02-python-import_modules]$ ./3-infinite_add.py 79 10 -40 -300 89
Total sum is = -162
[green@xero 0x02-python-import_modules]$
```
Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:
```
[green@xero 0x02-python-import_modules]$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
Total sum is = 22222222222222222222222222222222222222222222222222444444444444444444444444444666666666666666666669137800000022222222222222222222222222222222222222222222222222224444444444444444444444444444444444446870935733530887068868444444508888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888889111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111333333333333333333333333333333555555555555555555555555555555777777777777777777777777777777799999999999999999999999979999999999999999998
[green@xero 0x02-python-import_modules]$ 
```
Remember how you did (or did not) do it in C? `#pythoniscool`
![cat_meow](../memes/meow.jpg)

- Solution File: [3-infinite_add.py](./3-infinite_add.py)

<hr>

### `4.` Who are you?
> Write a program that prints all the names defined by the compiled module `hidden_4.pyc` (please download it locally).
- You should print one name per line, in alpha order
- You should print only names that do not start with `__`
- Your code should not be executed when imported
- Make sure you are running your code in Python3.8.x (`hidden_4.pyc` has been compiled with this version)
```
[green@xero 0x02-python-import_modules]$ curl -Lso "hidden_4.pyc" "https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc"
[green@xero 0x02-python-import_modules]$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
[green@xero 0x02-python-import_modules]$ 
```
- Solution File: [4-hidden_discovery.py](./4-hidden_discovery.py)

<hr>

### `5.` Everything can be imported
> Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.
- You are not allowed to use `*` for importing or `__import__`
- Your code should not be executed when imported
```
[green@xero 0x02-python-import_modules]$ cat variable_load_5.py 
───────┬──────────────────────────────────────────────────────────────────────────
       │ File: variable_load_5.py
───────┼──────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ 
   3   │ a = 98
───────┴──────────────────────────────────────────────────────────────────────────
[green@xero 0x02-python-import_modules]$ ./5-variable_load.py 
98
[green@xero 0x02-python-import_modules]$ 
```
- Solution File: [5-variable_load.py](./5-variable_load.py)

<hr>

### `6.` Build my own calculator!
> Write a program that imports all functions from the file `calculator_1.py` and handles basic operations.
- Usage: `./100-my_calculator.py a operator b`
  - If the number of arguments is not 3, your program has to:
    - print `Usage: ./100-my_calculator.py <a> <operator> <b>` followed with a new line
    - exit with the value `1`
  - `operator` can be:
    - `+` for addition
    - `-` for subtraction
    - `*` for multiplication
    - `/` for division
  - If the operator is not one of the above:
    - print `Unknown operator. Available operators: +, -, * and /` followed with a new line
    - exit with the value `1`
  - You can cast `a` and `b` into integers by using `int()` (you can assume that all arguments will be castable into integers)
  - The result should be printed like this: `<a> <operator> <b> = <result>`, followed by a new line
- You are not allowed to use `*` for importing or `__import__`
- Your code should not be executed when imported
```
[green@xero 0x02-python-import_modules]$ cat calculator_1.py 
───────┬──────────────────────────────────────────────────────────────────────────
       │ File: calculator_1.py
───────┼──────────────────────────────────────────────────────────────────────────
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
───────┴──────────────────────────────────────────────────────────────────────────
[green@xero 0x02-python-import_modules]$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py <a> <operator> <b>
1
[green@xero 0x02-python-import_modules]$ ./100-my_calculator.py 3 + 5; echo $?
3 + 5 = 8
0
[green@xero 0x02-python-import_modules]$ ./100-my_calculator.py 3 H 5; echo $?
Unknown operator. Available operators: +, -, * and /
1
[green@xero 0x02-python-import_modules]$ 
```
- Solution File: [100-my_calculator.py](./100-my_calculator.py)

<hr>

### `7.` Easy print
> Write a program that prints `#pythoniscool`, followed by a new line, in the standard output.
- Your program should be maximum 2 lines long
- You are not allowed to use `print` or `eval` or `open` or `import sys` in your file `101-easy_print.py`
```
[green@xero 0x02-python-import_modules]$ ./101-easy_print.py 
#pythoniscool
[green@xero 0x02-python-import_modules]$
```
- Solution File: [101-easy_print.py](./101-easy_print.py)

<hr>

### `8.` ByteCode -> Python #3
> Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
```
(<code object magic_calculation at 0x7f003b224df0, file "102-magic_calculation.py", line 2>)
              2 LOAD_CONST               1 ('magic_calculation')
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (magic_calculation)
              8 LOAD_CONST               2 (None)
             10 RETURN_VALUE


Disassembly of <code object magic_calculation at 0x7f003b224df0, file "102-magic_calculation.py", line 2>:
  3           0 LOAD_CONST               1 (0)
              2 LOAD_CONST               2 (('add', 'sub'))
              4 IMPORT_NAME              0 (magic_calculation_102)
              6 IMPORT_FROM              1 (add)
              8 STORE_FAST               2 (add)
             10 IMPORT_FROM              2 (sub)
             12 STORE_FAST               3 (sub)
             14 POP_TOP

  4          16 LOAD_FAST                0 (a)
             18 LOAD_FAST                1 (b)
             20 COMPARE_OP               0 (<)
             22 POP_JUMP_IF_FALSE       64

  5          24 LOAD_FAST                2 (add)
             26 LOAD_FAST                0 (a)
             28 LOAD_FAST                1 (b)
             30 CALL_FUNCTION            2
             32 STORE_FAST               4 (c)

  6          34 LOAD_GLOBAL              3 (range)
             36 LOAD_CONST               3 (4)
             38 LOAD_CONST               4 (6)
             40 CALL_FUNCTION            2
             42 GET_ITER
        >>   44 FOR_ITER                14 (to 60)
             46 STORE_FAST               5 (i)

  7          48 LOAD_FAST                2 (add)
             50 LOAD_FAST                4 (c)
             52 LOAD_FAST                5 (i)
             54 CALL_FUNCTION            2
             56 STORE_FAST               4 (c)
             58 JUMP_ABSOLUTE           44

  8     >>   60 LOAD_FAST                4 (c)
             62 RETURN_VALUE

 10     >>   64 LOAD_FAST                3 (sub)
             66 LOAD_FAST                0 (a)
             68 LOAD_FAST                1 (b)
             70 CALL_FUNCTION            2
             72 RETURN_VALUE
```
- Solution File: [102-magic_calculation.py](./102-magic_calculation.py)
  - Compilation Command: 
      ```
      [green@xero 0x02-python-import_modules]$ py -m dis 102-magic_calculation.py
      ```
  - Python Version: `Python 3.8.5`
  - OS: `XeroLinux-KDE (Arch)`

<hr>

### `9.` Fast alphabet 
> Write a program that prints the alphabet in uppercase, followed by a new line.
- Your program should be maximum 3 lines long
- You are not allowed to use:
  - any loops
  - any conditional statements
  - `str.join()`
  - any string literal
  - any system calls
```
[green@xero 0x02-python-import_modules]$ ./103-fast_alphabet.py 
ABCDEFGHIJKLMNOPQRSTUVWXYZ
[green@xero 0x02-python-import_modules]$ wc -l 103-fast_alphabet.py 
3 103-fast_alphabet.py
[green@xero 0x02-python-import_modules]$ 
```
- Solution File: [103-fast_alphabet.py](./103-fast_alphabet.py)

<hr>

### Repo Info:
- **GitHub repository:** [alx-higher_level_programming](../README.md)
- **Directory:** [0x02-python-import_modules](./)
