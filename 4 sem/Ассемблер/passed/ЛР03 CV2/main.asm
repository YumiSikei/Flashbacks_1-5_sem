SSTACK SEGMENT PARA STACK 'STACK'
DB 64 DUP('—“≈ ____')
SSTACK ENDS
DSEG SEGMENT PARA PUBLIC 'DATA'
X DB 0,1,2,3,4,5,6,7 ; 
B DB 1B ; инициализируетс€ в 1 (хз почему)
K DB ?
DSEG ENDS
SUBTTL ќ—Ќќ¬Ќјя ѕ–ќ√–јћћј
PAGE
CSEG SEGMENT PARA PUBLIC 'CODE'
ASSUME CS:CSEG,DS:DSEG,SS:SSTACK
START PROC FAR
MOV AX,DSEG
MOV DS,AX
M1: MOV K,2
MOV SI,0 ; грубо говор€, начальный индекс массива дл€ поиска
MOV CX,8 ; 
MOV AL,B ; значение B (B=1) Ц дл€ проверки четности
M2: TEST X[SI],AL ; 
JNZ M3 ; 
DEC K ; декремент K, если встретили четное число.   
JZ M4 ; 
M3: INC SI ; увеличение индекса массива
LOOP M2 ; пока не обнулилс€ счетчик CX переходим на M2
M4: ADD SI,'0' ; 
MOV AH,2 ; 2 - код функции DOS вывода на экран
MOV DX,SI ; 
M5: INT 21H ; вызов функции DOS 02h
M6: MOV AH,4CH ; 4C - код функции DOS завершение программы
MOV AL,0
INT 21H
START ENDP
CSEG ENDS
END START