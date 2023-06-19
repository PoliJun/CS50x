#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
} node;

int unload( node * ptr);
int main(int argc, char *argv[])
{
    node *list = NULL;

    for (int i = 1; i < argc; i++)
    {
        int number = atoi(argv[i]);

        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            free(list);
            return 1;
        }
        n->number = number;
        n->next = NULL;

        // prepend
        n->next = list;
        list = n;
    }

    node *ptr = list;
    while (ptr != NULL)
    {
        printf("%d ", ptr->number);
        ptr = ptr->next;
    }
    printf("\n");

    // free every node with a while loop
    unload(ptr);
    // while (ptr != NULL)
    // {

    //     node *next = ptr->next;
    //     free(ptr);
    //     ptr = next;
    // }

}
int unload(node *ptr)
{
    if (ptr == NULL)
    {
        return 0;
    }
    else
    {
        unload(ptr->next);
        free(ptr);
        return 1;
    }
    
}
