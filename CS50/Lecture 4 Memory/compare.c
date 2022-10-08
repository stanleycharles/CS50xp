// Version 1

// #include <cs50.h>
// #include <stdio.h>

// int main(void)
// {
//     int i = get_int("i: ");
//     int j = get_int("j: ");

//     if (i == j)
//     {
//         printf("Same\n");
//     }
//     else
// }

// Version 2

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int i = get_int("i: ");
    int j = get_int("j: ");

    if (i == j)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}

// Version 3

// #include <cs50.h>
// #include <stdio.h>

// int main(void)
// {
//     string s = get_string("s: ");
//     string t = get_string("t: ");

//     if (s == t)
//     {
//         printf("Same\n");
//     }
//     else
//     {
//         printf("Different\n");
//     }
// }

// Version 4

// #include <cs50.h>
// #include <stdio.h>

// int main(void)
// {
//     char *s = get_string("s: ");
//     char *t = get_string("t: ");

//     if (s == t)
//     {
//         printf("Same\n");
//     }
//     else
//     {
//         printf("Different\n");
//     }
// }


// Version 5

// #include <cs50.h>
// #include <stdio.h>
// #include <string.h>

// int main(void)
// {
//     char *s = get_string("s: ");
//     char *t = get_string("t: ");

//     printf("%s\n", s);
//     printf("%s\n", t);
    
// }

// Version 6

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    printf("%p\n", s);
    printf("%p\n", t);
    
}