# Lecture 3 Algorithms

## Algorithm

-   For each . This is **Linear Search**
-   Binary Search
    -   should be sorted
    -   pseudo code:
        ```
        If no doors left
            Return false
        If 50 is behind doors[middle]
            Return true
        Else if 50 < doors[middle]
            Search doors[0] through doors[middle - 1]
        Else if 50 > doors[middle]
            Search doors[middle + 1] through doors[n - 1]
        ```

## Running Time

-   Worst cases **O**

    > $$
    > \begin{align}
    > O(n^{2}) \\
    > O(n\ log\ n)  \\
    > O(n) \\
    > O(log\ n) \\
    > O(1) \\
    > \end{align}
    > $$

-   Best cases **Ω**

    > $$
    > \begin{align}
    > Ω(n^{2}) \\
    > Ω(n\ log\ n)  \\
    > Ω(n) \\
    > Ω(log\ n) \\
    > Ω(1) \\
    > \end{align}
    > $$

-   Best case and worst case are the same **⍬**

    > $$
    > \begin{align}
    > ⍬(n^{2}) \\
    > ⍬(n\ log\ n)  \\
    > ⍬(n) \\
    > ⍬(log\ n) \\
    > ⍬(1) \\
    > \end{align}
    > $$

## typeof struct

```C
typedef struct
{
    string name;
    string number;
}
person;
```

## sorting

```
Repeat n-1 times
    For i from 0 to n-2
        If numbers[i] and numbers[i+1] out of order
            Swap them
    If no swaps
        Quit
```

This is O(n^2)

## recursion

-   set a break point

## merge sort

-   recursion
-   O(n log n) **But WHY?**
-   need more spaces

```
Sort left half of numbers
Sort right half of numbers
Merge sorted halves
```

# Section 3

## Linear Search

## Binary Search

-   must sort

## Running Time

## selection sort

## Structs

This can be used to define a new type

```c
typedef struct
{
    string name;
    int votes;
}
candidate;

candidate president;
president.name = "Alyssa";
president.votes = 10;
```

Use `typedef` can reuse the struct, if you only use the struct once, you can just use `struct`

## Recursion

-   Factorial

# Shorts

## Linear Search

-   O(n^2)
-   Ω(1)

## Binary Search

-   O(log n)
-   Ω(1)
-   must sort

## Bubble Sort

-   O(n^2)
-   Ω(n)

## Selection Sort

-   O(n^2)
-   Ω(n^2)

## Recursion

-   The base case, which when triggered will terminate the recursive process.
-   The recursive case, which is where the recursion will acctually occur.

```c
int fact(int n)
{
    if (n == 1)
    {
        return 1;
    }

    // recursive case
    return n * fact(n - 1);
}
```

-   In general, but not always, recursive functions replace loops in non-recursive functions.
-   It's also possible to have more than one base or recursive case, if the program might recurse or terminate in different ways, depending on the input being passed in.

## Merge Sort

-   O(n log n)
-   Ω(n log n)
