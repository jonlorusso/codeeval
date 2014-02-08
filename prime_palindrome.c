#include <stdio.h>
#include <math.h>

int palindrome(int x)
{
    char str[80];
    int chars;
    int i;

    chars = sprintf(str, "%d", x);

    for(i = 0; i < (chars / 2); i++) {
        if(str[i] != str[chars - (i + 1)]) {
            return 0;
        }
    }
    
    return 1;
}

int is_prime(int x)
{
    int i;
    double sq = sqrt(x);

    if(x == 2) return 1;

    for(i = 2; i <= sq; i++) {
        if(x % i == 0)
            return 0;
    }

    return 1;
}

int main(int argc, char *argv[])
{
    int i;
    int result = 0;

    for(i = 3; i < 1000; i = i + 2) {
        if(is_prime(i) && palindrome(i) && ( i > result)) {
            result = i;
        }
    }

    printf("%d\n", result);

    return 0;
}
