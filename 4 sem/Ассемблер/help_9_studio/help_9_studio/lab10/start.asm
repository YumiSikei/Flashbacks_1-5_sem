.386

.model FLAT,C

PUBLIC start
extern COUNT:near, X_Y:near, SetCler:near, X_U_Y:near

.DATA
S 	DD 0,0,0,0
S1 	DD 00001111000011110000111100001111B,1010101B
           ;0-38 - разр¤ды строки
S2 	DD 00111100001111000011110000111100B,1000001B
           ;0-38 - разр¤ды строки
L DD 39    ;= длина строки

.CODE

start:

   PUSH EBP
   MOV EBP, ESP

   PUSH 1                
   PUSH 1  
   PUSH L   
   PUSH OFFSET S2 
   CALL SetCler; (var S:LONGWORD; L:LONGWORD; N:LONGWORD; P:LONGWORD)
   ADD ESP, 16;  

   PUSH 0
   PUSH 34 
   PUSH L
   PUSH OFFSET S2   
   CALL SetCler; (var S:LONGWORD; L:LONGWORD; N:LONGWORD; P:LONGWORD)
   ADD ESP, 16;   

    PUSH L
   PUSH OFFSET S1     
   CALL COUNT; (const S: LONGWORD; L:LONGWORD)
   ADD ESP, 8; ѕам¤ть освобождаем здесь же

   PUSH L 
   PUSH OFFSET S2       
   PUSH OFFSET S1                      
   CALL X_Y; (var X: LONGWORD; const Y:LONGWORD; L:LONGWORD)   
   ADD ESP, 12; разобрано
   
   PUSH L 
   PUSH OFFSET S2       
   PUSH OFFSET S1                      
   CALL X_U_Y; (var X: LONGWORD; const Y:LONGWORD; L:LONGWORD)   
   ADD ESP, 12; разобрано

   POP EBP   
   MOV EAX, 8


   RET 

END