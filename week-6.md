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
