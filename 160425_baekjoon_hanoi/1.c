#include <stdio.h>
int Cnt;
void hanoi(int n, int a, int b)
{
	int temp;
	if(n==1)
	{
		printf("Move %d, move from Fall%d, to Fall%d\n", n, a, b);
	}
	else
	{
		temp=6-a-b;
		hanoi(n-1, a, temp);
		printf("Move %d, move from Fall%d, to Fall%d\n", n, a, b);
		hanoi(n-1, temp, b);
	}
        Cnt++;
}
int main()
{
	int n;
	printf("Input disk number:");
	scanf("%d", &n);
	hanoi(n, 1, 2);
        printf("Count : %d\n",Cnt);
	return 0;

}

