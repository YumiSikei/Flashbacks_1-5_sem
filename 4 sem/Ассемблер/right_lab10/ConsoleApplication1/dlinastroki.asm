.386
.model flat, c

public DlinaStroki 

.code
DlinaStroki proc
	
    push ebp
    mov  ebp, esp
    
    xor  eax, eax ; счетчик всех символов 
    mov  ebx, [ebp + 8]
    
    jmp  m1

    m2:
        inc  eax
    m1:
        mov  dl, [ebx + eax]  
        test dl, dl ; cmp dl, 0 
        jnz  m2

    pop  ebp
	
    ret
DlinaStroki endp
end
