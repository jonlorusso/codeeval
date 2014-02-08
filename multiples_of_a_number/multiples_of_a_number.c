#include <stdio.h>

void multiple(int x, int n)
{
    int m = n;

    while( m < x )
        m += n;
    printf("%d\n", m);
}

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");

    int x, n;
    while (fscanf(file, "%d,%d", &x, &n) != EOF)
        multiple(x, n);

    return 0;
}
