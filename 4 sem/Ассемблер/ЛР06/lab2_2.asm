     SSTACK     SEGMENT PARA STACK  'STACK'
                DB   64 DUP('����____')
     SSTACK     ENDS

     DSEG          SEGMENT  PARA PUBLIC 'DATA'
     M         dw  5
     fact      dw  1
               dw  ?
     DSEG          ENDS
PAGE
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG,DS:DSEG,SS:SSTACK
		

p1 proc near ; ���� - bx ����� -  ax

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
; �������� �� ����� ������� �� 1 ������
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
               MOV  AX,DSEG ; �������� ������� ������ datasec � ds
               MOV  DS,AX
	       mov ax, offset fact
	       push ax
	       push M
	       call p2
	       add sp, 4

 	       MOV  AH,4Ch; ������� ��� ��� - ��������� ���������
               INT 21H; �������� ���������� ���
     START     ENDP
               
     CSEG      ENDS
               END  START