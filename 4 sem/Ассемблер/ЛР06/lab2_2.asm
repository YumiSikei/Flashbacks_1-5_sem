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
		

p1 proc near ; вход - bx выход -  ax

               cmp cx, 1
	       jna m22
	       
	       dec cx

               call p1

               inc cx
	       mul cx
               ret
m22:       
	       mov cx, 1    
               ret
p1 endp	

p2 proc near
; поиенять на вызов функции из 1 задачи
               mov bx, sp
               mov cx, ss:[bx + 2];
			   mov ax, 1

               call p1

	       mov cx, ss:[bx + 4]

               mov bx, cx
	       mov [bx], ax
             ret
p2 endp   

     START     PROC FAR
               MOV  AX,DSEG ; получаем адресок секции datasec в ds
               MOV  DS,AX
	       mov ax, offset fact
	       push ax
	       push M
	       call p2
	       add sp, 4

 	       MOV  AH,4Ch; команда для дос - завершить программу
               INT 21H; передача управления дос
     START     ENDP
               
     CSEG      ENDS
               END  START