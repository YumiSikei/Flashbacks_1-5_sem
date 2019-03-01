     SSTACK     SEGMENT PARA STACK  'STACK'
                DB   64 DUP('СТЕК____')
     SSTACK     ENDS

     DSEG          SEGMENT  PARA PUBLIC 'DATA'
     M         dw  5
     fact      dw  14
               dw  ?
     DSEG          ENDS
PAGE
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG,DS:DSEG,SS:SSTACK
p1 proc near ; вход - bx выход -  ax

               cmp bx, 1
	       jna m22
	       
	       dec bx

               call p1

               inc bx
	       mul bx
               ret
m22:       
	       mov ax, 1    
               ret
p1 endp	

p2 proc near
; поиенять на вызов функции из 1 задачи
               mov bx, sp
               mov cx, ss:[bx + 2];

               call p1

               mov bx, sp
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