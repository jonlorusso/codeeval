#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");

    int n, p1, p2;
    int x, y;
    while (fscanf(file, "%d,%d,%d", &n, &p1, &p2) != EOF) {
        x = ( n & (int)pow(2, (p1 -1)) ) >> (p1 - 1);
        y = ( n & (int)pow(2, (p2 -1)) ) >> (p2 - 1);

        if ( x == y )
            printf("true\n");
        else
            printf("false\n");

    }

    return 0;
}
