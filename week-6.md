# Lecture 6 Python

## interpreter

## automatically add a space using `,`

    ```python
    answer = get_string("What is your name? ")
    print("Hello," , answer)

    answer = get_string("What is your name? ")
    # f is a format string
    # {} means the value of the variable
    print(f"Hello , {answer}")

    print("hello, answer")
    ```

## types

## trade-off

-   slower than c
-   many built-in functions

## loops

```python
i = 0
while i < 3:
    print("Meow")
    i += 1

# python doesn't have arrays, but has `list`
for i in [1, 2, 3]:
    print("Meow")

for i in range(3):
    print("Meow")

# forever loop
while True:
    print("Meow")
```

## calculator

-   input function
-   convert string to integer
-   1/3 would truncate in C, python avoiding truncation, integer would be converted to a float
-   floating-point imprecision
-   integer overflow

## agree

-   `||` in C, but `or` in python
-   in python, there is no char
-   methods and functions, differences between them
-   `s = s.lower()`. Python automatically free the memory of the old `s`.
<!-- ? what if in C -->
-   [official documentation](https://docs.python.org/)

## meow

-   python is executed line by line. so meow() must be defined first

```python
# This won't work!!!!!!!!
for i in range(3):
    meow()

def meow():
    print("meow")
```

```python
# This is good
def main():
    for i in range(3):
        meow()

def meow():
    print('meow')

main()
```

```python
# This is good
def main():
    meow(3)


def meow(n):
    for i in range(n):
        print('meow')

main()
```

## mario

-   There is no such do...while loop in python, but there is a equivalent while loop:
    ```python
    flag = True
    while flag:
    # code to be executed inside the loop
    # ...
    # check the condition to continue or exit the loop
    if some_condition:
        flag = False
        # or break
    ```
-   key word `try`
-   the `else` keyword in python: not only used in if blocks
-   `print` function in python:
    > there is a default parameter `end='\n'` in python
    ```python
    print('?', end='\n')
    ```
-   ```python
    print('?' * 4)
    ```
-   python does not have pointers
-   ```python
    for i in range(3):
        for j in range(3):
            print('#')
    # same as
    for i in range(3)
        print('#' * 3)
    ```

## List

-   len
-   sum
-   list.append
-   ```python
    scores = []
    score = 5
    scores.append(score)
    # same as
    scores += [score]
    ```
-   `for c in string` and `c.upper()` or `string.upper()`

## sys

-   ```python
    from sys import argv

    for arg in argv:
    print(arg)
    ```

-   if import whole sys library, you need namespace to argv.  
    `sys.exit(1)` and `sys.exit(0)`

    ```python
    import sys

    for arg in sys.argv:
        if len(sys.argv) != 2:
            print("Missing argument")
            # exit(1) means that something went wrong
            sys.exit(1)
        print(arg)
    sys.exit(0)
    ```

## slices of list

-   ```python
    from sys import argv

    for arg in argv[1:]:
    print(arg)
    ```

-   ```python
    from sys import argv

    for arg in argv[0:1]:
    print(arg)
    ```

## `if name in names:`

-   This would just if the name exists in the names list

```python
import sys

if name in names:
    print("Found")
    sys.exit(0)
print("Not found")
sys.exit(1)

```

## dictionary

-   python built-in dictionary
    -   `people = dict()`
    -   `people = {key: value}`
-   Key: Value

    ```python
    people = {
        "Carter": "+1-617-9087",
        "David": "+1-763-9654"
    }
    name = input("Name: ")
    if name in people:
        number = people[name]
        print(f"{name}: {number}")
        exit(0)
    print("Not Found")
    exit(1)
    ```

## compare in Python

-   `==` compares character to character in Python

    ```python
    s=input("s: ")
    t=input("t: ")

    if s == t:
        print("s == t")
    else:
        print("s != t")

    ```

    ```
    (base) huntley@Huntleys-MacBook-Pro (main)✗ % python compare.py                                          ~/learn/cs50/cs50x
    s: cat
    t: cat
    s == t
    (base) huntley@Huntleys-MacBook-Pro (main)✗ %                                                            ~/learn/cs50/cs50x
    (base) huntley@Huntleys-MacBook-Pro (main)✗ % python compare.py                                          ~/learn/cs50/cs50x
    s: Dog
    t: dog
    s != t
    ```

## `t = s.capitalize(0)`

    -   just capitalize the first character
    -   doesn't change the s, it just make a copy of s and modify it.
        ```python
        s=input("s: ")
        t=s.capitalize()
        print(f"s: {s}\nt: {t}")
        ```
        ```
        (base) huntley@Huntleys-MacBook-Pro (main)✗ % python capitalize.py                                       ~/learn/cs50/cs50x
        s: dog
        s: dog
        t: Dog
        ```

## swap

-   just `x,y=y,x`

    ```python
    x = input("x: ")
    y = input("y: ")

    print(f"x is {x} and y is {y}")
    x, y = y, x
    print(f"x is {x} and y is {y}")
    ```

    ```
    (base) huntley@Huntleys-MacBook-Pro (main)✗ % python swap.py                                             ~/learn/cs50/cs50x
    x: 2
    y: 4
    x is 2 and y is 4
    x is 4 and y is 2
    ```

## open file

-   in case of that you forgot to close the file, use `with open("phonebook.csv", "a") as file:`

```python
import csv

file = open("phonebook.csv","a")

name=input("Name: ")
number=input("Number: ")

writer = csv.writer(file)
writer.writerow([name,number])

file.close()
```

```python
import csv

with open("phonebook.csv", "a") as file:
    name = input("Name: ")
    number = input("Number: ")

    writer = csv.writer(file)
    writer.writerow([name, number])
```

-   DictWriter
    > This doesn't have to worry about the order of values  
    
    > ```python
    > writer = csv.DictWriter(file, fieldnames=["name","number"])
    > writer.writerow({"name": name, "number": number})
    > ```
## import pyttsx3
