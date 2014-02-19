#include <stdio.h>
#include <string.h>

#define LINE_SIZE 1024
int main(int argc, char **argv)
{
    int i;

    for (i = 1; i < 100; i += 2 )
        printf("%d\n", i);

    return 0;
}
