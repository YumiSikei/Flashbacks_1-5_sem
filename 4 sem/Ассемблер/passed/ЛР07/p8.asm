PAGE
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG
		PUBLIC p8
p8 PROC NEAR
               EXTRN end_p: near
               jmp end_p
	       ret
p8 ENDP
     CSEG      ENDS
               END  