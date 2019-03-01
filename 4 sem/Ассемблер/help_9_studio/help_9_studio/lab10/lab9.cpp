// lab10.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"

extern "C" void start();

int _tmain(int argc, _TCHAR* argv[])
{
	_asm

	{

		call start

	}
	int f;
	scanf_s("%d", &f);
	return 0;
}

