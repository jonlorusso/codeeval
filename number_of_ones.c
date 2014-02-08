#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");

    int x;
    while ( fscanf(file, "%d\n?", &x) != EOF ) {
        int count = 0;
        int i;
        for (i = 0; i < 16; i++) {
            count += ( x & ( (int)pow(2, i) ) ) >> i;
        }
        printf("%d\n", count);
    }

    return 0;
}
