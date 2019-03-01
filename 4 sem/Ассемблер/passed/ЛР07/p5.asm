PAGE
EXTRN prob:near
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG
		PUBLIC p5
EXTRN p41:proc
p5 PROC NEAR
               Push bp
               mov bp, sp
               add bp, 4
  
      
               mov ax, [bp]; numb
               mov bx, [bp + 2]; str

               cmp ax, 0
               jge c5pl
	       
               neg ax
               mov bp, 1
               jmp c5m

c5pl:          mov bp, 0
c5m:           push bx
               push ax
               call p41   

               cmp bp, 1
               je c5min
               mov bx, ax
c5g:          

               mov dx, offset prob
               mov ah, 9
               int 21h 

               mov dx, bx
               int 21h 

               mov dx, offset prob
               int 21h 

               pop bp
	       ret 4
c5min:         mov bx, ax
               dec bx
               mov [bx],byte ptr '-'
               jmp c5g

p5 ENDP
     CSEG      ENDS
               END  