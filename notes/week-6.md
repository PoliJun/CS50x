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

# Section 6

## Methods

-   `text.strip()`
-   `text.lower()` and `text.capitalize()` and `text.upper()`
-   dot syntax

## loops in python

-   ```python
      for c in string:
      print(c)
    ```
-   ```python
    words = text.split()
    for word in words:
        print(word)
    ```
-   for in loops the data type in a list
-   `if word in words`
-   `for word in words[2:]`
-   `for word in words[1:5]`
-   ```python
    for word in words:
        if "g" in word:
            print(word)
    ```
-   ```python
    # underscore means that the variable name doesn't matter
    for _ in words:
        print("Goodnight!")
    print()
    ```

## Dictionary

-   ```python
    book = dict()
    book["title"] = "Corduroy"
    book["author"] = "Don Freeman"
    print(book["title"])

    # Corduroy
    ```

-   A list of dictionaries
    ```python
    [{"title": "Corduroy", "author": "Don Freeman"},{"title": "Goodnight", "Author": "Rowlin"} ]
    ```
-   Add dictionaries to a list

    ```python
    books=[]

    # Add three books to your shelf
    for i in range(3):
        book=dict()
        book['title']=input("Enter title of book: ").strip().Capitalize()
        book['author']=input("Enter author of book: ").strip().Capitalize()

        books.append(book)

    for book in books:
        print(book['title'])
    ```

## Libraries and Module

-   csv modules
-   `with open("books.csv") as file:` and then indent at the new line, without indent, the file would be closed.
-   `text = file.read()`, then we don't need to `import csv`, but this is not useful
-   `file_reader = csv.DictReader(file)`
-   add dictionary to the list

# Shorts

## python

### Python Syntax

-   Variables
    -   Must initialize when to use a variable, but without data type declaration
-   Conditionals
    -   `or`
    -   `elif`
    -   `letters_only = True if input().isalpha() else False`
-   Loops
    -   while loop
        ```python
        counter = 0
        while counter < 100:
            print(counter)
            counter += 1 # There is no i++ syntax in Python
        ```
    -   for loop
        ```python
        # range() function, start point, end point, skip by point
        for i in range(0, 100,2):
            print(i)
        ```
        > This is corresponding to the following
        ```java
        for(int i = 0; i < 100; i += 2){
            print(i)
        }
        ```
-   lists
    > There is no arrays in Python, but there are lists
    - initialize a list
        > `nums = []`  
        > `nums = [x for x in range(500)]`  
        > `nums = list()`
    - methods
        > `nums.insert(4, 5)`. This would insert 5 at the forth position
        > `nums.append(5)`. This would append 5 at the end of the list.
        > `nums[len(nums):] = [5]`. This would append 5 at the end of the list.
- Tuples
    > Imutable set of data
    ```python
    presidents = [
        ("George Washington", 1789),
        ("John Adams", 1797),
        ("Thomas Jefferson", 1801)
    ]
    for prez, year in presidents:
        print("In {1}, {0} took office".format(prez, year))
        # same as 
        print(f"In {year}, {prez} took office")   
    ```
- Dictionary
    - currly brackets `{}`
    - `key:value` pairs
    - Loops in dictionary
        > We don't have index likely in C    
        > ```python
        > for pie in pizzas:
        >     print(pie) # this prints all the keys in pizzas
        > for pie, price in pizzas.items(): # pizzas.items() method returns a list of tuple pairs.
        >     print(price) # this prints out values, but this is not maintain the original order.
        > for pie, price in pizzas.items():
        >     print("A whole {} pizza costs ${}".format(pie, price)) # This would be fine.
        > ```
- functions
    - don't need to specify the return type, nor the data type of any parameters.
    - All functions are introduced with the `def` key word.
    - if you want to define main nonetheless, you must at the very end of your code have:
        ```python
        if __name__ == '__main__':
            main()
        ```
- Objects
    - We don't pass objects into functions as parameters, we call methods on objects: `obj.method()`.
    - `class` keyword: create a new kind of object
    - In defining each method of an object, self should be its first parameter, which stipulates on what object the method is called.
- style
    - good style is crucial in Python
    - **tabs** and **indentation** actually matter in this language
    - No more curly braces to delineate blocks
- including files
    - `import module`
- python command line
- your program will run through the interpreter, which will execute everything inside of the file, top to bottom