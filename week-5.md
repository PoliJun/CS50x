# Lecture 5 Data Structure

## Queue

-   FIFO
    > First in first out
-   enqueue
-   dequeue

## Stacks

-   LILO
    > Last in first out
-   push
    > add to the top, pushing on the top
-   pop
    > remove from the top, poping off the top

## `realloc(list, sizeof(int));`

## linked lists

-   node
    ```c
    typedef struct node
    {
        int number;
        node *next;
    }
    node;
    ```
-   there is no way for a linked list to do binary search

    ```c
    node *list;

    ```

## while loop to free memory

```c
// free every node with a while loop
    while (ptr != NULL)
    {
        /* code */
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }
```

## trees

-   binary search trees

## dictionaries

-   hashing

-   hash tables
-   tries
    > try is a tree each of whose nodes is an array.

# Section 5

## Wake Word

-   tries

    > memory is cheap, but you also need time to allocate memory, to put things into memory, and may losse it.

-   trade-offs
-   Nodes

## Creating a Linked List

## Hash Function

> "Hey!" --> hash function --> 7

-   A good hash function ...
    -   Always gives you the same value for the same input
    -   Produces an even distribution across buckets
    -   Uses all buckets
