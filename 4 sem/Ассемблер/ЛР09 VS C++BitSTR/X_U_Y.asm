;��������� ������������ � ������ X_U_Y ����
;   Procedure (var X: LONGWORD; const Y:LONGWORD; L:LONGWORD)
;����������� ����������� ������� ����� X:=X U Y ����� L.

.386
.model FLAT,C
PUBLIC X_U_Y

.CODE
X_U_Y PROC

; ��� ��� ������� �������. ��� ��� ������ ��������? 
PUSH EBP                
MOV EBP,ESP  

X EQU DWORD PTR[EBP+8]           ;������ ������
Y EQU DWORD PTR[EBP+12]           ;������ ������
L EQU DWORD PTR[EBP+16]            ;����� �����             

  MOV ECX,L                       ;CX = ����� �����
  SHR ECX,5        
  INC ECX                      
  MOV EBX,X
  MOV EDX,Y

M1:
  MOV EAX,[EDX]
  ; �������� Y(1000) ��� ��������� ������ ������������ 
  OR EAX, [EBX]
  ADD EBX,4                   
  ADD EDX,4

  LOOP M1                         

  RET
X_U_Y ENDP
END