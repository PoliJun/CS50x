#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *s = "HI!";
    printf("%s\n", s);
    printf("%c\n", *(s + 5));

    int *i = malloc(10 * sizeof(int));

    for (int j = 0; j < 10; j++)
    {
        printf("%d\n", i[j]);
    }

    free(i);
}