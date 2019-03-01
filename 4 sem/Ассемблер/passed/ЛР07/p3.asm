PAGE
EXTRN prob:near
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG
		PUBLIC p3
EXTRN p21:proc
p3 PROC NEAR
               Push bp
               mov bp, sp
               add bp, 4
  
      
               mov ax, [bp]; numb
               mov bx, [bp + 2]; str

               cmp ax, 0
               jge c3pl
	       
               neg ax
               mov bp, 1
               jmp c3m

c3pl:          mov bp, 0
c3m:           push bx
               push ax
               call p21   

               cmp bp, 1
               je c3min
               mov bx, ax
c3g:          

               mov dx, offset prob
               mov ah, 9
               int 21h 

               mov dx, bx
               int 21h 

               mov dx, offset prob
               int 21h 

               pop bp
	       ret 4
c3min:         mov bx, ax
               dec bx
               mov [bx],byte ptr '-'
               jmp c3g

p3 ENDP
     CSEG      ENDS
               END  