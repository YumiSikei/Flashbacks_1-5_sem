.386
.model flat, c

public CopyStr

.code
CopyStr proc
    push    ebp
    mov     ebp, esp
    push    esi
    push    edi
    
    mov     ecx, [ebp + 16] ; Длина (L)
    mov     edi, [ebp + 12] ; Приёмник (s2)
    mov     esi, [ebp + 8]  ; Источник (s1) 

    mov     eax, edi        ; result
    cld                     ; df := 0 DF — флаг направления. 

    cmp     edi, esi        ; приёмник, источник (s2, s1)    
    je      exit            ; приёмник == источник (s2 == s1)
    jb      norev           ; приёмник < источник (s2 < s1)

    ; приёмник > источник (s2 > s1)
    std                     ; df := 1
    add     edi, ecx ; приемник
    dec     edi
    add     esi, ecx ; источник
    dec     esi
	; df - справа налево
    norev:     
    rep     movsb; из esi в edi записывает байты  ecx - сколько последовательно если df- 0 слева направо если df - 1 справа налево

    exit:
    pop  edi
    pop  esi
    pop  ebp
	
    ret
CopyStr endp
end
