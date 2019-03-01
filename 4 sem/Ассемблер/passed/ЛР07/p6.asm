
PAGE
EXTRN prob:near
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG
		PUBLIC p6
                PUBLIC p61
p61 PROC NEAR
; 10 ичное целое без знака
               Push bp
               mov bp, sp
               add bp, 4
  
      
               mov ax, [bp]
               mov bx, [bp + 2]

               add bx, 15


cy6:           mov dx, 15
               and dx, ax

               cmp dx, 10
               jge bukva ; больше или равно

	       add dx, '0'
kon:           mov [bx], dl

               mov cl, 4
               shr ax, cl
               cmp ax, 0
               je c6con
               dec bx  
               ;shr ax, 1
               jmp cy6

c6con:

               mov ax, bx

               pop bp
	       ret 4

bukva:        sub dx, 10
              add dx, 'A'
              jmp kon
p61 ENDP

p6 proc near
               Push bp
               mov bp, sp
               add bp, 4

               mov ax, [bp]
               mov bx, [bp + 2]
               push bx
               push ax

               call p61
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

p6 endp
     CSEG      ENDS
               END  
     CSEG      ENDS
               END  