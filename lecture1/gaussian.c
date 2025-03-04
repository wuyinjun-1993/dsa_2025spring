#include <stdio.h>
int main()
{
    int s, i;
    s=0;// adding numbers 1 to 100
    for(i=0;i<100;i++)
    {
        s+=(i+ 1);
    }
    printf("Sum= %d",s);
}
