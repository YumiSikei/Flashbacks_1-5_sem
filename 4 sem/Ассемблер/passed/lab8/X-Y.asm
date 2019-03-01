;—оставить подпрограмму с именем A_B типа
;   Procedure (var A: LONGWORD; const B:LONGWORD; L:LONGWORD)
;выполн€ющую вычитание битовых строк A:=A \ B длины L.

.386
.model FLAT,PASCAL
PUBLIC X_Y

.CODE
X_Y PROC
; Они опять перепутали местами пролог, но я пофиксил если что
  PUSH EBP                        
  MOV EBP,ESP                     

  X EQU DWORD PTR[EBP+16]           ;первая строка
  Y EQU DWORD PTR[EBP+12]           ;вторая строка
  L EQU DWORD PTR[EBP+8]          ;длина строк

  PUSH ESI                     
  PUSH EDI
  
  MOV ECX,L                     ;CX = длина строки
  SHR ECX,5                    
  INC ECX 
  MOV EDI,X
  MOV ESI,Y
  
  ; Тут все как в X_U_Y, так что без комментариев. В буквальном смысле. Ахахахаа

  ; Опять сразу пример. Пусть X = 111, а Y = 101

M1:
  ; Напомню, что EAX - наш return из си(не путать со здешним супер pop)
  MOV EAX,[ESI]
  ; EAX = 101
  NOT EAX             ;отрицаем содержимое EAX, работает также как кажется :)
  ; EAX = 010
  AND EAX,[EDI]                   ;объединяем(Опять записывается в первый)
  ; EAX = (010 & 111) = 010 (Да, чето мой пример слишком гениален)
  ADD EDI,4                       
  ADD ESI,4
  ; Как обычно сдвигаем указатели строк на 4 для того, чтобы обработать числа
  ; длиной более 32-ух бит
  LOOP M1                         

  POP EDI
  POP ESI
  POP EBP
  ; Опять восстановили стек
  RET 12 ; 3 переменных по 4 байта
X_Y ENDP
END