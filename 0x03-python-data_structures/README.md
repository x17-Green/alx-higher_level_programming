# 0x03. Python - Data Structures: Lists, Tuples

:gear: Weight: 1

:calendar: Project over - took place from Jan 5, 2024 6:00 AM to Jan 9, 2024 6:00 AM

:ballot_box_with_check: An auto review will be launched at the deadline

# Learning Resources
### Read or watch:
1. [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
1. [Data structures](https://docs.python.org/3/tutorial/datastructures.html) (until `5.3. Tuples and Sequences` included)
1. [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw&themeRefresh=1)

# Learning Objectives
> At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

## General
- Why Python programming is awesome
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the `del` statement and how to use it

## Copyright - Plagiarism
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

## C
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- Your code should use the `Betty` style. It will be checked using `betty-style.pl` and `betty-doc.pl`
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded

# Tasks

### `0.` Print a list of integers
> Write a function that prints all integers of a list.
- Prototype: `def print_list_integer(my_list=[]):`
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers
```
[green@xero 0x03-python-data_structures]$ cat 0-main.py 
───────┬───────────────────────────────────────────────────────────────────────────────────
       │ File: 0-main.py
───────┼───────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ print_list_integer = __import__('0-print_list_integer').print_list_integer
   3   │ 
   4   │ my_list = [1, 2, 3, 4, 5]
   5   │ print_list_integer(my_list)
───────┴───────────────────────────────────────────────────────────────────────────────────
[green@xero 0x03-python-data_structures]$ ./0-main.py 
1
2
3
4
5
[green@xero 0x03-python-data_structures]$ 
```
- Function File: [0-print_list_integer.py](./0-print_list_integer.py)
  - Test File: [0-main.py](./0-main.py)

<hr>

### `1.` Secure access to an element in a list
> Write a function that retrieves an element from a list like in C.
- Prototype: `def element_at(my_list, idx):`
- If `idx` is negative, the function should return `None`
- If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
- You are not allowed to import any module
- You are not allowed to use `try/except`
```
[green@xero 0x03-python-data_structures]$ cat 1-main.py 
───────┬─────────────────────────────────────────────────────────────────────
       │ File: 1-main.py
───────┼─────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ element_at = __import__('1-element_at').element_at
   3   │ 
   4   │ my_list = [1, 2, 3, 4, 5]
   5   │ idx = 3
   6   │ print("Element at index {:d} is {}".format(idx, element_at(my_list, 
       │ idx)))
   7   │ 
───────┴─────────────────────────────────────────────────────────────────────
[green@xero 0x03-python-data_structures]$ ./1-main.py 
Element at index 3 is 4
[green@xero 0x03-python-data_structures]$ 
```
- Function File: [1-element_at.py](./1-element_at.py)
  - Test File: [1-main.py](./1-main.py)

<hr>

### `2.` Replace element
> Write a function that replaces an element of a list at a specific position (like in C).
- Prototype: `def replace_in_list(my_list, idx, element):`
- If `idx` is negative, the function should not modify anything, and returns the original list
- If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
- You are not allowed to import any module
- You are not allowed to use `try/except`
```
[green@xero 0x03-python-data_structures]$ cat 2-main.py 
───────┬─────────────────────────────────────────────────────────────────────
       │ File: 2-main.py
───────┼─────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ replace_in_list = __import__('2-replace_in_list').replace_in_list
   3   │ 
   4   │ my_list = [1, 2, 3, 4, 5]
   5   │ idx = 3
   6   │ new_element = 9
   7   │ new_list = replace_in_list(my_list, idx, new_element)
   8   │ 
   9   │ print(new_list)
  10   │ print(my_list)
  11   │ 
───────┴─────────────────────────────────────────────────────────────────────
[green@xero 0x03-python-data_structures]$ ./2-main.py 
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
[green@xero 0x03-python-data_structures]$ 
```
- Function File: [2-replace_in_list.py](./2-replace_in_list.py)
  - Test File: [2-main.py](./2-main.py)

<hr>

### `3.` Print a list of integers... in reverse! 
> Write a function that prints all integers of a list, in reverse order.
- Prototype: def `print_reversed_list_integer(my_list=[]):`
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers
```
[green@xero 0x03-python-data_structures]$ cat 3-main.py 
───────┬─────────────────────────────────────────────────────────────────────
       │ File: 3-main.py
───────┼─────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ print_reversed_list_integer = __import__('3-print_reversed_list_inte
       │ ger').print_reversed_list_integer
   3   │ 
   4   │ my_list = [100, 200, 300, 400, 500]
   5   │ print_reversed_list_integer(my_list)
   6   │ 
───────┴─────────────────────────────────────────────────────────────────────
[green@xero 0x03-python-data_structures]$ ./3-main.py 
500
400
300
200
100
[green@xero 0x03-python-data_structures]$ 
```
- Function File: [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py)
  - Test File: [3-main.py](./3-main.py)

<hr>

###
