// Version 1

// #include <stdio.h>

// int main(void)
// {
//     int score1 = 72;
//     int score2 = 73;
//     int score3 = 33;

//     printf("Average: %f\n", (score1 + score2 + score3) / 3.0);
    
// }

// Version 2

#include <cs50.h> // not working
#include <stdio.h>

int main(void)
{
    int scores[3];

    scores[0] = 72;
    scores[1] = 73;
    scores[2] = 33;



    printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
    
}

// Version 3

#include <cs50.h> // not working
#include <stdio.h>

int main(void)
{
    int scores[3];

    scores[0] = get_int("Score: ");
    scores[1] = get_int("Score: ");
    scores[2] = get_int("Score: ");

    printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
    
}

// Version 4

#include <cs50.h> // not working
#include <stdio.h>

int main(void)
{
    int scores[3];

    for (int i = 0; i < 3; i++)
    {
        scores[i] = get_int("Score: ");
    }

    printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
    
}

// Version 5

#include <cs50.h> // not working
#include <stdio.h>

int n = get_int("How many scores? ");
{co
    int scores[n];

    for (int i = 0; i < n; i++)
    {
        scores[i] = get_int("Score: ");
    }

    printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
    
}

