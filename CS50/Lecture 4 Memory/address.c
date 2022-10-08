// Version 1

// #include <stdio.h>

// int main(void)
// {
//     int n = 50;
//     printf("%i\n", n);

// }

// Version 2

// #include <stdio.h>

// int main(void)
// {
//     int n = 50;
//     int *p = &n;
//     printf("%p\n", p);
//     printf("%i\n", *p);
// }

// Version 3

// #include <stdio.h>

// int main(void)
// {
//     int n = 50;
//     int *p = &n;
//     printf("%p\n", p);
//     printf("%i\n", *p);
// }

// Version 4

// #include <stdio.h>

// int main(void)
// {
//     int n = 50;
//     int *p = &n;
//     int c = n;
//     printf("%p\n", p);
//     printf("%i\n", *p);
// }

// Version 5

// #include <cs50.h> // not working
// #include <stdio.h>

// int main(void)
// {
//     string s = "HI!";
//     printf("%s\n", s);
// }

// Version 6

// #include <stdio.h>

// int main(void)
// {
//     char *s = "HI!";
//     printf("%s\n", s);
// }

// Version 6

// #include <cs50.h> // not working
// #include <stdio.h>

// int main(void)
// {
//     string s = "HI!"
//     char c = s[0];
//     char *p = &c;
//     printf("%p\n", p);
// }

// Version 7

// #include <cs50.h> // not working
// #include <stdio.h>

// int main(void)
// {
//     string s = "HI!"
//     char *p = &s[0];
//     printf("%p\n", p);
// }

// Version 8

// #include <cs50.h> // not working
// #include <stdio.h>

// int main(void)
// {
//     string s = "HI!"
//     char *p = &s[0];
//     printf("%p\n", p);
//     printf("%p\n", s);
// }


// Version 9

// #include <stdio.h>

// int main(void)
// {
//     char *s = "HI!"
//     char *p = &s[0];
//     printf("%p\n", p);
//     printf("%p\n", s);
// }

// Version 10

// #include <stdio.h>

// int main(void)
// {
//     char *s = "HI!";
//     printf("%p\n", s);
//     printf("%p\n", &s[0]);
//     printf("%p\n", &s[1]);
//     printf("%p\n", &s[2]);
//     printf("%p\n", &s[3]);
// }

// Version 11

// #include <cs50.h>
// #include <stdio.h>

// int main(void)
// {
//     string s = "HI!";
//     printf("%c\n", s[0]);
//     printf("%c\n", s[1]);
//     printf("%c\n", s[2]);
//     printf("%c\n", s[3]);
// }

// Version 12

// #include <stdio.h>

// int main(void)
// {
//     char *s = "HI!";
//     printf("%c\n", s[0]);
//     printf("%c\n", s[1]);
//     printf("%c\n", s[2]);
// }


// Version 12

#include <stdio.h>

// int main(void)
// {
//     char *s = "HI!";
//     printf("%c\n", *s);
//     printf("%c\n", *(s + 1));
//     printf("%c\n", *(s + 2));
// }


// Version 13

// #include <stdio.h>

// int main(void)
// {
//     int numbers[] = {4, 6, 8, 2, 7, 5, 0};

//     printf("%i\n", numbers[0]);
//     printf("%i\n", numbers[1]);
//     printf("%i\n", numbers[2]);
// }

// Version 14

#include <stdio.h>

int main(void)
{
    int numbers[] = {4, 6, 8, 2, 7, 5, 0};

    printf("%i\n", *numbers);
    printf("%i\n", *(numbers + 1));
    printf("%i\n", *(numbers + 2));
    printf("%i\n", *(numbers + 3));
    printf("%i\n", *(numbers + 4));
    printf("%i\n", *(numbers + 5));
    printf("%i\n", *(numbers + 6));
}
