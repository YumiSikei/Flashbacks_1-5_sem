
PAGE
EXTRN prob:near
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG
		PUBLIC p2
                PUBLIC p21
p21 PROC NEAR
; 10 ичное целое без знака
               Push bp
               mov bp, sp
               add bp, 4
  
      
               mov ax, [bp]
               mov bx, [bp + 2]

               add bx, 15


cy2:           mov dx, 1
               and dx, ax

	       add dx, '0'
               mov [bx], dl
                  
               shr ax, 1
               cmp ax, 0
               je c2con
               dec bx  
               ;shr ax, 1
               jmp cy2

c2con:

               mov ax, bx

               pop bp
	       ret 4
p21 ENDP

p2 proc near
               Push bp
               mov bp, sp
               add bp, 4

               mov ax, [bp]
               mov bx, [bp + 2]
               push bx
               push ax

               call p21
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

p2 endp
     CSEG      ENDS
               END  
     CSEG      ENDS
               END  