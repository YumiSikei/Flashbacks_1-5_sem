
P0SEG          SEGMENT  PARA  'DATA'
     Y         db  '0. show menu '
               db  10, 13
               db  '1. input int  to word X'
               db  10, 13
               db   '2.output from X as binary unsigned'
               db  10, 13
               db   '3. output from X as binary signed'
               db  10, 13
               db    '4.output from X as decimal unsigned'
               db  10, 13
               db  '5. output from X as decimal signed'
               db  10, 13
               db  '6. output from X as hexadecimal unsigned'
               db  10, 13
               db  '7. output from X as hexadecimal signed'
               db  10, 13
               db  '8. out from program'
               db  10, 13
               db '$'
P0SEG          ENDS

PAGE
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG, ds:P0SEG

		PUBLIC p0
p0 PROC NEAR

               mov ax, P0SEG
               mov ds, ax

               mov dx, offset Y
               mov ah, 9
               int 21h
	       ret
p0 ENDP
     CSEG      ENDS
               END  