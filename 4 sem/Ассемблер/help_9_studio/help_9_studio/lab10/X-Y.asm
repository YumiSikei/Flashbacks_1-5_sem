.386
.model FLAT,C
PUBLIC X_Y

.CODE
X_Y PROC
 PUSH EBP                        
  MOV EBP,ESP 

  X EQU DWORD PTR[EBP+8]           ;������ ������
  Y EQU DWORD PTR[EBP+12]           ;������ ������
  L EQU DWORD PTR[EBP+16]          ;����� �����

    MOV ECX,L                     ;CX = ����� ������
  SHR ECX,5                    
  INC ECX 
  MOV EDX,X
  MOV EBX,Y

M1:
 MOV EAX,[EBX]
  
  NOT EAX           
  AND EAX,[EDX]         
  
  ADD EDX,4 ; ��� ����� �� ��������, ���� ����������                
  ADD EBX,4
  
  LOOP M1          
  POP EBP ; ������������ ��������
  RET ;12 3 ���������� �� 4 �����
X_Y ENDP ;������ �� ��������, �� ����� �������. ����� �����
END