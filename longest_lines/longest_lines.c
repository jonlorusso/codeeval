#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Tree Tree;
struct Tree {
    Tree *left;
    Tree *right;
    int length;
    char *line;
};

Tree *new_tree(char *line)
{
    Tree *new_tree = malloc(sizeof(Tree));

    new_tree->line = malloc(strlen(line) + 1);
    strcpy(new_tree->line, line);

    new_tree->length = strlen(line);
    return new_tree;
}

Tree *add_line(Tree *tree, char *line)
{
    if(tree == NULL)
        return new_tree(line);

    int length = strlen(line);

    if(length > tree->length) {
        tree->right = add_line(tree->right, line);
    } else {
        tree->left = add_line(tree->left, line);
    }

    return tree;
}

int print_tree(Tree *tree, int n)
{
    if (n > 0) {
        if(tree->right)
            n = print_tree(tree->right, n);

        printf("%s", tree->line);
        n--;

        if(tree->left)
            print_tree(tree->left, n);
    }

    return n;
}

int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");

    int count;
    fscanf(file, "%d\n", &count);

    Tree *tree;
    char line[1000];

    while ( fgets(line, sizeof(line), file) != NULL )
        tree = add_line(tree, line);

    print_tree(tree, count);

    free(tree->line);
    free(tree);
    free(file);

    
    return 0;
}
