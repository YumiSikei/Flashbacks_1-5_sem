;Составить подпрограмму с именем X_U_Y типа
;   Procedure (var X: LONGWORD; const Y:LONGWORD; L:LONGWORD)
;выполн€ющую объединение битовых строк X:=X U Y длины L.

.386
.model FLAT,C
PUBLIC X_U_Y

.CODE
X_U_Y PROC

; Тут был нарушен порядок. Как это вообще работало? 
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

  RET
X_U_Y ENDP
END