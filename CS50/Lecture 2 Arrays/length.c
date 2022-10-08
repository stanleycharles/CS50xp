// Version 1

#include <cs50.h>
#include <stdio.h>

int main(void)
{ 
    string name = get_string("Name: ");
    
    int i = 0;
    while (name[i] != '\0')
    {
        i++;
    }
    
    printf("%i\n", i);
}

// Version 2

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{ 
    string name = get_string("Name: ");
    int lenght = string_length(name);
    print ("%i\n", length)   
}

int string_length(string s)
{
    int i = 0:
    while (s[i] != '\0')
{
    i++;
}

}
    return i;


// Version 3

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{ 
    string name = get_string("Input: ");
    print ("Output: ");
    for (int i = 0; i < strlen(s); i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
}

// Version 4 - Well design

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{ 
    string name = get_string("Input: ");
    print ("Output: ");
    for (int i = 0; n = strlen(s); i < n; i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
}
