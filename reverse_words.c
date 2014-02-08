#include <stdio.h>
#include <string.h>

void print_range(char *line, int start, int end)
{
    int i;
    for(i = start; i < end && line[i]; i++) {
        printf("%c", line[i]);
    }
}

void reverse_words(char *line)
{
    int i, j;
    int previous_space;
    int spaces[200];

    j = 0;
    i = 0;

    while(line[i]) {
        if(line[i] == ' ') {
            spaces[j] = i;
            j++;
        }
        i++;
    }

    previous_space = 200;

    j = j - 1;

    while(j >= 0) {
        print_range(line, spaces[j] + 1, previous_space);
        printf(" ");
        previous_space = spaces[j];
        j--;
    }

    print_range(line, 0, previous_space);
    printf("\n");
}


int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    if ( file != NULL ) {
        char line[200];
        char *pos;

        while( fgets(line, sizeof line, file) != NULL ) {
            if ((pos = strchr(line, '\n')) != NULL)
                *pos = '\0';
            reverse_words(line);
        }
    }

    return 0;
}

