PUBLIC factorial

CSEG SEGMENT PARA PUBLIC 'CODE'
	assume CS:CSEG
factorial proc near
	factorial1:
		push bp                
		mov bp,sp               
		mov ax,[bp+4]     
		cmp ax, 1              
		je f_ret         
		dec ax                  
		push ax                
		call factorial      
		mul word ptr[bp+4]	 
		add sp, 2 
	f_ret:
		pop bp                
		ret           
factorial endp
CSEG ENDS
END

