.386
.model flat, c

public CopyStr

.code
CopyStr proc
    push    ebp
    mov     ebp, esp
    push    esi
    push    edi
    
    mov     ecx, [ebp + 16] ; ����� (L)
    mov     edi, [ebp + 12] ; ������� (s2)
    mov     esi, [ebp + 8]  ; �������� (s1) 

    mov     eax, edi        ; result
    cld                     ; df := 0 DF � ���� �����������. 

    cmp     edi, esi        ; �������, �������� (s2, s1)    
    je      exit            ; ������� == �������� (s2 == s1)
    jb      norev           ; ������� < �������� (s2 < s1)

    ; ������� > �������� (s2 > s1)
    std                     ; df := 1
    add     edi, ecx ; ��������
    dec     edi
    add     esi, ecx ; ��������
    dec     esi
	; df - ������ ������
    norev:     
    rep     movsb; �� esi � edi ���������� �����  ecx - ������� ��������������� ���� df- 0 ����� ������� ���� df - 1 ������ ������

    exit:
    pop  edi
    pop  esi
    pop  ebp
	
    ret
CopyStr endp
end
