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
