// Version 1

#include <stdio.h>

int main(void)
{
    char c1 = 'H';
    char c1 = 'I';
    char c1 = '!';

    printf("%c%c%c\n", c1, c2, c3);

}

// Version 2

#include <stdio.h>

int main(void)
{
    char c1 = 'H';
    char c1 = 'I';
    char c1 = '!';

    printf("%i%i%i\n", (int) c1, (int) c2, (int) c3);
}

// Version 3

#include <stdio.h>
#include <cs50.h> // not working

int main(void)
{
    string s = "HI!"
    printf("%s\n", s);
}

// Version 4

#include <stdio.h>
#include <cs50.h> // not working

int main(void)
{
    string s = "HI!"
    printf("%i %i %i\n", s[0], s[1], s[2]);
}

// Version 5

#include <stdio.h>
#include <cs50.h> // not working

int main(void)
{ 
    string s = "HI!";
    string t = "BYE!";
    
    printf("%s\n", s);
    printf("%s\n", t);
}

