.386
.model FLAT,C
PUBLIC COUNT

.CODE
COUNT PROC

  push ebp          
  mov ebp,esp      

  S equ dword ptr[ebp+8]
  L equ dword ptr[ebp+12]
 
  mov eax,0            
  mov ebx,S                  
  mov ecx,L           
  mov edx,0    

M:
  bt [ebx], edx 
  adc eax, 0	
  inc edx
  loop M 
 
  pop ebp     
  ret
COUNT ENDP
END