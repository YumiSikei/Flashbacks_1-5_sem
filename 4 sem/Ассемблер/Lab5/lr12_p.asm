PUBLIC factorial


CSEG SEGMENT PARA PUBLIC 'CODE'
	assume CS:CSEG
factorial proc near
	factorial1:               
		cmp bx, 1              
		je f_ret         
		dec bx                                 
		call factorial 
		inc bx
		mul bx	 
	f_ret:               
		ret           
factorial endp
CSEG ENDS
END
