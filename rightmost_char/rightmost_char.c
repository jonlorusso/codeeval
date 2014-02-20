#include <stdio.h>
#include <string.h>

#define LINE_SIZE 1024
int main(int argc, char **argv)
{
    FILE *file;
    char line[LINE_SIZE], *p;

    char *text;
    char *ch;

    int i;
    int found;

    file = fopen(argv[1], "r");

    while (fgets(line, LINE_SIZE, file)) {
        if ((p = strchr(line, '\n'))) { *p = '\0'; }
        if (line[0] == '\0') { continue; }

        text = strtok(line, ",");
        ch = strtok(NULL, ",");

        found = 0;

        for (i = 0; i < strlen(text); i++) {
            if (text[i] == ch[0]) {
                printf("%d\n", i + 1);
                found = 1;
                break;
            }
        }

        if (!found) {
            printf("-1\n");
        }
    }

    return 0;
}
