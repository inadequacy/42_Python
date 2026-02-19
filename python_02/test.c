# include <stdio.h>
# include <stdlib.h>

int     get_words(char *str)
{
    int i = 0;
    int words = 0;

    while(str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
        i++;
    while(str[i] != '\0')
    {
        while(str[i] != ' ' && str[i] != '\t' && str[i] != '\n')
            i++;
        if(str[i] == ' ' || str[i] == '\t' || str[i] == '\n' || str[i] == '\0')
        {
            words++;
            i++;
        }
        while(str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
            i++;
    }
    printf("%i\n", words);
    return (words);
}

int     get_characters(char *str)
{
    int i = 0;
    int characters = 0;

    while(str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
        i++;
    while(str[i] != '\0')
    {
        while(str[i] != ' ' && str[i] != '\t' && str[i] != '\n')
        {
            if(str[i] == '\0')
                break;
            characters++;
            i++;
        }
        while(str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
            i++;
        if(str[i] == '\0')
            break;
    }
    printf("%i\n", characters);
    return (characters);
}

int     next_str_len(char *str, int pos)
{
    int i = pos;
    
    while(str[i] != ' ' && str[i] != '\t' && str[i] != '\n' && str[i] != '\0')
        i++;
    return (i);
}

char    **split(char *str)
{
    if (str == "")
        return (0);
    
    int words = get_words(str);
    int characters = get_characters(str);
    char **matrix = (char **)malloc((words * (characters + 1)) * sizeof(char **));
    int i = 0;
    int j = 0;
    int k = 0;
    int n_len;

    while(str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
        i++;
    while(str[i] != '\0')
    {
        n_len = next_str_len(str, i);
        matrix[k] = (char *)malloc(n_len + 1 * sizeof(char));
        while(str[i] != ' ' && str[i] != '\t' && str[i] != '\n')
        {
            if(str[i] == '\0')
                break;
            matrix[k][j] = str[i];
            printf("%i %i %i\n", i, j, k);
            j++;
            i++;
        }
        matrix[k][j] = '\0';
        j = 0;
        k++;
        while(str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
            i++;
        if(str[i] == '\0')
            break;
    }
    return (matrix);
}

int     *range(int start, int end)
{
    int total_numbers = 1;
    int *result;
    int temp;

    if (start < end)
    {
        temp = start;
        total_numbers = 0;
        while (temp != end)
        {
            total_numbers++;
            temp++;
        }
    }
    if (start > end)
    {
        temp = end;
        total_numbers = 0;
        while (temp != start)
        {
            total_numbers++;
            temp++;
        }
    }
    temp = 0;
    result = (int *)malloc(total_numbers * sizeof(int));
    if (start == end)
    {
        result[0] = start;
        return (result);
    }
    if (start < end)
    {
        while (end >= start)
        {
            result[temp] = end;
            end--;
            temp++;
        }
    }
    else
    {
        while (end <= start)
        {
            result[temp] = end;
            end++;
            temp++;
        }
    }
    return (result);
}

int     main(void)
{
    // char **words = split("  word two  \n and lets go    ");
    // printf("%s\n", words[0]);
    // printf("%s\n", words[1]);
    // printf("%s\n", words[2]);
    // printf("%s\n", words[3]);
    // printf("%s\n", words[4]);
    // free(words[0]);
    // free(words[1]);
    // free(words[2]);
    // free(words[3]);
    // free(words[4]);
    // free(words);

    int *number = range(-2, 5);
    int *zero = range(5, 5);
    int size = 8;

    printf("%i\n", zero[0]);
    free(zero);
    for (int i = 0; i < size; i++)
        printf("%d ", number[i]);
    free(number);
    return (0);
}