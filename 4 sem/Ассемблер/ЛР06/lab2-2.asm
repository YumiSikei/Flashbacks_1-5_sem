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
		
                    

p1 proc near ;

               add sp, 4;  ������� ��������� ����� �������
               mov bp, sp
               mov ax, [bp + 2];     ������� ax   
	       mul word ptr ds:[bx]; � ax �������� ���������
               mov word ptr ds:[bx], ax; � *fact �������� ���������
               ret

p1 endp	

p2 proc near

               mov bp, sp
               mov ax, [bp + 2];
               mov bx, [bp + 4];

               cmp ax, 1; �������� �� ����� �� ��������
	       jna m2
               
               dec ax
 
               push bx;    �������� ���������� ������� � ����
	       push ax;   
               call p2
               
		call p1
               
               jmp a         
             ret
m2:             
	       mov word ptr ds:[bx], 1; � *fact �������� ���������  
a:             ret

p2 endp   

     START     PROC FAR
               MOV  AX,DSEG ; �������� ������� ������ datasec � ds
               MOV  DS,AX
	       mov ax, offset fact
	       push ax
	       push M
	       call p2
	       add sp, 4
		mov cx, word ptr ds:[bx]

 	       MOV  AH,4Ch; ������� ��� ��� - ��������� ���������
               INT 21H; �������� ���������� ���
     START     ENDP
               
     CSEG      ENDS
               END  START