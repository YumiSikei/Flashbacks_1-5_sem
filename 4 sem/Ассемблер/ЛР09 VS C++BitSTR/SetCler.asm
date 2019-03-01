;��������� ������������ � ������ SetCler ����
;   Procedure (var S:LONGWORD; L:LONGWORD; N:LONGWORD; P:LONGWORD)
;����������� ��������� ������� N ������� ������ S
;� ����, ���� P=0, � �������,���� P �� ����� 0.

.386 
.model FLAT,C 
PUBLIC SetCler

.CODE
SetCler PROC
  PUSH EBP
  MOV EBP,ESP                 

  S EQU DWORD PTR[EBP+8]         ;���� ������
  L EQU DWORD PTR[EBP+12]        ;����� ������
  N EQU DWORD PTR[EBP+16]        ;����� �������
  P EQU DWORD PTR[EBP+20]        ;��������
  
  MOV ECX,N ; ����������� �� ������������ ESI � EDI                  
  MOV EBX,S   

  CMP ECX,32
  JNA M0  ; ���� ����� ������� ������ ��� ����� 32, �� � �0
  
  SUB ECX,32 ; ����� ����� ������� -= 32;
  ADD EBX,4 ; ������� ����� ������ �� 4 ����� ������(��� ��� ����� 32 ����)

M0:
  CMP P,0                       ;���������� ����� � �����
  JE M1                         ;���� �����, �� ��������� �� ����� M1
  BTS [EBX], ECX                ;��������� ���� � 1
  JMP M2
M1:
  BTR [EBX], ECX                ;��������� ���� � 0

M2:
  POP EBP
  RET
SetCler ENDP
END