# Lecture 2 Arrays

## Compiler

-   clang

    > `clang -o hello hello.c`. the `-o` means output  
    > `clang -o hello hello.c -lcs50`. tell the compiler to use libraries with `-l`

-   gcc

## 4 Steps of Compiling

-   preprocessing

    > This is what `#include <stdio.h>` do.
    > It copies the source maggically to the destination.  
    > The `get_string()` function delcared in `cs50.h`  
    > `/usr/include` includes `stdio.h` and `cs50.h`

-   compiling

    > compile C into Assembly language

-   assembling

    > convert into acctual binary (0101010101)

-   linking

    > take the binary code all together (cs50.h and your .c files)

## Decompiling

> binary code back to C source code.  
> Decompiled code is not identical to the original source code. While most of the functionality and logic can be reconstructed, the decompiled code may have differences in style, white space, naming conventions, comments, and formatting. Additionally, some high-level structures in the original source code, such as loop unrolling or compiler optimizations, may not be apparent or accurately reconstructed in decompiled code.

## Debug Code

-   printf debugging output
-   debug with software

    > step over  
    > step in  
    > step out

-   undebugging

    >

-   Three ways to debug
    -   printf
    -   debugger
    -   rubber duck

## Array

-   memory is contiguous
-   magic numbers
-   You can't figure out the size of an array in C.
-   strings are arrays

## C Libraries

-   string.h

    ```C
    int n = strlen(name);
    ```

    This is achieved by for loop

-   ctype.h

    ```C
     #include <cs50.h>
     #include <stdio.h>
     #include <string.h>

     int main(void)
     {
     string s = get_string("Before: ");
     printf("After: ");
     for (int i = 0; i < strlen(s); i++)
     {
     if (s[i] >= 'a' && s[i] <= 'z')
     {
     printf("%c", s[i] - 32);
     }
     else
     {
     printf("%c", s[i]);
     }
     }
     printf("\n");
     }
    ```

    This is how it is achieved,  
    then we include the ctype.h library:

    ```C
    #include <cs50.h>
    #include <ctype.h>
    #include <stdio.h>
    #include <string.h>

    int main(void)
    {
     string s = get_string("Before: ");

     printf("After: ");
     //declare an variable to store strlen(s), then there is no need to execute the function over and over again
    for (int i = 0, /**i < strlen(s)*/ n = strlen(s); i < n; i++)
     {
         printf("%c", toupper(s[i]));
     }
     printf("\n");
    }
    ```

## Command Line Arguments

```C
#include <cs50.h>
// #include <ctype.h>
#include <stdio.h>
// #include <string.h>

int main(int argc,string argv[])
{
    // string name = get_string("What is your name? ");
    // printf("hello, %s\n", name);

    printf("hello, %s\n",argv[1]);
}
```

`$ ./greet David`  
The output: `hello, David`

## Exit Status

The exit status is a numerical value returned by a command or a program when it completes its execution.

> int retruns 0 in C in which how C is designed, we just don't see it on the screen

-   `echo $`

    -   explained
        > In Unix/Linux shell scripting, the dollar sign ($) is used to reference the value of a variable.
        >
        > When you use the command `echo $`, it will not display anything because `$` is not a variable name. However, if you add a variable name after the `$`, like `echo $var`, it will display the value of the variable `var`.
        >
        > For example, if you have defined a variable named `name` and assigned it a value of "John", running the command `echo $name` will display "John" in the terminal.
        >
        > Overall, the `$` symbol is used to reference the value of a variable in shell scripting.
    -   `echo $?` explained:

        > In Unix/Linux shell scripting, the `echo $?` command is used to display the exit status of the last command that was executed.
        >
        > When a command or program is executed, it returns an exit code or exit status. This exit code is a numerical value that indicates whether the command was successful or not. A value of 0 means that the command was successful, while any other value indicates an error or failure.
        >
        > The `$?` variable is a special shell variable that holds the exit status of the last command executed. When you run the `echo $?` command, it displays the value of the `$?` variable, which is the exit status of the last command that was executed.
        >
        > For example, if you run the `ls` command, which lists the files and directories in the current directory, and then run `echo $?`, it will display the exit status of the `ls` command. If the `ls` command was successful, the exit status will be 0, and `echo $?` will display 0. If the `ls` command encountered an error, the exit status will be a non-zero value, and `echo $?` will display that value.
        >
        > Overall, `echo $?` is a useful command for debugging shell scripts and checking the exit status of commands or programs that were previously executed.

## cryptography

-   encryption

    > plaintext and key --> cipher --> ciphertext

-   decryption
    > ciphertext and key --> decryption --> plaintext

# Section 2

## Think. Pair. Share.

-   What are the steps involved in compilation
    > how comiled into binary code : first into assembly code
    > `$ clang -o hello hello.c`
-   What are arrays?
    > types matters for how much memory to allocate to
    > `int hours[5]`: name, size, type
    1. declare an array
    2. set the first
-   What are strings?
    > 32 upper to lower
-   What's the point of command-line arguments?
    > arv[] argument vector
-   What makes for good design?

# Shorts

## Functions

-   What is a function
    -   A black box with a set of 0+ inputs and 1 output
        > int func(a,b,c) {return 0 }
    -   Why call it a black box
        -   if we aren't writing the functions ourselves, we don't need to know the underlying implementation.
        -   That's part of the contract of using functions. The behavior is typically predicatable based on that name.That's why most functions have clear, obvious(ish) names, and are well-documented.
-   Why use functions?
    -   Organization
        -   functions help break up a complicated problem into more manageable subparts.
    -   Simplification
        -   Smaller components tend to be easier to design, implement, and debug.
    -   Reusability
        -   Functions can be recycled; you only need to write them once, but can use them as often as you need!
-   Function Declarations

    -   The first step to creating a function is to declare it. This gives the compiler a heads-up that a user-written function appears in the code.

        > return-type name(argument-list);

        ```C
        int add_two_ints(int a, int b);
        ```

    -   Function delarations should always go atop your code, before you begin writing main().
    -   There is a standard form that every function declaration follows.

-   A function to mutltiple two floating point numbers.

    ```C
    float mult_two_reals(float a, float b); // the semicolon indicates that that is a function delaration.

    float mul_two_reals(float a, float b)
    {
        float product = x * y;
        return product; // we can just return x * y
    }
    ```

-   Function calls
-   Function Miscellany

## Variable Scope

-   Scope is a characteristic of a variable that defines from which functions that variable may be accessed.
    -   Local variables can only be accessed within the functions in which they are created.
    -   Global variables can be accessed by any function in the program.
-   Why does this distinction matter? For the most part, local variables in C are passed by value in fuction calls.
-   When a variable is passed by value, the callee receives a copy of the passed variable, not the variable itself. **THIS IS VERY IMPORTANT**
-   That means that the variable in the caller is unchanged unless overwritten.

## Debugging("Step through")

-   `debug50`
-   setp over

## Duplicate of 'Debugging("setp into")'

-   step into the function to see the details

## Arrays

-   Arrays are a fundamental **data structure**, and they are extremely useful!
-   We use arrays to hold values of the same type at contiguous memory locations.
-   One way to analogize the notion of array is to think of your local post office, which usually has a large bank of post office boxes.
-   In C, the elements of an array are indexed starting from 0.
-   If an array consists of n elements, the first element is located at index 0 and the last element is located at index (n-1).
-   C is lenient. **IT WILL NOT PREVENT YOU FROM GOING "OUT OF BOUNDS" OF YOUR ARRAY; BE CAREFUL!**
-   Array declarations: **type, name, size.**
    -   instantiation declarations
    -   individual element syntax
-   Arrays can consist of more than a single dimension.
    ```C
    bool battleship[10][10];
    ```
-   While we can treat individual elements of arrays as variables, we cannot treat entire arrays themselves as variables.
-   We cannot, for instance, assign one array to another using the assignment operator. That is not legal C.
-   Instead, we must use a loop to copy over the elements one at a time.
-   Pass by value:
    -   Recall that most variables in C are **passed by value** in function calls.
    -   Arrays do not follow this rule. Rather, they are **passed by reference**. The callee receives the actual array, not a copy of it.
        -   What does it mean when the callee manipulates elements of the array?

## Command Line Arguments

-   To collect so called **command-line arguments** from the user, declare main as:

    ```C
    int main(int argc, string argv[])
    {

    }
    ```

-   This two special arguments enable you to know what data the user provided at the command line and how much data they provided.
