# 0x01. Python - if/else, loops, functions

:teacher: By: Guillaume

:gear: Weight: 1

:calendar: Project over - took place from Jan 2, 2024 6:00 AM to Jan 3, 2024 6:00 AM

:ballot_box_with_check: An auto review will be launched at the deadline

![code](./code.png)

### In a nutshell…
- Auto QA review: 0.0/160 mandatory & 0.0/41 optional
- Altogether:  0.0%
  - Mandatory: 0.0%
  - Optional: 0.0%
  - Calculation:  0.0% + (0.0% * 0.0%)  == 0.0%

# Learning Resources
### Read or watch:
1. [More Control Flow Tools](https://intranet.alxswe.com/rltoken/jpjs5EnZTpBLLEremJYjPQ) (Read until “4.6. Defining Functions” included)
1. [IndentationError](https://intranet.alxswe.com/rltoken/F9n2AE-fpEPzt2PfBMGYAQ)
1. [How To Use String Formatters in Python 3](https://intranet.alxswe.com/rltoken/ZdtRIAkFu8dMBT99DcFBNg)
1. [Learn to Program](https://intranet.alxswe.com/rltoken/ElQgZYNHrLI7kV_ysEB1hQ)
1. [Learn to Program 2 : Looping](https://intranet.alxswe.com/rltoken/ElQgZYNHrLI7kV_ysEB1hQ)
1. [Pycodestyle – Style Guide for Python Code](https://intranet.alxswe.com/rltoken/TuTTnEg_Rwn8U1g3PEsZmA)

### man or help:
- `python3`

# Learning Objectives
> At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/SdBJUMTPS5VW3cQNkhaeSg), without the help of Google:

## General
- Why Python programming is awesome
- Why indentation is so important in Python
- How to use the `if`, `if ... else` statements
- How to use comments
- How to affect values to variables
- How to use the `while` and `for` loops
- How is Python’s `for` different from `C`‘s?
- How to use the `break` and `continues` statements
- How to use `else` clauses on loops
- What does the `pass` statement do, and when to use it
- How to use `range`
- What is a function and how do you use functions
- What does return a function that does not use any `return` statement
- Scope of variables
- What’s a traceback
- What are the arithmetic operators and how to use them

### Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

# Requirements
## Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

## C Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using `gcc`, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- All your files should end with a new line
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called lists.h
- Don’t forget to push your header file
- All your header files should be include guarded

# More Info
> Note: you do not need to understand lists yet.

<hr>

# Tasks

### `0.` Positive anything is better than negative nothing 
> This program will assign a random signed `number` to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.

- You can find the source code [here](https://intranet.alxswe.com/rltoken/e4tR3cjFHqhelf4y485-zQ)
- The variable `number` will store a different value every time you will run this program
- You don’t have to understand what `import`, `random.randint` do. Please do not touch this code
- The output of the program should be:
  - The number, followed by
    - if the number is greater than 0: `is positive`
    - if the number is 0: `is zero`
    - if the number is less than 0: `is negative`
  - followed by a new line
```
[green@xero 0x01-python-if_else_loops_functions]$ ./0-positive_or_negative.py 
-5 is negative
[green@xero 0x01-python-if_else_loops_functions]$ ./0-positive_or_negative.py 
0 is zero
[green@xero 0x01-python-if_else_loops_functions]$ ./0-positive_or_negative.py 
-1 is negative
[green@xero 0x01-python-if_else_loops_functions]$ ./0-positive_or_negative.py 
-3 is negative
[green@xero 0x01-python-if_else_loops_functions]$ ./0-positive_or_negative.py 
-7 is negative
[green@xero 0x01-python-if_else_loops_functions]$ ./0-positive_or_negative.py 
3 is positive
[green@xero 0x01-python-if_else_loops_functions]$ ./0-positive_or_negative.py 
1 is positive
[green@xero 0x01-python-if_else_loops_functions]$ ./0-positive_or_negative.py 
-2 is negative
[green@xero 0x01-python-if_else_loops_functions]$ ./0-positive_or_negative.py 
3 is positive

```
- Solution File: [0-positive_or_negative.py](./0-positive_or_negative.py)

<hr>

### `1.` The last digit
> This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.
- You can find the source code [here](https://intranet.alxswe.com/rltoken/Vku0ZPFeDPuXUKD8nZ4mOQ)
- The variable `number` will store a different value every time you will run this program
- You don’t have to understand what `import`, `random.randint` do. **Please do not touch this code**. This line should not change: `number = random.randint(-10000, 10000)`
- The output of the program should be:
  - The string `Last digit of`, followed by
  - the number, followed by
  - the string `is`, followed by the last digit of `number`, followed by
    - if the last digit is greater than 5: the string `and is greater than 5`
    - if the last digit is 0: the string `and is 0`
    - if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
  - followed by a new line
```
[green@xero 0x01-python-if_else_loops_functions]$ ./1-last_digit.py 
Last digit of 2868 is 8 and is greater than 5
[green@xero 0x01-python-if_else_loops_functions]$ ./1-last_digit.py 
Last digit of -7412 is -2 and is less than 6 and not 0
[green@xero 0x01-python-if_else_loops_functions]$ ./1-last_digit.py 
Last digit of 6524 is 4 and is less than 6 and not 0
[green@xero 0x01-python-if_else_loops_functions]$ ./1-last_digit.py 
Last digit of 6822 is 2 and is less than 6 and not 0
[green@xero 0x01-python-if_else_loops_functions]$ ./1-last_digit.py 
Last digit of 4230 is 0 and is 0
[green@xero 0x01-python-if_else_loops_functions]$ ./1-last_digit.py 
Last digit of 1916 is 6 and is greater than 5
[green@xero 0x01-python-if_else_loops_functions]$ ./1-last_digit.py 
Last digit of -7951 is -1 and is less than 6 and not 0
[green@xero 0x01-python-if_else_loops_functions]$ ./1-last_digit.py 
Last digit of 3077 is 7 and is greater than 5
[green@xero 0x01-python-if_else_loops_functions]$ ./1-last_digit.py 
Last digit of -8720 is 0 and is 0
[green@xero 0x01-python-if_else_loops_functions]$ ./1-last_digit.py 
Last digit of -6059 is -9 and is less than 6 and not 0
[green@xero 0x01-python-if_else_loops_functions]$ ./1-last_digit.py 
Last digit of -6237 is -7 and is less than 6 and not 0
```
- Solution File: [1-last_digit.py](./1-last_digit.py)

<hr>

### `2.` 
