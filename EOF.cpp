#include <stdio.h>

int eof()
{
    int a,b;
    while ( scanf("%d %d",&a,&b) != -1 ) { //EOF 대신에 -1 을 주어도 됩니다.
        printf("%d\n",a+b);
    }
}