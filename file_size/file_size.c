#include <stdio.h>
#include <string.h>

#define LINE_SIZE 1024
int main(int argc, char **argv)
{
    FILE *f;
    int sz;

    f = fopen(argv[1], "r");

    fseek(f, 0L, SEEK_END);
    sz = ftell(f);

    printf("%d\n", sz);

    return 0;
}
