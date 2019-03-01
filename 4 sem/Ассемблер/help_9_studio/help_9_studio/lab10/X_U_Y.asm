.386
.model FLAT,C
PUBLIC X_U_Y

.CODE
X_U_Y PROC

PUSH EBP                
MOV EBP,ESP 

X EQU DWORD PTR[EBP+8]           ;первая строка
Y EQU DWORD PTR[EBP+12]           ;вторая строка
L EQU DWORD PTR[EBP+16]            ;длина строк

  MOV ECX,L                       ;CX = длина строк
  SHR ECX,5        
  INC ECX                      
  MOV EBX,X
  MOV EDX,Y

M1:
  MOV EAX,[EDX]
  ; Помещаем Y(1000) как результат работы подпрограммы 
  OR EAX, [EBX]
  ADD EBX,4                   
  ADD EDX,4

  LOOP M1                         
  POP EBP 
  RET
X_U_Y ENDP
END