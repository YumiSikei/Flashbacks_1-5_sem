#include <LPC23xx.H>

void delay(void) {
   unsigned int i;
   for (i=0;i<0xfffff;i++){}
}

#define MIX (1 << 26)
#define HEAT (1 << 27)
#define BAKE (1 << 28)
#define BUTTON (1 << 29)

// button mix heat bake
// 1      0   0    1
// 0      1   1    0

int main (void) {
	PINSEL3 = 0x00000000;
	IODIR1 = 0x1C000000;
	IOCLR1 = 0x1C000000;
	while(1){
		if(IOPIN1&BUTTON){
			IOCLR1 = MIX|HEAT;
			IOSET1 = BAKE;
			delay();}
		else {
			IOCLR1 = BAKE;
			IOSET1 = MIX|HEAT;
		delay();}
	}
}