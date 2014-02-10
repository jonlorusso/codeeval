#include <stdio.h>
#include <string.h>

#define LINE_SIZE 1024


char mth(char *line)
{
    char *pch, *previous;
    printf ("Splitting string \"%s\" into tokens:\n",line);

    pch = strtok (line, " ");
    while (pch != NULL) {
        printf ("%s\n",pch);
        previous = pch;
        pch = strtok (NULL, " ");
    }

    printf("last: %s\n", previous);

    return 0;
}

int main(int argc, char **argv)
{
    FILE *f;
    char line[LINE_SIZE];
    int len, i;

    # ...
    f = fopen(argv[1], "r");
    while ( fgets(line, sizeof(line), f) != NULL ) {
        mth(line);
    }

    return 0;
}
