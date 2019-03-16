#include <LPC23xx.H>

#define BIT_BTTN (1<<29)
#define STB 26 //Port1.26
#define CLK 27 //Port1.27
#define DIO 28 //Port1.28


void delay(unsigned int count)
{
	unsigned int i;
	for (i=0;i<count;i++) {}
}
void tm1638_sendbyte(unsigned int x)
{
	unsigned int i;
	IODIR1 |= (1<<DIO);//????????????? ??? DIO ?? ?????
	for(i = 0; i < 8; i++)
	{
		IOCLR1=(1<<CLK);//?????? CLK ????????????? ? 0
		delay(0xfff);//????????
		if (x&1)
		{
			IOSET1=(1<<DIO);
		} //????????????? ???????? ?? ?????? DIO
		else
		{
			IOCLR1=(1<<DIO);
		}
		delay(0xfff);//????????
		x >>= 1;
		IOSET1=(1<<CLK);//?????? CLK ????????????? ? 1
		delay(0x1fff);
	}
}

unsigned int tm1638_receivebyte()
{
	unsigned int i;
	unsigned int x=0;
	IODIR1 &= ~(1<<DIO);
	for(i = 0; i < 32; i++)
	{
		IOCLR1=(1<<CLK);
		delay(0xfff);
		if (IOPIN1&(1<<DIO))
		{
			x |= (1<<i);
		}
		delay(0xfff);
		IOSET1=(1<<CLK);
		delay(0x1fff);
	}
	
	return x;
}

void tm1638_sendcmd(unsigned int x)
{

	IOSET1=(1<<STB);

	IODIR1 = (1<<CLK)|(1<<DIO)|(1<<STB);

	IOCLR1=(1<<STB);
	tm1638_sendbyte(x);
}

void tm1638_setadr(unsigned int adr)
{
	tm1638_sendcmd(0xC0|adr);
}
void tm1638_init()
{
	unsigned int i;

	tm1638_sendcmd(0x88); //play mode
	tm1638_sendcmd(0x40); //auto increment
	tm1638_setadr(0);

	for (i=0;i<=0xf;i++)
		tm1638_sendbyte(0);

	tm1638_sendcmd(0x44); //work mode
}
int main (void)
{
	unsigned int i;
	tm1638_init();
		
	while (1)
	{
		i=1;
		//button pressed or not
		tm1638_sendcmd(0x46);
		i = tm1638_receivebyte();
		if ( i == 1 ) 
		{
			tm1638_setadr(1); 
			tm1638_sendbyte(0);
			tm1638_setadr(3); 
			tm1638_sendbyte(0); 
			
			tm1638_setadr(5); 
			tm1638_sendbyte(1); 
			
		}
		else
		{
			tm1638_setadr(1); 
			tm1638_sendbyte(1);
			tm1638_setadr(3); 
			tm1638_sendbyte(1); 
			
			tm1638_setadr(5); 
			tm1638_sendbyte(0);
			
			
		}
		delay(0xffff);


	}
	
}