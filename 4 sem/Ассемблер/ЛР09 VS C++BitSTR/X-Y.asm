;—оставить подпрограмму с именем A_B типа
;   Procedure (var A: LONGWORD; const B:LONGWORD; L:LONGWORD)
;выполн€ющую вычитание битовых строк A:=A \ B длины L.

.386
.model FLAT,C
PUBLIC X_Y

.CODE
X_Y PROC
  PUSH EBP                        
  MOV EBP,ESP 

  X EQU DWORD PTR[EBP+8]           ;первая строка
  Y EQU DWORD PTR[EBP+12]           ;вторая строка
  L EQU DWORD PTR[EBP+16]          ;длина строк


  MOV ECX,L                     ;CX = длина строки
  SHR ECX,5                    
  INC ECX 
  MOV EDX,X
  MOV EBX,Y

M1:
  ; Напомню, что EAX - наш return из си(не путать со здешним супер pop)
  MOV EAX,[EBX]
  NOT EAX           
  AND EAX,[EDX]         
  
  ADD EDX,4 ;                
  ADD EBX,4
  
  LOOP M1             

  POP EBP ; Восстановили регистры
  RET ;12 3 переменных по 4 байта
X_Y ENDP ;Вообще не сходится, но какая разница. Здесь лучше
END