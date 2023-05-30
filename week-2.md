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
