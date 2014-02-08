#include <stdio.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");

    char line[200];
    int i;
    while ( fgets(line, sizeof line, file) != NULL )
        for(i = 0; line[i]; i++ )
            printf("%c", tolower(line[i]));

    return 0;
}
