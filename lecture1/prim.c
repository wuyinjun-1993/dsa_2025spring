#include <stdio.h>
#include <math.h>
int main()
{
    int n,i, flag =0;
    printf("please input number:");
    scanf("%d",&n);
    for (i = 2; i< sqrt(n)+1;i++)
        if( n % i == 0 )
        {
            flag = 1;
            break;
        }
    
    if(flag == 1)
        printf("%d is NoT a prime number.",n);
    else
        printf("%d is a prime number.",n);
}
