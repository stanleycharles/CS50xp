// Version 1

// #include <stdio.h>

// void swap(int a, int b);

// int main(void)
// {
//     int x = 1;
//     int y = 2;
//     printf("x is %i, y is %i\n", x , y);
//     swap(x, y);
//     printf("x is %i, y is %i\n", x, y);
// }

// void swap(int a, int b)

// {
//     int tmp = a;
//     a = b;
//     b = tmp;
// }

// Version 2

// #include <stdio.h>

// void swap(int a, int b);

// int main(void)
// {
//     int x = 1;
//     int y = 2;
//     printf("x is %i, y is %i\n", x , y);
//     swap(x, y);
//     printf("x is %i, y is %i\n", x, y);
// }

// void swap(int a, int b)

// {
//     printf("a is %i, b is %i\n", a, b);
//     int tmp = a;
//     a = b;
//     b = tmp;
//     printf("a is %i, b is %i\n", a, b);
// }

// Version 3

#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;
    printf("x is %i, y is %i\n", x , y);
    swap(&x, &y);
    printf("x is %i, y is %i\n", x, y);
}

void swap(int *a, int *b)

{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
