# Lecture 3 Algorithms

## Target 50

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
