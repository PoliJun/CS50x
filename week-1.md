# Lecture 0

## Tue May 9 15:57:28 CST 2023

    1. Why use C ?
    use C to know details about the bottom hood
    2. input --> blackbox --> output
    3. unary
        base-1
    4. binary digit --> bit
    5. binary represent numbers. This is smart. (decimal : 1-->10)
        base-2

## Tue May 9 16:10:50 CST 2023

    6. byte : 8 bits
        00000000
    7. ASCII

## Tue May 9 23:20:51 CST 2023

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

-   source code -> compiler -> machine code
-   correctness, design, style
-   say -> printf( "hello,world\n ")  
    ` #include <stdio.h>

int main(void)
{
printf("hello world");

} `if there is no \n ,then `hello world%`

-   `#include <stdio.h>`
    header file
    libraries
    This inform the compiler I want to use the functionality from the Standard I/O Library

## Fri May 12 13:56:03 CST 2023

-   Manual Pages:https://manual.cs50.io

-   `string answer = get_string("What's your name:");`
    there is a return value of get_string
    "=" sign means copy content from right to left
    type is "string"

-   join `printf("hello %s\n",);`

    `string answer = get_string("What is your name? ");`
    `printf("Hello, %s\n", answer);`

-   `string first = get_string("What is your first name? ");`
    `string last = get_string("What is your last name? ");`
    `printf("Hello, %s %s\n", first,last);`

-   you have to delcare first
    `string last = get_string("What is your last name? ");`
    `printf("Hello,  %s\n", first);`

-   use %s as a placeholder has a problem: if i want 100%

-   to solve the problem
    `printf("Hello, 100%%s\n")`
    just double %

-   Types
    bool, string, int,

-   conditionals
    `
        if(x < y){
   printf("hello\n")
}
`

                                if(x < y){

                                }else{

                                }

                                if(x > y){

                                }else if(x < y){{

                                }else{

                                }

-   char:
    double quote "" for string
    single quote '' for single character

-   character is case sensitive in C : 'a' is different to 'A'

-   OR : ||

-   for spaces : for loop
    for( int i = 0; i < 3;i++){
    // states;
    }

-   variables:
    declare with type:
    int x = 5;
    increase
    x = x +1; // this means copy right value to the left
    x++; // increment
    x--; // decrement

## Fri May 12 22:47:09 CST 2023

-   while loop
    `int n = 0;`
    `while (n <3)
{
  printf("meow\n");
}`

-   forever loop
    while(true){

}

## Sat May 13 10:08:24 CST 2023

-   Linux CLI

-   inner for loop

-   Constant
    const x = 5;

-   Comments
    use comments to write pseudo code

-   define a function
    void print_grid(int size)
    {

    }

*   write the function in the head of the file ,this convince the compiler to trust you

*   operators

*   integer overflow

*   format code
    %c %f %i %li %s

*   truncate

*   floating-point imprecision
    `printf("%.20f",z) // twenty decimal point.`

# Section 1

## Tue May 16 09:30:40 CST 2023

### Variables

    `int calls = 4; //4 is the value`
    `calls = 5;`
    Why it's at first line? Because declare first. When you declare and initialize
    a variable, the computer remembers the type of the variable.
    If we want to change the value.

#### asigning a variable.

    function runs first then asings the value to the variable

### Printing the values

    printf("calls is %1\n", calls);

### Types and format codes

    int (%i)    long (%li)   char (%c)
    float (%f)  double (%f)  string(%s)

### Excersize

#### the context
    ```
    int i = 0;
    while (i <10)
    {
        printf("%i\n,i");

    }

    // i in the for loop only can be used in the scope int the for loop
    for(int i = 0; i <10; i++)
    {
        printf("%i\n,i");
    }
    for loop : 
    first roll: do int i = 0, and run the code, then ask if i < 10, if true
    then : when the code run to the end, do i++; then ask if i < 10;

    // This is do while loop. The code run at least one time
    int n;
    do
    {
        n = get_int("n: ");
    }
    while(n <= 0);
    ```
## Fri May 26 10:23:35 CST 2023
### Data Types
* int
    * The int data type is used for variables taht will store integers
    * Integers always take 4 bytes of memory (32 bits) .
    * singned and unsigned integers
* char
    * 1 single character
    * 1 byte
* float
    * floating point values, also known as real numbers
    * 4 bytes of memory
* double
    * floating point values, also known as real numbers
    * 8 bytes of memory
    * more precise real numbers
* void
    * This is not a data type, but a type.
* bool
    * Boolean value: True and false
    * Be sure to #include<cs50.h> atop your programs if you wish to use the bool type
    * in C, bool is not a default dafault data type
* string
    * series of characters
    * be sure to #include<cs50.h> to use string type

* Creating a variable
    * specify the data type and give it a name
        int number;
        char letter;
    * create multiple variables of same type
        int height, width;
        float sqrt2, sqrt3, pi;
    * in general, only declare variables when you need them
    * using a variable
        int number; // delcaration 
        number = 17; // assignment
        char letter = 'h'; // initialization
        you can't redeclare a variable.     

