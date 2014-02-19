#include <stdio.h>
#include <string.h>

#define LINE_SIZE 1024
int main(int argc, char **argv)
{
    int i, j;
    int begin;

    for (i = 1; i <= 12; i++) {
        begin = 1;
        for (j = 1; j <= 12; j++) {
            if (!begin) {
                printf("%4d", (i * j));
            } else {
                printf("%d", (i * j));
                begin = 0;
            }
        }
        printf("\n");
    }

    return 0;
}
