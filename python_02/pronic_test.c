# include <stdio.h>
# include <stdlib.h>

int is_pronic(int num){
    int i = 1;
    int j = 2;
    while (j <= num || num == 1)
    {
        int x = i * j;
        int y = i + j;
        int z = j - i;
        if (x == num || y == num || z == num)
        {
            printf("x = %i, y = %i, z = %i\n", x, y, z);
            return (1);
        }
        i++;
        j++;
    }
    return (0);
}

int main(void)
{
    printf("%i no idea\n", is_pronic(547));
}