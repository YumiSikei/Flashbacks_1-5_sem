PAGE
EXTRN prob:near
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG
		PUBLIC p7
EXTRN p61:proc
p7 PROC NEAR
               Push bp
               mov bp, sp
               add bp, 4
  
      
               mov ax, [bp]; numb
               mov bx, [bp + 2]; str

               cmp ax, 0
               jge c7pl
	       
               neg ax
               mov bp, 1
               jmp c7m

c7pl:          mov bp, 0
c7m:           push bx
               push ax
               call p61   

               cmp bp, 1
               je c7min
               mov bx, ax
c7g:          

               mov dx, offset prob
               mov ah, 9
               int 21h 

               mov dx, bx
               int 21h 

               mov dx, offset prob
               int 21h 

               pop bp
	       ret 4
c7min:         mov bx, ax
               dec bx
               mov [bx],byte ptr '-'
               jmp c7g

p7 ENDP
     CSEG      ENDS
               END  