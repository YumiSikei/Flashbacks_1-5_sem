TITLE	À¿¡Œ–¿“Œ–Õ¿ﬂ –¿¡Œ“¿ 4

     SSTACK     SEGMENT PARA STACK  'STACK'
                DB   64 DUP('—“≈ ____')
     SSTACK     ENDS

     DSEG          SEGMENT  PARA PUBLIC 'DATA'
     X         DB      1,2,3,4,5
	       DB      1,2,3,4,5
	       DB      1,2,3,4,5
	       DB      1,2,3,4,5
	       DB      1,2,3,4,5
     N         DB      5
     DSEG          ENDS

SUBTTL         Œ—ÕŒ¬Õ¿ﬂ œ–Œ√–¿ÃÃ¿
PAGE
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG,DS:DSEG,SS:SSTACK

     START     PROC FAR
               MOV  AX,DSEG		
               MOV  DS,AX
                
					
               MOV   BX, OFFSET X	
					
	
               MOV DL, [BX][1]		
               XCHG DL, [BX][5]	
               MOV [BX][1], DL	

	       MOV DL, [BX][2]		
               XCHG DL, [BX][10]	
               MOV [BX][2], DL	

	       MOV DL, [BX][3]		
               XCHG DL, [BX][15]	
               MOV [BX][3], DL	
               
               MOV DL, [BX][4]		
               XCHG DL, [BX][20]	
               MOV [BX][4], DL	

	       MOV DL, [BX][7]		
               XCHG DL, [BX][11]	
               MOV [BX][7], DL	

	       MOV DL, [BX][8]		
               XCHG DL, [BX][16]	
               MOV [BX][8], DL	
               
	       MOV DL, [BX][9]		
               XCHG DL, [BX][21]	
               MOV [BX][9], DL	

	       MOV DL, [BX][13]		
               XCHG DL, [BX][17]	
               MOV [BX][13], DL	

               MOV DL, [BX][14]		
               XCHG DL, [BX][22]	
               MOV [BX][14], DL	

	       MOV DL, [BX][19]		
               XCHG DL, [BX][23]	
               MOV [BX][19], DL	


 
     	       MOV  AH,4CH
               MOV  AL,0
               INT 21H
     START     ENDP

     CSEG      ENDS
               END  START
