;2.  Составить подпрограмму с именем Count типа
;      function (const S: LONGWORD; L:LONGWORD)
;возвращающую число единиц битовой строки S длины L.

.386
.model FLAT,C ; Теперь С вместо паскаля
PUBLIC COUNT

.CODE
COUNT PROC

;Пролог(неполный)
  push ebp          
  mov ebp,esp      

  ; тут теперь сначала +8, потом +12.(У них это неисправлено)
  S equ dword ptr[ebp+8] ; наша строка  
  L equ dword ptr[ebp+12] ; длина строки
 
  mov eax,0            
  mov ebx,S                  
  mov ecx,L           
  mov edx,0    

; Цикл
M:
  bt [ebx], edx 
  adc eax, 0	
  inc edx ; смещение растёт
  loop M 
 
  pop ebp   ; по поглашению должны защитить регистры    
  ret ;8 прощай гениальная очистка. Пусть кто то другой очистит память
COUNT ENDP; У них эта строчка почему то убрана. Но не надо так.
END