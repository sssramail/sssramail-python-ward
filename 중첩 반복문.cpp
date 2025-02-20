#include <stdio.h>

int main()
{
/*	int i;
	int j;
	
	for (i = 1;i <= 6;i++)
	{
		printf("%dÇÐ³â ",i);
		for (j = 1;j <= 7;j++)
		{
			printf("%d¹Ý ",j); 
		}
		printf("\n");
	}
	
	int i;
	int j;
	
	for (i = 1;i <= 5;i++)
	{
		for (j = 1;j <= i;j++)
		{
			printf("%d ",j);
		}
		printf("\n");
	}
	
	int i;
	int j;
	
	for (i = 5;i >= 1;i--)
	{
		for (j = 1;j <= i;j++)
		{
			printf("%d ",j);
		}
		printf("\n");
	}
	
	int i;
	int j;
	
	for (i = 5;i >= 1;i--)
	{
		for (j = i;j <= 5;j++)
		{
			printf("%d ",j);
		}
		printf("\n");
	}
	
	int i;
	int j;
	
	for (i = 1;i <= 5;i++)
	{
		for (j = 5;j >= i;j--)
		{
			printf("%d ",j);
		}
		printf("\n");
	}
	
	int i;
	int j;
	
	for (i = 1;i <= 5;i++)
	{
		for (j = i;j <= 4;j++)
		{
			printf("  ");
		}
		for (j = 1;j <= i;j++)
		{
			printf("%2d",j);
		}
		printf("\n");
	}*/
	
	int n;
	int j;
	int i;
	
	scanf("%d",&n);
	
	for (i = 1;i <= n;i++)
	{
		printf("%d :",i);
		for (j = 1;j <= i;j++)
		{
			if (i%j == 0)
			{
				printf("%d ",j);
			}
		}
		printf("\n");
	}
	
	return 0;
}

