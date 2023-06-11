# Lecture 4 Memory

## RGB

## Hexadecimal

-   16-based
-   0~f
-   F is 15(decimal) and 1111(binary), and it's 4 bits.
-   prefix 0x

## Pointers

```c
int main()
{
    int n = 50;
    char *s = "HI!";
    int *p = &n;
    printf("%p\n", p);
    printf("%i\n", *p);
    printf("%c\n", *(s + 1));
}
```

-   `&` the address of the variable. This is called "ampersand".
-   `int *p = &n;` means `p` is going to be a pointer
-   `printf("%p\n", p);` means print the address of n, which is &n.
-   `printf("%i\n", *p);` means acctually go there. this prints out `50`
-   **Segment Faults** `printf("%c\n", *(s + 500000000000000990));`

## Pointer Arithmetic

-   how to compare strings?
    > strcmp(s, t) goes into the address , then compares them
-   copy of the address
    > string s = "hi"; string t = s;
-   `strcpy(s, t);` instead

## NULL

In C, `NULL` is a special value that represents a null pointer. A null pointer is a pointer that does not point to any memory location. When we declare a pointer variable but do not initialize it, its value is undefined and it points to some random memory location. In contrast, when we set a pointer variable to `NULL`, it explicitly points to no memory location.

Here is an example:

```c
int *ptr = NULL;

if (ptr == NULL) {
    printf("The pointer is null");
} else {
    printf("The pointer is not null");
}
```

In this example, we declare a pointer variable `ptr` and set it to `NULL`. We then check if the pointer is null using an if statement. Since `ptr` points to no memory location, the condition in the if statement is true, and the program prints "The pointer is null".

In C, `NULL` is defined as a preprocessor macro in the standard header file `stddef.h`. The value of `NULL` is typically defined as 0 or ((void\*)0), but this may vary depending on the implementation.

It is important to note that when using pointers in C, we should always initialize them to `NULL` to avoid undefined behavior. We should also check if a pointer is null before dereferencing it to avoid segmentation faults or other errors.

-   `malloc()` and `free()`

    > you should free after finishing the operation of malloc() memory

    > `malloc` is a standard library function in C that is used to dynamically allocate memory during runtime. The name `malloc` stands for "memory allocation".
    >
    > In C, memory is typically allocated statically or automatically. Static memory allocation is done at compile-time, and the size of the memory block is fixed. Automatic memory allocation is done at runtime, but the size of the memory block is determined by the scope of the variable.
    >
    > Dynamic memory allocation, on the other hand, allows us to allocate memory at runtime, and the size of the memory block can be determined dynamically. This is where `malloc` comes in.
    >
    > The `malloc` function takes a single argument, which is the number of bytes to allocate. It returns a pointer to the first byte of the allocated memory block, which can then be used to store data.
    >
    > Here is an example:
    >
    > ```c
    > int *ptr;
    >
    > ptr = (int*) malloc(5 * sizeof(int));
    >
    > if (ptr == NULL) {
    >     printf("Failed to allocate memory");
    > } else {
    >     // use the allocated memory
    >     ptr[0] = 1;
    >     ptr[1] = 2;
    >     ptr[2] = 3;
    >     ptr[3] = 4;
    >     ptr[4] = 5;
    >
    >     // free the allocated memory when done
    >     free(ptr);
    > }
    > ```

    > In this example, we allocate memory for an array of 5 integers using `malloc`. We then check if the allocation was successful by checking if the returned pointer is `NULL`. If the allocation was successful, we use the allocated memory to store some data. Finally, we free the allocated memory using the `free` function when we are done with it.
    >
    > It is important to note that when using `malloc`, we must always check if the allocation was successful by checking if the returned pointer is `NULL`. If the allocation fails, we should handle the error appropriately. We should also remember to free the allocated memory using the `free` function when we are done with it to avoid memory leaks.

## Memory Leak

In C, a memory leak occurs when a program dynamically allocates memory using functions like `malloc`, `calloc`, or `realloc`, but fails to free the allocated memory when it is no longer needed. This leads to a situation where the program continues to use memory that it does not need, which can cause the program to consume more and more memory over time.

Memory leaks can be a serious problem, especially in long-running programs, because they can cause the program to run out of memory and crash. They can also lead to performance issues, as the program may become slower as it consumes more and more memory.

Here is an example of a memory leak:

```
int *ptr;

while (1) {
    ptr = (int*) malloc(sizeof(int));
    // use the allocated memory, but forget to free it
}
```

In this example, we create a pointer `ptr` to an integer, and then enter an infinite loop where we allocate memory for the integer using `malloc`, but we never free the allocated memory. This means that each time the loop runs, we allocate more memory which we never release. This is a classic example of a memory leak.

To avoid memory leaks in C, it is important to always free dynamically allocated memory when it is no longer needed. This can be done using the `free` function. Here is an example of how to free dynamically allocated memory:

```
int *ptr;

ptr = (int*) malloc(sizeof(int));

if (ptr != NULL) {
    // use the allocated memory
    *ptr = 10;

    // free the allocated memory when done
    free(ptr);
}
```

In this example, we allocate memory for an integer using `malloc`, and then check if the allocation was successful. If the allocation was successful, we use the allocated memory to store a value, and then free the allocated memory using the `free` function when we are done with it. This ensures that the program does not leak memory and avoids potential memory-related issues.

## Garbage Values

If there is no allocation, the addressed location has undefined values. These values are garbage values.

## Regions of memory

![Alt text](pictures/cs50Week4Slide163.png)

> In C, there are typically three regions of memory: the code/text segment, the stack, and the heap.
>
> 1. Code/Text Segment: This is a read-only region of memory where the compiled code of the program is stored. It contains the instructions that the processor executes when the program is run. This region is typically located at the lowest memory address.
>
> 2. Stack: This is a region of memory that is used to store variables and function call information. When a function is called, a new stack frame is created to store the function's local variables and other information. Each stack frame is placed on top of the previous one, creating a stack-like structure. When a function returns, its stack frame is removed from the stack, and the program resumes execution from the previous stack frame. Variables stored in the stack are automatically deallocated when the stack frame is removed.
>
> 3. Heap: This is a region of memory that is used for dynamic memory allocation. In C, we can use functions like `malloc`, `calloc`, and `realloc` to allocate memory on the heap. The memory that is allocated on the heap is not automatically deallocated, and we must use the `free` function to deallocate it when it is no longer needed. Variables stored in the heap persist even after the function that allocated them has returned.
>
> It is important to note that the exact number and size of memory regions may vary depending on the compiler and operating system being used. Additionally, some systems may have additional memory regions, such as the data segment, the bss segment, or the stack guard. However, the three regions described above are the most common in C programming.

-   stack is in the function
-   heap is unallocated locations.

    `void swap(int a, int b);` As for this, a and b are copies of the values.

You should write like this, which will goes into the location:

```c
void swap(int *a, int *b);
```

This is the whole code:

```c
#include <stdio.h>

void swap(int *a, int *b);

int main()
{
    int x = 1;
    int y = 2;

    printf("x is %d, y is %d\n", x, y);
    swap(&x, &y);
    printf("y is %d, x is %d\n", x, y);
}

void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
```

## buffer overflow, heap overflow and stack overflow

> Buffer overflow, heap overflow, and stack overflow are all types of memory-related vulnerabilities that can occur in software applications.
>
> 1. Buffer Overflow: A buffer overflow occurs when a program attempts to write data to a buffer that is too small to hold the data. This can result in the data being written to adjacent memory locations, which can cause the program to crash or behave unpredictably. In some cases, an attacker can exploit a buffer overflow vulnerability to execute arbitrary code on the system or to gain elevated privileges. Buffer overflows can occur in both the stack and the heap.
>
> 2. Heap Overflow: A heap overflow occurs when a program attempts to allocate more memory on the heap than is available. This can cause the program to overwrite adjacent memory locations, which can cause the program to crash or behave unpredictably. In some cases, an attacker can exploit a heap overflow vulnerability to execute arbitrary code on the system or to gain elevated privileges.
>
> 3. Stack Overflow: A stack overflow occurs when a program attempts to allocate more memory on the stack than is available. This can occur when a function calls itself recursively, or when a program attempts to create too many nested function calls. This can cause the program to crash or behave unpredictably. In some cases, an attacker can exploit a stack overflow vulnerability to execute arbitrary code on the system or to gain elevated privileges.
>
> To prevent these types of vulnerabilities, it is important to use secure coding practices, such as validating input data, using bounds checking when copying data to buffers, and using memory-safe programming languages or libraries. Additionally, it is important to keep software applications up to date with the latest security patches and to conduct regular security testing to identify and address vulnerabilities.

### Undefined Behavior

> In the code above, the scanf function is writing more than one byte of data to the s array, which is an array of size 1. This is called a buffer overflow and it is undefined behavior. It means that the program might appear to run correctly, but there is no guarantee that it will. In this case, the behavior of the program is indeed undefined, so it might crash with segmentation fault, it might produce wrong results or it might seem to run correctly.
>
> The fact that you don't get a segmentation fault when running this code might be due to the following reasons:
>
> The memory location immediately after the s array might have been reserved for another variable, so the scanf function overwrites that variable instead of corrupting the program's memory.
> The s array might be located in an area of memory that is not protected by the operating system, so the program is allowed to write beyond its boundaries without causing a segmentation fault. However, this is still undefined behavior and should be avoided.
>
> In general, it is important to always allocate enough memory for the data you are working with and to use safe programming practices to avoid undefined behavior.
