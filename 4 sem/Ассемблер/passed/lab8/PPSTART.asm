.386
.model FLAT,PASCAL
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

;Выполнить трассировку, открыв после первого шага вкладку CPU,
; отображающую дизассемблированный код, регистры, стек и память, командой .
; Отладить программу.
;Добавить в проект п\п COUNT из файла COUNT.ASM:
;•	составить подпрограмму COUNT в файле COUNT.ASM
;•	получить COUNT. OBJ
;•	добавить в проект перед begin
;{$L COUNT .OBJ}
;FUNCTION COUNT:LONGWORD ; EXTERNAL;
;а в конце блока ASM END
;   PUSH OFFSET S1
;   PUSH L
;   CALL COUNT
;•	выполнить отладку функции COUNT
;Подобным образо последовательно добавить в проект и отладить
; подпрограмму SetCler из файла SetCler. ASM (два вызова в п\п START, см ниже) и подпрограмму X_Y из файла X-Y. ASM (один вызов в п\п START).
;Результаты выполнения подпрограмм проверять средствами отладки Turbo Delphi


.CODE
START:
	; Согласно соглашению передаем все аргументы по стеку в прямом порядке
   PUSH OFFSET S1     
   PUSH L                 
   CALL COUNT
   ; Разобрано

   PUSH OFFSET S1
   PUSH L      
   PUSH 1                
   PUSH 1                
   CALL SetCler 
   ; Разобрано   

   PUSH OFFSET S2
   PUSH L
   PUSH 34
   PUSH 0              
   CALL SetCler  
   ; Разобрано    

   PUSH OFFSET S1       
   PUSH OFFSET S2        
   PUSH L               
   CALL X_Y   
   ; Разобрано 

	PUSH OFFSET S1       
   PUSH OFFSET S2        
   PUSH L               
   CALL X_U_Y   
   ; Разобрано  
   
   ; Согласно соглашению не занимаемся очисткой памяти

RET;
END