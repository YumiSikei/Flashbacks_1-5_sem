     SSTACK     SEGMENT PARA STACK  'STACK'
                DB   64 DUP('����____')
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
               MOV  AX,DSEG ; �������� ������� ������ datasec � ds
               MOV  DS,AX
	       
	       mov cx, M
	       call p
	       mov fact, ax
 	       MOV  AH,4Ch; ������� ��� ��� - ��������� ���������
               INT 21H; �������� ���������� ���
     START     ENDP
               
     CSEG      ENDS
               END  START
