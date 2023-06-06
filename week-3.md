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
typeof struct
{
    string name;
    string number;
}
person;
```
