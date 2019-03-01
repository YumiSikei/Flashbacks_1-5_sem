;2.  Составить подпрограмму с именем Count типа
;      function (const S: LONGWORD; L:LONGWORD)
;возвращающую число единиц битовой строки S длины L.

.386
.model FLAT,PASCAL
PUBLIC COUNT

.CODE
COUNT PROC


push ebp          
mov ebp,esp      

; Опять дефайны  
S EQU dword ptr[ebp+12] ; наша строка  
L EQU dword ptr[ebp+8] ; длина строки
   
push edi                                      
mov ebx,S                               

mov edi, L                               ; В регистре EDI теперь хранится размер строки
mov eax, 0                               ; EAX - число единиц

BIG:                                     ; Внешний цикл
    cmp edi, 0
		jbe FINISH                         ; Если размер строки - 0, выходим
	cmp edi, 32
        ja AGAIN                         ; Если размер > 32, запускаем AGAIN

	mov ecx, edi  
    mov edi, 0	; ECX - счётчик лупа, поместили в него текущий размер строки
										 ; В это место можно попасть, только если размер строки  < 32
	                                     ; Поэтому edi содержит корректный остаток размера строки

	GO:
		bt  edx, ecx
		adc eax, 0	
	loop GO
	loop BIG     ; ECX = -1, вроде должно всегда выполняться

    AGAIN:                               ; Если размер > 32
        sub edi, 32                      ; Вычитаем из размера строки 32
		mov edx, [ebx]                   ; Сохраняем в регистр адрес начала DWORD(Двоичного слова), чей адрес [ebx]
		add ebx, 32                      ; Увеличиваем смещение ebx на 32. Не на 4, потому что ebx - не адрес, а 
		                                 ; смещение. А вообще нужно тестить.
		mov ecx, 33                      ; ECX - размер строки, максимум 32, за счёт лишнего лупа, пишем 33
		loop GO 
FINISH:
       pop edi
       pop ebp      
       ret 8 ; на вход пришло 2 аргумента по 4 байта.


;mov ebx, S ;Сама строка
;mov edi, L ;Длина строки
;mov eax, 0
;mov ecx, 1
;
;loop_extern:
;	push ecx
;	mov ecx, edi
;
;	cmp edi, 0
;		jbe fin
;		
;	mov edx, [ebx] 
;		
;	cmp edi, 32
;		jb loop_intern
;	
;	GREATER:
;		                   
;		add ebx, 32                                                      
;		;pop ecx     ; Ну тут в общем через пуш поп
;		;inc ecx		; Не хотелось совать в регистры
;		;push ecx	;
;		mov ecx, 32  
;		
;	
;	loop_intern:
;	    sub edi, 32  
;		bt edx, ecx
;		adc eax, 0
;	loop loop_intern
;	
;		bt edx, ecx
;		adc eax, 0
;	
;	;pop ecx
;	
;	loop loop_extern
;	
;fin:
;	pop ebp
;	ret 8
COUNT ENDP
END