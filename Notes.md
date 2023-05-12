# Lecture 0
## Tue May  9 15:57:28 CST 2023
    1. Why use C ?
    use C to know details about the bottom hood
    2. input --> blackbox --> output
    3. unary 
        base-1
    4. binary digit --> bit
    5. binary represent numbers. This is smart. (decimal : 1-->10)
        base-2

## Tue May  9 16:10:50 CST 2023
    6. byte : 8 bits
        00000000
    7. ASCII

## Tue May  9 23:20:51 CST 2023
    8. UNICODE
    9. type : numbers or string 
    10. RGB
    11. the blackbox is abstraction: you don't have to consider the most underneath hood , you think at high level
    12. algorithm: how you solve the problem
    13. pseudocode: (step by step)
        first setp: Pick up phone book
        second setp: Open to middle of phone book
        third setp: Look at page
        fourth setp: If person is on page
                        fifth setp: Call the person

## Wed May 10 00:28:51 CST 2023

                    Else if person is earlier in book
                        fifth step: Open to middle of left half of phone book
                                    go back to line 3
                    Else if person is later in book
                        fifth step: Open to middle of right half of phone book
                                    go back to line 3
                    Else 
                        fifth step: Quit
    14. The actions of verbs are functions
    15. The "if"s are conditional
    16. The words after if are boolean expressions --> Y or N, 1 or 0, true or false
    17. "Go back" is a loop
    18. functions
            arguments , return values
        conditions
        boolean expressions
        loops
        variables
        ...
        all would be compiled to 01010101010101
        so, the 01010101101 are not just "hello world", but also verbs
    19. We don't have to write 0101010, because ancestors solved this problem.
        We can use high level languages like C
    20. https://scratch.mit.edu/
    
## Wed May 10 01:37:43 CST 2023

    21. event(click), function(say),"hello"(parameter)
    22. input --> ALGORITHM --> output

## Wed May 10 09:28:03 CST 2023

    23. compound function
    24. make a block.

## Wed May 10 09:57:59 CST 2023

    25. control : forever

    26. 


# Lecture-1 C

## Thu May 11 10:19:13 CST 2023

* source code -> compiler -> machine code
* correctness, design, style
* say -> printf( "hello,world\n ")         
` #include <stdio.h>

int main(void)
{
    printf("hello world");

} `
if there is no \n ,then 
`hello world%` 

* `#include <stdio.h>`
    header file 
        libraries
    This inform the compiler I want to use the functionality from the Standard I/O Library

## Fri May 12 13:56:03 CST 2023

* Manual Pages:https://manual.cs50.io

* `string answer = get_string("What's your name:");` 
    there is a return value of get_string 
    "=" sign means copy content from right to left
    type is "string"

* join `printf("hello %s\n",);`

    `string answer = get_string("What is your name? ");`
    `printf("Hello, %s\n", answer);`

*   `string first = get_string("What is your first name? ");`
    `string last = get_string("What is your last name? ");`
    `printf("Hello, %s %s\n", first,last);`

* you have to delcare first
    `string last = get_string("What is your last name? ");`
    `printf("Hello,  %s\n", first);`