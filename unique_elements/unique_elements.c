#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define LINE_SIZE 1024
int main(int argc, char **argv)
{
    FILE *f;
    char line[LINE_SIZE], *p;
    char *pch;

    int first;
    int curr;
    int x;
   
    // Open file passed as argument
    if (argc < 2 || !(f = fopen(argv[1], "r"))) {
        fprintf(stderr, "Unable to open file argument\n");
        return 1;
    }

    // Read lines from file
    while (fgets(line, LINE_SIZE, f)) {
        // You may want to remove the trailing '\n'
        if ((p = strchr(line, '\n'))) { *p = '\0'; }

        curr = -1;
        first = 1;

        pch = strtok(line, ",");
        while (pch != NULL) {
            x = atoi(pch);

            if (x != curr) {
                if (!first) {
                    printf(",");
                } else {
                    first = 0;
                }
                printf("%s", pch);
                curr = x;
            }

            pch = strtok(NULL, " ,.-");
        }

        printf("\n");
    }

    return 0;
}
