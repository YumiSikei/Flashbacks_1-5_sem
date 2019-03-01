PAGE
EXTRN prob:near
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG
		PUBLIC p4
                PUBLIC p41
p41 PROC NEAR
; 10 ичное целое без знака
               Push bp
               mov bp, sp
               add bp, 4
  
      
               mov ax, [bp]
               mov bx, [bp + 2]

               add bx, 15

               mov cx, 10

               mov dx, 0

c4:            div cx

	       
               add dl, '0'
               mov [bx], dl
	       mov dx, 0

               cmp ax, 0
               jz c41 

               dec bx
               
	       jmp c4
c41:

               mov ax, bx

               pop bp
	       ret 4
p41 ENDP

p4 proc near
               Push bp
               mov bp, sp
               add bp, 4

               mov ax, [bp]
               mov bx, [bp + 2]
               push bx
               push ax

               call p41
               mov bx, ax

               mov dx, offset prob
               mov ah, 9
               int 21h 

               mov dx, bx
               int 21h 

               mov dx, offset prob
               int 21h 

               pop bp
	       ret 4

p4 endp
     CSEG      ENDS
               END  