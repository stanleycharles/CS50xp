// Lecture 3 - Algo

#include <stdio.h>
#include <cs50.h>
#include <string.h>


int main(void)
{
    string names[] = {"Carter", "David"};
    string numbers[] = {"+1-617-387-3938", "+1-983-398-8736"}
    
    for (int i = 0; i < 2; i++)
    {
        if (strcmp(names[i], "David") == 0)
        {
            printf("Found %s\n", numbers[i]);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}

// Lecture 3 - Algo

#include <stdio.h>
#include <cs50.h>
#include <string.h>

typedef struct 
{
    string name;
    string number;
}

int main(void)
{
    person people[2];

    people[0].name = "Carter";
    people[0].number = "+1-617-387-3938";

    people[0].name = "David";
    people[0].number = "+1-834-784-9059";
    
    for (int i = 0; i < 2; i++)
    {
        if (strcmp(people[i].name, "David") == 0)
        {
            printf("Found %s\n", people[0],number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}