#include <stdio.h>

void merge_sort(int *array, int size)
{
    //int size = sizeof(&array);
    printf("%d", size);   
}

int main(void)
{
    int array[3] = {1,2,3};
    //merge_sort(array);
    char string[] = "hello world";
    int size = sizeof(string)/sizeof(char);
    printf("%d", size);
    return 0;
}