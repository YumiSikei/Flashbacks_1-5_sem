;��������� ������������ � ������ A_B ����
;   Procedure (var A: LONGWORD; const B:LONGWORD; L:LONGWORD)
;����������� ��������� ������� ����� A:=A \ B ����� L.

.386
.model FLAT,PASCAL
PUBLIC X_Y

.CODE
X_Y PROC
; ��� ����� ���������� ������� ������, �� � �������� ���� ���
  PUSH EBP                        
  MOV EBP,ESP                     

  X EQU DWORD PTR[EBP+16]           ;������ ������
  Y EQU DWORD PTR[EBP+12]           ;������ ������
  L EQU DWORD PTR[EBP+8]          ;����� �����

  PUSH ESI                     
  PUSH EDI
  
  MOV ECX,L                     ;CX = ����� ������
  SHR ECX,5                    
  INC ECX 
  MOV EDI,X
  MOV ESI,Y
  
  ; ��� ��� ��� � X_U_Y, ��� ��� ��� ������������. � ���������� ������. ��������

  ; ����� ����� ������. ����� X = 111, � Y = 101

M1:
  ; �������, ��� EAX - ��� return �� ��(�� ������ �� ������� ����� pop)
  MOV EAX,[ESI]
  ; EAX = 101
  NOT EAX             ;�������� ���������� EAX, �������� ����� ��� ������� :)
  ; EAX = 010
  AND EAX,[EDI]                   ;����������(����� ������������ � ������)
  ; EAX = (010 & 111) = 010 (��, ���� ��� ������ ������� ��������)
  ADD EDI,4                       
  ADD ESI,4
  ; ��� ������ �������� ��������� ����� �� 4 ��� ����, ����� ���������� �����
  ; ������ ����� 32-�� ���
  LOOP M1                         

  POP EDI
  POP ESI
  POP EBP
  ; ����� ������������ ����
  RET 12 ; 3 ���������� �� 4 �����
X_Y ENDP
END