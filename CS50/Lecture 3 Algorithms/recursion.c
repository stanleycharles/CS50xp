// Lecture 3 - Algo

#include <stdio.h>
#include <cs50.h>

void draw(int n)

int main(void)
{
    int height = get_int("Height: ");
    
    drew(height);
}

void draw(int n)
{   
    if ( n <= 0)
    {
        return;
    }

    draw(n-1);

    for (int i = 0; i < n; i++)
    
        {
            printf("#");
        }
        prinf("\n");
    
}