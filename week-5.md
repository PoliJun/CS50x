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
- there is no way for a linked list to do binary search
    ```c
    node *list;
    
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
- binary search trees
## dictionaries
- hashing

