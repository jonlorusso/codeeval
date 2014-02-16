#include <stdio.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");

    int x;
    int sum = 0;
    while (fscanf(file, "%d", &x) != EOF)
        sum += x;

    printf("%d\n", sum);

    return 0;
}
