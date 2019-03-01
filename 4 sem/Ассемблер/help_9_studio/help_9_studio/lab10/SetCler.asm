.386 
.model FLAT,C 
PUBLIC SetCler

.CODE
SetCler PROC
  PUSH EBP
  MOV EBP,ESP                 

  S EQU DWORD PTR[EBP+8]         ;наша строка
  L EQU DWORD PTR[EBP+12]        ;длина строки
  N EQU DWORD PTR[EBP+16]        ;номер разр¤да
  P EQU DWORD PTR[EBP+20]        ;параметр

  MOV ECX,N                  
  MOV EBX,S   
  
  CMP ECX,32
  JNA M0  
  
  SUB ECX,32 
  ADD EBX,4 

M0:
  CMP P,0                      
  JE M1                
  BTS [EBX], ECX 
  JMP M2
M1:
  BTR [EBX], ECX  

M2:
  POP EBP
  RET
SetCler ENDP
END