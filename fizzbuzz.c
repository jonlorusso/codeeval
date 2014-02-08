#include <stdio.h>
#include <errno.h>
#include <stdlib.h>

void fizzbuzz(int a, int b, int n)
{
    int i;

    for(i = 1; i <= n; i++) {
        int fizz = i % a == 0;
        int buzz = i % b == 0;

        if(fizz && buzz)
            printf("FB");
        else if(fizz)
            printf("F");
        else if(buzz)
            printf("B");
        else
            printf("%d", i);
        
        if(i < n)
            printf(" ");
    }

    printf("\n");
}


int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");

    int a, b, n;
    while (fscanf(file, "%d %d %d", &a, &b, &n) != EOF)
        fizzbuzz(a, b, n);

    return 0;
}
