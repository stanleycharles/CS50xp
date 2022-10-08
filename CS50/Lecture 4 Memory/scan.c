// Version 1

// #include <stdio.h>

// int main(void)
// {
//     int x;
//     printf("x: ");
//     scanf("%i", &x);
//     printf("x: %i\n", x);

// }

// Version 2

// #include <stdio.h>

// int main(void)
// {
//     char *s;
//     printf("s: ");
//     scanf("%s", s);
//     printf("s: %s\n", s);

// }

// Version 3

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char s[4];
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}