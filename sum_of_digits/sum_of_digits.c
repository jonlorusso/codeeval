#include <stdio.h>

int sum_digits(char *line)
{
    int i, sum;
    sum = 0;
    for(i = 0; line[i]; i++)
        if (line[i] > 48 && line[i] < 58)
            sum += ( line[i] - 48 );

    return sum;
}

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");

    char line[80];
    while ( fgets(line, sizeof(line), file) != NULL )
        printf("%d\n", sum_digits(line));

    fclose(file);

    return 0;
}
