.386
.model FLAT,C
PUBLIC X_Y

.CODE
X_Y PROC
 PUSH EBP                        
  MOV EBP,ESP 

  X EQU DWORD PTR[EBP+8]           ;перва€ строка
  Y EQU DWORD PTR[EBP+12]           ;втора€ строка
  L EQU DWORD PTR[EBP+16]          ;длина строк

    MOV ECX,L                     ;CX = длина строки
  SHR ECX,5                    
  INC ECX 
  MOV EDX,X
  MOV EBX,Y

M1:
 MOV EAX,[EBX]
  
  NOT EAX           
  AND EAX,[EDX]         
  
  ADD EDX,4 ; Ёто может не работать, надо запустаить                
  ADD EBX,4
  
  LOOP M1          
  POP EBP ; ¬осстановили регистры
  RET ;12 3 переменных по 4 байта
X_Y ENDP ;¬ообще не сходитс€, но кака€ разница. «десь лучше
END