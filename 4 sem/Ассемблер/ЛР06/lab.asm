     SSTACK     SEGMENT PARA STACK  'STACK'
                DB   64 DUP('СТЕК____')
     SSTACK     ENDS

     DSEG          SEGMENT  PARA PUBLIC 'DATA'
     M         dw  5
     fact      dw  ?
     DSEG          ENDS
PAGE
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG,DS:DSEG,SS:SSTACK
		
p proc near
	       
               cmp cx, 1
	       jna m2
	       
	       dec cx

               call p
			   inc cx
			   mov bx,cx
	       mul bx
               jmp m1
m2:             
	       mov ax, 1
               
m1:	       
               ret
p endp

     START     PROC FAR
               MOV  AX,DSEG ; получаем адресок секции datasec в ds
               MOV  DS,AX
	       
	       mov cx, M
	       call p
	       mov fact, ax
 	       MOV  AH,4Ch; команда для дос - завершить программу
               INT 21H; передача управления дос
     START     ENDP
               
     CSEG      ENDS
               END  START
