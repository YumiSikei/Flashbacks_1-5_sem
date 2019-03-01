#include <stdio.h>

#define OK 0
#define UNCORRECT_DATA -1
#define FULL_DATA 1

/*#define LEN_MANTISS 30

struct chislo
{
	char znak; // "+" or "-"
    int mantissa[LEN_MANTISS]; //massive of numbers
    int poryadok; 
};*/



int mantissa(int *M, int *r, int point, char *symbol)
{
	int code = OK;
	//int j = 0;
	//char Mc[32];
	
	*r = 0;
	
	int i = 0;
	int count = 0;
	int number = 0;
	char c = getchar();
	if (point == 0)
		c = getchar();
	
	while (c)
	{
		//printf("%c", c);
		if (c == '\n')
			break;
		if (i == 30)
		{
			printf("Mantissa should be smaller than 30 symbols\n");
			code = FULL_DATA;
			break;
		}
		if (i == 0)
		{
			if (c != '.' && c != '-' && c != '+' && (c < '0' || c > '9'))
			{
				printf("In number you should not enter other numbers and point!\n");
				code = UNCORRECT_DATA;
				break;
			}
			else 
			{
				if (c == '-')
				{
					*symbol = '-';
					i--;
				}
				if (c == '+')
					i--;
			}
		}
		if (c == ' ')
		{
			M[i] = 0;
			break;
		}
		
		if (c >= '0' && c <= '9')
		{
			if (count == 0 && c > '0')
			{
				count = 1;
				M[i] = (int)c - 48;
			}
			if (count == 0 && c == '0')
			{
				i--;
				if (number == 1)
					*r -= 1;
			}
			if (count == 1)
				M[i] = (int)c - 48;
		}
		else 
		{
			if (c == '.' && point == 0)
			{
				if (number == 0)
				{
					*r += i;
					i--;
					number = 1;
				}
				else
				{
					printf("In number you should enter only one point!\n");
					code = UNCORRECT_DATA;
					break;
				}
			}
			else 
			{
				if (c == '.' && point == 1)
				{
					printf("It's integer number! Point shouldn't be in integer number!\n");
					code = UNCORRECT_DATA;
					break;
				}
				else 
				{
					if (i > 0)
					{
						printf("In number you should not enter other numbers and point!\n");
						code = UNCORRECT_DATA;
						break;
					}
				}
			}
		}
		i++;
		c = getchar();
	}
	if (point == 1)
		*r += i;
	if (point == 0 && number == 0)
		*r += i;
	for (int j = i; j < 30; j++)
		M[j] = 0;
	/*printf("\n");
	for (i = 0; i < 30; i++)
		printf("%d ", M[i]);
	printf("     %d\n", *r);*/
	
	return code;
}

int okruglenie(int *M, int r)
{
	int i = 29;
	
	while (i >= 0)
	{
		if (M[i] == 9)
		{
			if (i > 0)
			{
				M[i] = 0;
				i--;
			}
			else
			{
				M[i] = 1;
				for (i = 1; i < 30; i++)
					M[i] = 0;
				r++;
			}
		}
		else 
		{
			M[i] += 1;
			break;
		}
	}
	
	return r;
}

int vichitanie(int *M1, int *M2)
{	
	//int k = 0;
	//while ((k < 30) && (M1[k] == M2[k]))   
		//k++;
	if (M1[0] < M2[0])                        
		return UNCORRECT_DATA;
			
	for (int i = 29; i >= 0; i--)
	{
		if (M1[i] < M2[i])
		{
			M1[i] += 10;
			M1[i - 1] -= 1;
		}
		M1[i] -= M2[i];
	}
	
	return OK;
}

/*int umnojenie(int M1, int M2, int M)
{
	int r = 0;
	int j;
	int Mprov[30];
	
	for (int i = 0; i < 30; i++)
		Mprov[i] = 0;
	for (i = 29; i >= 0; i--)
	{
		j = i;
		M1[i] = M1[i] * M2[i];
		if (M1[i] > 9)
		{
			M1[i - 1]
		}
	}
	
	return r;
}*/

int deleniye(int M1[], int M2[], int r1, int r2, int *M, int *r)
{
	int n;
	int count = 0;
	
	*r = r1 - r2 + 1;
	
	
	int k = 0;
	while ((k < 30) && (M1[k] == M2[k]))   
		k++;
	if (k != 30)                        //если делимое меньше делителя, то уменьшаем
	{                                   //порядок на единицу и сдвигаем делимое на одну позицию
		if (M1[k] < M2[k] && (count == 0))
		{			
			*r -= 1;
			count = 1;
		}
		M1[0] = M1[0] * 10 + M1[1];
		for (int j = 2; j < 30; j++)
			M1[j - 1] = M1[j];
		M1[29] = 0;
	}
	else
	{
		M[0] = 1;                        //если оба числа равны, то частное = +0.1 Е1
		for (int y = 1; y < 30; y++)
			M[y] = 0;
		return OK;
	}
	
	k = 0;
	for (int y = 0; y < 30; y++)      //если делимое является нулем, то частное = +0.0 Е0
	{
		if (M1[y] == 0)
			k++;
	}
	if (k == 30)
	{
		for (int y = 0; y < 30; y++)
			M[y] = 0;
		*r = 0;
		return OK;
	}
	
	int i = 0;
	while (i < 31)
	{
		n = 0;
		while (vichitanie(M1, M2) == OK)
		{
			n++;
		}
		//printf("%d", n);
		if (i == 30 && n > 4)
			*r = okruglenie(M, *r);
		if (i < 30)
			M[i] = n;
		M1[0] = M1[0] * 10 + M1[1];
		for (int j = 2; j < 30; j++)
			M1[j - 1] = M1[j];
		M1[29] = 0;
		
		if (M[0] == 0 && M1[0] != 0)
		{
			i--;
			//*r += 1;
		}
		i++;
	}
	//printf("\n");
	return OK;
}

int main(void)
{
	int Mch[30];      //массив для мантиссы частного
	int rch;          //порядок частного
	int Mint[30];     //массив для мантиссы делимого
	int rint;         //порядок делимого
	int Mdouble[30];  //массив для мантиссы делителя
	int rdouble;      //порядок делителя
	int code = OK;    //код ошибки
	char symbol_int = '+';
	char symbol_double = '+';
	char symbol = '+';

	int r = 0;
	int n = 0;

	setbuf(stdout, NULL);

	printf("Enter the mantissa of integer\n");
	printf("------------------------------\n");
	//int point = 0;
	code = mantissa(Mint, &r, 1, &symbol_int);
	if (code == OK)
	{
		printf("\nEnter poryadok for integer\n");
		printf("-----\n");
		scanf("%d", &rint);
		if ((rint > -100000) && (rint < 100000))
		{
			rint += r;
			printf("\n r in integer is %d\n", rint);
			printf("\n");
			printf("Enter the mantissa of float\n");
			printf("------------------------------\n");
			code = UNCORRECT_DATA;
			//point = 0;
			code = mantissa(Mdouble, &r, 0, &symbol_double);
			/*int k = 0;
			while ((k < 30) && (Mint[k] == Mdouble[k]))
			{
				k++;
			}
			if (k != 30)
			{
				if (Mint[k] < Mdouble[k] && point == 0)
					r += 1;
			}*/
			int count = 0;
			for (int i = 0; i < 30; i++)
			{
				if (Mdouble[i] == 0)
					count += 1;
			}
			if (count == 30)
			{
				printf("NOT ALLOWED TO DEVIDE ON ZERO\n");
				code = UNCORRECT_DATA;
			}
			else 
			{
				if (code == OK)
				{
					printf("\nEnter poryadok for float\n");
					printf("-----\n");
					scanf("%d", &rdouble);
					if ((rdouble > -100000) && (rdouble < 100000))
					{
						rdouble += r;
						printf("\n r in float is %d\n", rdouble);
						printf("\n");
						for (int i = 0; i < 30; i++)
							if (Mch[i] == 0)
								n++;
						if (n == 30)
						{
							printf("Delitel should be not 0!");
							code = UNCORRECT_DATA;
						}
						else
						{
							//if(Mint[0] > Mdouble[0])
								//rch -= 1;
							//printf("     %d %d\n", Mint[0], Mdouble[0]);
							deleniye(Mint, Mdouble, rint, rdouble, Mch, &rch);
							//printf("   %d\n", rch);
							if (rch < 99999 && rch > -99999)
							{
								if (symbol_double == '+' && symbol_int == '-')
									symbol = '-';
								if (symbol_double == '-' && symbol_int == '+')
									symbol = '-';
								printf("\nResult: %c0.", symbol);
								for (int i = 0; i < 30; i++)
									printf("%d", Mch[i]);
								printf(" E%d", rch);
							}
							else
							{
								code = FULL_DATA;
								printf("OVERFLOW VARIABLE FOR PORYADOK IN RESULT!\n");
							}
						}
					}
					else
					{
						code = UNCORRECT_DATA;
						printf("OVERFLOW VARIABLE FOR PORYADOK!\n");
					}
				}
				else
					printf("INCORRECT DATA!\n");
			}
		}
		else
		{
			code = UNCORRECT_DATA;
			printf("OVERFLOW VARIABLE FOR PORYADOK!\n");
		}
	}
	else
		printf("INCORRECT DATA!\n");
	
	return code;
}