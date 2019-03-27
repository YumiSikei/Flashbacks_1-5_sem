/* Вариант 15
Устройство управления фонтаном, состоящее из трех клапанов
форсунок. Программа функционирования:

a) первый клапан открывается каждые 10 секунд, длительность
подачи воды – 1 секунда;

b) второй клапан открывается каждые 20 секунд, длительность
подачи воды – 2 секунды;

c) третий клапан только при нажатии на кнопку.

*/
                  
#include <LPC23xx.H>                       // Описание LPC23xx 

#define BIT_BTTN (1<<29)

#define STB 26 //Port1.26
#define CLK 27 //Port1.27
#define DIO	28 //Port1.28

// функция задержки
void delay(unsigned int count)
{
	unsigned int i;
	for (i=0;i<count;i++){}
}

// задержка на одну секунду
void TimerDelay(void)
{
//Сбросить таймер
	T0TC = 0x00000000;
//Запустить таймер
	T0TCR = 0x00000001;
//Ожидаем окончания счета
	while (T0TCR&0x1) {};
}

// инициализация таймера
void Timer0_Init(void)
{
	T0PR = 8500;				//Предделитель таймера = 12000
	T0TCR = 0x00000002; //Сбросить счетчик и делитель
	T0MCR = 0x00000006; //При совпадении останавливаем, сбрасываем таймер
	T0MR0 = 1000;				//Регистр совпадения = 1000 (1 Гц)
}

// функция посыла байта
void tm1638_sendbyte(unsigned int x) {
		unsigned int i;
		IODIR1 |= (1<<DIO);	//Устанавливаем пин DIO на вывод
		for(i = 0; i < 8; i++)
    {
			IOCLR1=(1<<CLK);		//Сигнал CLK устанавливаем в 0
			delay(0xfff);				//Задержка 
			if (x&1) 	{IOSET1=(1<<DIO);} //Устанавливаем значение на выходе DIO
			else 			{IOCLR1=(1<<DIO);}
			delay(0xfff);				//Задержка
      x  >>= 1;
      IOSET1=(1<<CLK);		//Сигнал CLK устанавливаем в 1
      delay(0x1fff);			
    }
}

// функция прёма байта
unsigned int tm1638_receivebyte() {
		unsigned int i;
		unsigned int x=0;
		IODIR1 &= ~(1<<DIO);//Устанавливаем пин DIO на ввод
		for(i = 0; i < 32; i++)
    {
			IOCLR1=(1<<CLK);//Сигнал CLK устанавливаем в 0
			delay(0xfff);		//Задержка 
			if (IOPIN1&(1<<DIO)) {
				x |= (1<<i);
			}
			delay(0xfff);		//Задержка
      IOSET1=(1<<CLK);//Сигнал CLK устанавливаем в 1
      delay(0x1fff);			
    }
	return x;
}

// функция посыла команды
void tm1638_sendcmd(unsigned int x){
			IOSET1=(1<<STB);//Устанавливаем пассивный высокий уровень сигнала STB
			IODIR1 = (1<<CLK)|(1<<DIO)|(1<<STB);//Устанавливаем пины CLK,DIO,STB на вывод
			IOCLR1=(1<<STB);//Устанавливаем активный низкий уровень сигнала STB
			tm1638_sendbyte(x);
}

// установка адреса регистра LED инидикации
void tm1638_setadr(unsigned int adr) {
		tm1638_sendcmd(0xC0|adr);	//Установить адрес регистра LED инидикации
}

// инициализация индикации
void tm1638_init() {
		unsigned int i;
		tm1638_sendcmd(0x88);	//Разрешить работу индикации
		tm1638_sendcmd(0x40); //Установить режим адресации: автоинкремент
		tm1638_setadr(0);			//Установить адрес регистра LED инидикации
			
		for (i=0;i<=0xf;i++)//Сбросить все 
			tm1638_sendbyte(0);
		
		tm1638_sendcmd(0x44);//Установить режим адресации: фиксированный
}

void output(int mode)
{
	if (mode == 1)
	{
		tm1638_setadr(0x1);
		tm1638_sendbyte(1);
	}
	if (mode == 2)
	{
		tm1638_setadr(0x3);
		tm1638_sendbyte(1);
	}
	if (mode == 3)
	{
		tm1638_setadr(0x5);
		tm1638_sendbyte(1);
	}
	if (mode == 10)
	{
		tm1638_setadr(0x1);
		tm1638_sendbyte(0);
	}
	if (mode == 20)
	{
		tm1638_setadr(0x3);
		tm1638_sendbyte(0);
	}
	if (mode == 30)
	{
		tm1638_setadr(0x5);
		tm1638_sendbyte(0);
	}
}

void work(int type)
{
	unsigned int i;
	
	if(type == 1)
	{
		output(1);
		output(2);
		output(3);
		for ( i=0; i<20; ++i) // 20 = 10сек работа
			TimerDelay();
		output(20);
    output(30);		
	}
	if(type == 2)
	{
		output(1);
		output(20);
		output(30);
		for ( i=0; i<40; ++i) // 40 = 20сек работа
		{
			TimerDelay();
			if(i == 2)
				output(10);	
		}
		output(20);
	}
}

int main (void)
{
	unsigned int i, n;
	tm1638_init();
	Timer0_Init();
	output(111);
		
	while (1)
	{		
		for ( i=0; i<20; ++i)
		{
			TimerDelay();
			if(i == 10)
				work(1); // запуск первого с.д
			
			tm1638_sendcmd(0x46);
			n = tm1638_receivebyte();
			if ( n == 1 ) // кнопка нажата 
			{
				output(3);
			}
			if( n == 0) // кнопка отпущена
			{
				output(30);
			}
		}
		work(2); // запуск второго с.д
		
		tm1638_sendcmd(0x46);
		n = tm1638_receivebyte();
		if ( n == 1 ) // кнопка нажата
		{
			output(3);
		}
		if( n == 0 ) // кнопка отпущена
		{
			output(30);
		}
	}
}



