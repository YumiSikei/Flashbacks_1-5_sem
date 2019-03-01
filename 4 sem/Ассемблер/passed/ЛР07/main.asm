     SSTACK     SEGMENT PARA STACK  'STACK'
                DB   64 DUP('СТЕК____')
     SSTACK     ENDS

     DSEG          SEGMENT  PARA PUBLIC 'DATA'
     m         db 'use kind 0..8: '
               PUBLIC prob
     prob      db 10, 13
               db "$"
     str       db "                "
               db "$"
     numb      dw ?
     DSEG          ENDS
PAGE
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG,DS:DSEG,SS:SSTACK

            
               public end_p

p1 PROC NEAR

               mov dx, offset prob
               mov ah, 9
               int 21h 

               ; ввод  строки
               mov ah, 0ah
               mov str, 8
               mov str[1], 0
               mov dx, offset str
               int 21h

               mov al, str[1]; длина введенной строки
               add dx, 2 ; адрес введенной строки

               ; перевести в число
               mov si, dx
               cmp byte ptr [si], '-'
               je minus
               ;беззнаковое
               mov bp, 1

               mov cl, al; количество цифр
cy2:           mov ch, 0
               mov ax, 0
               mov bh, 0
               mov di, 10
cy1:          
               mul di
       
               mov bl, [si]; запишем очередной символ
               sub bl, '0'; получаем число
               add ax, bx
               inc si
               loop cy1

               imul bp

               mov numb, ax   

               mov dx, offset prob
               mov ah, 9
               int 21h 

               jmp e 
minus:         ;знаковое
               mov bp, -1
               mov cl, al; количество цифр
               dec cl
               inc si
               jmp cy2

	       ret
p1 ENDP
 		
     START     PROC FAR              
cycle_b:       MOV  AX,DSEG ; получаем адресок секции datasec в ds
               mov ds, ax
               mov dx, offset m; print string
               mov ah, 9
               int 21h

               mov ah, 1 ; считать 1 символ в al
               int 21h
               
               cmp al, '0'
               je m0
               cmp al, '1'
               je m1
               cmp al, '2'
               je m2
               cmp al, '3'
               je m3
               cmp al, '4'
               je  m4
               cmp al, '5'
               je m5
               cmp al, '6'
               je m6
               cmp al, '7'
               je m7
               cmp al, '8'
               je m8
              
m0:            EXTRN p0: PROC
               mov bx, offset p0
               jmp cycle_e   
            
m2:            EXTRN p2: PROC
               mov bx, offset p2
               mov ax, offset str
	       Push ax
               Push numb
               jmp cycle_e 

m3:            EXTRN p3: PROC
               mov bx, offset p3
               mov ax, offset str
	       Push ax
               Push numb
               jmp cycle_e 

m4:            EXTRN p4: PROC
               mov bx, offset p4
               mov ax, offset str
	       Push ax
               Push numb
               jmp cycle_e 

m5:            EXTRN p5: PROC
               mov bx, offset p5
               mov ax, offset str
	       Push ax
               Push numb
               jmp cycle_e 

m6:            EXTRN p6: PROC
               mov bx, offset p6
               mov ax, offset str
	       Push ax
               Push numb
               jmp cycle_e 

m7:            EXTRN p7: PROC
               mov bx, offset p7
               mov ax, offset str
	       Push ax
               Push numb
               jmp cycle_e 

m8:            EXTRN p8: PROC
               mov bx, offset p8
               jmp cycle_e 

m1:            ;EXTRN p1: PROC
               mov bx, offset p1

	       jmp cycle_e
	       

cycle_e:       call bx
e:             jmp cycle_b               
	
end_p label near
	       MOV  AH,4Ch;
               INT 21H; передача управления дос
     START     ENDP
               
     CSEG      ENDS
               END  START       