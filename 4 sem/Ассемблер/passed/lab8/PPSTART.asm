.386
.model FLAT,PASCAL
PUBLIC START
extern COUNT:near, X_Y:near, SetCler:near, X_U_Y:near

.DATA
S 	DD 0,0,0,0
S1 	DD 00001111000011110000111100001111B,1010101B
           ;0-38 - ������� ������
S2 	DD 00111100001111000011110000111100B,1000001B
           ;0-38 - ������� ������
L DD 39    ;= ����� ������
; DD �� �� DWORD - ������� �����, �������� 4 �����

;��������� �����������, ������ ����� ������� ���� ������� CPU,
; ������������ ������������������� ���, ��������, ���� � ������, �������� .
; �������� ���������.
;�������� � ������ �\� COUNT �� ����� COUNT.ASM:
;�	��������� ������������ COUNT � ����� COUNT.ASM
;�	�������� COUNT. OBJ
;�	�������� � ������ ����� begin
;{$L COUNT .OBJ}
;FUNCTION COUNT:LONGWORD ; EXTERNAL;
;� � ����� ����� ASM END
;   PUSH OFFSET S1
;   PUSH L
;   CALL COUNT
;�	��������� ������� ������� COUNT
;�������� ������ ��������������� �������� � ������ � ��������
; ������������ SetCler �� ����� SetCler. ASM (��� ������ � �\� START, �� ����) � ������������ X_Y �� ����� X-Y. ASM (���� ����� � �\� START).
;���������� ���������� ����������� ��������� ���������� ������� Turbo Delphi


.CODE
START:
	; �������� ���������� �������� ��� ��������� �� ����� � ������ �������
   PUSH OFFSET S1     
   PUSH L                 
   CALL COUNT
   ; ���������

   PUSH OFFSET S1
   PUSH L      
   PUSH 1                
   PUSH 1                
   CALL SetCler 
   ; ���������   

   PUSH OFFSET S2
   PUSH L
   PUSH 34
   PUSH 0              
   CALL SetCler  
   ; ���������    

   PUSH OFFSET S1       
   PUSH OFFSET S2        
   PUSH L               
   CALL X_Y   
   ; ��������� 

	PUSH OFFSET S1       
   PUSH OFFSET S2        
   PUSH L               
   CALL X_U_Y   
   ; ���������  
   
   ; �������� ���������� �� ���������� �������� ������

RET;
END