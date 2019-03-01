.386
.model FLAT,C
PUBLIC START
extern COUNT:near, X_Y:near, SetCler:near, X_U_Y:near

.DATA
S 	DD 0,0,0,0
S1 	DD 00001111000011110000111100001111B,1010101B
           ;0-38 - разряды строки
S2 	DD 00111100001111000011110000111100B,1000001B
           ;0-38 - разряды строки
L DD 39    ;= длина строки
; DD он же DWORD - двойное слово, занимает 4 байта

;СОГЛАШЕНИЯ TURBO C
;1. Параметры передаются в стек справа налево
;2. Функция должна сохранять регистры DS, CS, SS, BP, SI, DI
;3. Функция возвращает результат через AX или DX:AX, причем в  DX
; - старшая часть числа.
;4. Освобождение стека от параметров выполняет вызывающая программа

.CODE
START:
	; Согласно соглашению передаем все аргументы по стеку в прямом порядке   
   push ebp          
   mov ebp,esp     
   
   ; Обратный порядок пушей
   PUSH L
   PUSH OFFSET S1     
   CALL COUNT; (const S: LONGWORD; L:LONGWORD)
   ADD ESP, 8; Память освобождаем здесь же
   
   PUSH 1                
   PUSH 1  
   PUSH L   
   PUSH OFFSET S2 
   CALL SetCler; (var S:LONGWORD; L:LONGWORD; N:LONGWORD; P:LONGWORD)
   ADD ESP, 12;  

   PUSH 0
   PUSH 34 
   PUSH L
   PUSH OFFSET S2   
   CALL SetCler; (var S:LONGWORD; L:LONGWORD; N:LONGWORD; P:LONGWORD)
   ADD ESP, 12;   

   PUSH L 
   PUSH OFFSET S2       
   PUSH OFFSET S1                      
   CALL X_Y; (var A: LONGWORD; const B:LONGWORD; L:LONGWORD)
   ADD ESP, 8; разобрано
   
   PUSH L 
   PUSH OFFSET S2       
   PUSH OFFSET S1                      
   CALL X_U_Y; (var X: LONGWORD; const Y:LONGWORD; L:LONGWORD)   
   ADD ESP, 8; разобрано
   
   POP EBP

   RET
END