     SSTACK     SEGMENT PARA STACK  'STACK'
                DB   64 DUP('СТЕК____')
     SSTACK     ENDS

     DSEG          SEGMENT  PARA PUBLIC 'DATA'
     M         dw  5
     fact      dw  1
               dw  ?
     DSEG          ENDS
PAGE
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG,DS:DSEG,SS:SSTACK
		
                    

p1 proc near ;

               add sp, 4;  вернуть указатель стека обратно
               mov bp, sp
               mov ax, [bp + 2];     вернуть ax   
	       mul word ptr ds:[bx]; в ax помещаем результат
               mov word ptr ds:[bx], ax; в *fact помещаем результат
               ret

p1 endp	

p2 proc near

               mov bp, sp
               mov ax, [bp + 2];
               mov bx, [bp + 4];

               cmp ax, 1; проверка на выход из рекурсии
	       jna m2
               
               dec ax
 
               push bx;    передача параметров функции в стек
	       push ax;   
               call p2
               
		call p1
               
               jmp a         
             ret
m2:             
	       mov word ptr ds:[bx], 1; в *fact помещаем результат  
a:             ret

p2 endp   

     START     PROC FAR
               MOV  AX,DSEG ; получаем адресок секции datasec в ds
               MOV  DS,AX
	       mov ax, offset fact
	       push ax
	       push M
	       call p2
	       add sp, 4
		mov cx, word ptr ds:[bx]

 	       MOV  AH,4Ch; команда для дос - завершить программу
               INT 21H; передача управления дос
     START     ENDP
               
     CSEG      ENDS
               END  START