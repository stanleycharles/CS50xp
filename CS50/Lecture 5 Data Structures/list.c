// Version 1

// #include <stdio.h>
// #include <stdlib.h>

// int main(void)
// {
//     int list[3];

//     list[0] = 1;
//     list[1] = 2;
//     list[2] = 3;

//     for (int i = 0; i < 3; i++)
//     {
//         printf("%i\n", list[i]);
//     }    
// }


// Version 2


#include <stdio.h>

int main(void)

{
    // Dynamically allocate an array of size 3
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }
    
    // Assign 3 numbers to that array
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // Times passes

    // Resize old array to be of size 4
    int *tmp = remalloc(4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list);
        return 1;

    }

    // Copy numbers from old array into new array
    for (int 1 = 0; 1 < 3; i++)
    {
        tmp[1] = list[1];
    }

    // Add fourth number to new array
    tmp [3] = 4;

    // Remember new array
    list = tmp;

    // Print new array
    for (int 1 = 0; 1 < 4; i++)
    {
        printf("%i\n", list[1])
    }

    // Free new array 
    free(list)

    return 0;

}


