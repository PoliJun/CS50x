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

# Shorts

## Data Structures Summary

-   By this point we've now examined four different ways to store sets of data:

    -   Arrays

        -   Insertion is bad - lots of shifting to fit an element in the middle
        -   Deletion is bad - lots of shifting after removing an element

            > In computer science, "deletion" refers to the process of removing an element from an array. When an element is deleted from an array, the remaining elements need to be shifted down to fill the empty space left by the deleted element. This shifting operation can be computationally expensive, especially if the array is large or the deletion is performed frequently.

            > The expression "Deletion is bad - lots of shifting after removing an element" means that deleting elements from an array can be inefficient and time-consuming due to the need to shift the remaining elements. This is particularly true if the array is being modified frequently or if there are a large number of elements in the array. As a result, it may be preferable to avoid deleting elements from an array if possible, or to use a different data structure that does not require shifting when elements are removed.

        -   Lookup is great - random access, constant time
        -   Relatively easy to sort
        -   Relatively small size-wise
        -   Stuck with a fixed size, no flexibility

    -   Linked lists
        -   Insertion is easy - just tack onto the front
        -   Deletion is easy - once you find the element
        -   Lookup is bad - have to rely on linear search
        -   Relatively difficult to sort - unless you're willing to compromise on super-fast insertion and instead sort as you construct
        -   Relatively small size-wise(not as small as arrays)
    -   Hash tables
        -   Insertion is a two-step process - hash, then add
        -   Deletion is easy - once you find the element
        -   Lookup is on average better than with linked lists because you have the benefit of a real-world constant factor
        -   Not an ideal data structure if sorting is the goal - just use an array
        -   Can run the gamut of size
    -   Tries
        -   Insertion is complex - a lot of dynamic memory allocation, but gets easier as you go
        -   Deletion is easy - just free a node
        -   Lookup is fast - not quite as fast as an array, but almost
        -   Already sorted - sorts as you build in almost all situations
        -   Rapidly becomes huge, even with very little data present, not great if space is at a premium

-   There are even some variations on these (trees and heaps, quite similar to tries, stacks and queues quite similar to arrays or linked lists, etc.) but this will generally cover most of what we're looking at in C.

## Structure

-   Structures provide a way to unify several variables of different types into a single, new variable type which can be saasigned its own type neme.
-   We use structures(structs) to group together elements of a variety of data types that have a logical connection.
-   Think of a structure like a "super-variable".

```c
// variable declaration
struct car myCar;

// field accessing
myCar.year = 2011;
strcpy(myCar.plate, "CS50");
myCar.odometer = 50505;
```

-   Structures, like variables of all other data types, do not need to be created on the stack. We can dynamically allocate structures at run time if our program requires it.
-   In order to access the fields of our structures in that situation, we first need to dereference the pointer to the structure, and then we can access its fields.

```c
// variable declaration, dynamically
struct car *myCar = malloc(sizeof(struct car));

// field accessing
(*myCar).year = 2011;
strcpy((*myCar).plate, "CS50");
(*myCar).odometer = 50505;

// This is annoying. And so as you might expect, there's a shorter way!
```

-   The arrow operator `->` makes this process easier. it's an operator that does two things back-to-back:
    -   First, it dereferences the pointer on the left side of the operator.
    -   Second, it accesses the field on the right side of the operator.
        > Dereferencing is the process of accessing the value of the variable that is pointed to by a reference. This is done using the \* operator in C-like languages.
    ```c
    myCar->year = 1900;
    strcpy(myCar->plate, "CS50");
    myCar->odometer = 50505;
    ```

## Singly-Linked List

-   So far in the course, we've only had one kind of data structure for representing collections of like values.
    -   strrcts, recall, gives us "containers" for holding variables of different data types, typically.
-   Arrays are great for element lookup, but unless we want to insert at the very end of the array, inserting elements is quite costly - remember insertion sort?
-   Arrays are inefficient when inserting and deleting elements. Because of too many shifting operations.
-   So, linked list
-   node
    -   data
    -   pointer

```c
typedef struct sllist
{
    VALUE val;
    struct sllist *next;
}
sllnode;
```

-   In order to work with linked lists efficiently, there are a number of operations that we need to understand:
    1. Create a linked list when it doesn't already exist.  
       `sllnode *create(VALUE val);`
        1. Dynamically allocate
        2. make sure we didn't run out of memory
        3. Initialize the node's val field.
        4. Initialize the node's next field.
        5. Return a pointer to the newly created sllnode.
    2. Search through a linked list to find an element.
        1. create a traversal pointer
        2. if true, return the current
        3. if not, point to the next
        4. reach the end, report failure.
    3. insert a new node into the linked list.
        - insert to the end of the linked list, because we can find the first node immediately.
    4. Delete a single element from a linked list.
    5. Delete an entire linked list.
       `destroy(list);` recursion.

---

## **_HOW TO FREE MEMORY WITH RECURSION?_**

> **_The Three Steps of Inserting into Linked Lists_**

> Inserting a node into a linked list using the insertion method typically involves three steps:
>
> 1. Locate the position where the new node should be inserted: Traverse through the linked list from the head node to find the position where the new node should be inserted. This can be done by comparing the value of the new node with the values of the nodes in the linked list until the appropriate position is found.
>
> 2. Create the new node: Once the appropriate position is found, create a new node with the value to be inserted and set its next pointer to the node that was found in step 1.
>
> 3. Update the pointers: Finally, update the pointers of the nodes involved to include the new node. Set the next pointer of the node before the new node to point to the new node, and set the next pointer of the new node to point to the node that was found in step 1.
>
> These three steps will insert the new node into the linked list in the correct position while maintaining the order of the linked list.

## Doublely Linked Lists

**What is the advantages of doubly linked lists over singly linked lists**

-   Doubly linked lists allow traversal in both forward and backward directions, while singly linked lists only allow traversal in one direction.
-   With a doubly linked list, deletion of a node can be done in constant time, without needing to traverse to the previous node, while in singly linked lists, deletion requires traversal to the previous node, which takes linear time.
-   In a doubly linked list, insertion and deletion of nodes can be done at both ends of the list in constant time, while in a singly linked list, insertion and deletion at the end of the list takes linear time.
-   Doubly linked lists can be used to implement more complex data structures, such as queues and stacks, more efficiently than singly linked lists.

**Why deletion of a node can be done in constant time**

> Deletion of a node in a doubly linked list can be done in constant time because each node in the list has pointers to both its previous and next nodes. To delete a node, we first update the pointers of the previous and next nodes to point to each other, effectively removing the node from the list. This operation can be done in constant time, regardless of the size of the list.
>
> In contrast, deletion of a node in a singly linked list requires traversal to the previous node in order to update its pointer to the next node, before the node to be deleted can be removed. This operation takes linear time, since we may need to traverse the entire list to find the previous node.

## Hash Tables

-   We use a hash table only when we don't care wether the data is sorted
-   A combination of two things:
    -   First, a hash function which returns a nonnegative integer value callled a hash code.
    -   Second, an array capable of storing data of the type we wish to place into the data structure.
-   How to define a hash function?
-   A good hash function should:
    -   Use only the data being hashed
    -   Use all of the data being hashed
    -   Be deterministic
    -   Uniformly distribute data
    -   Generate very different hashe codes for every similar data
-   Search the Internet to find the hash function, don't need to write your own.
-   collision
-   Resolve collisions: Linear probing
-   Linear probing -- clustering.

## Tries

-   What if the data in a hash table is liked lists

## Queue and Stack

![](pictures/Screenshot_2023-06-19-10-06-21-140_org.edx.mobile.jpg)
![](pictures/Screenshot_2023-06-19-10-07-02-062_org.edx.mobile.jpg)
![](pictures/Screenshot_2023-06-19-10-09-41-462_org.edx.mobile.jpg)
![](pictures/Screenshot_2023-06-19-10-14-05-615_org.edx.mobile.jpg)
![](pictures/Screenshot_2023-06-19-10-18-40-317_org.edx.mobile.jpg)
![](pictures/Screenshot_2023-06-19-10-21-26-707_org.edx.mobile.jpg)
![](pictures/Screenshot_2023-06-19-10-47-58-570_org.edx.mobile.jpg)
