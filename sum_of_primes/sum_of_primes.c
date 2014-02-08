#include <stdio.h>
#include <math.h>

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
    int count;
    int sum;

    i = 2;
    sum = 0;
    count = 0;

    while(count < 1000) {
        if(is_prime(i)) {
            sum += i;
            count++;
        }
        i++;
    }

    printf("%d\n", sum);

    return 0;
}
