.386 
.model FLAT,C 
PUBLIC SetCler

.CODE
SetCler PROC
  PUSH EBP
  MOV EBP,ESP                 

  S EQU DWORD PTR[EBP+8]         ;���� ������
  L EQU DWORD PTR[EBP+12]        ;����� ������
  N EQU DWORD PTR[EBP+16]        ;����� ������
  P EQU DWORD PTR[EBP+20]        ;��������

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