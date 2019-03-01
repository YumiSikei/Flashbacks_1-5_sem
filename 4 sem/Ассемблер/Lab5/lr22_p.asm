EXTRN factorial: near

STK SEGMENT PARA STACK 'STACK'
	db 100 dup(0)
STK ENDS

DSEG SEGMENT PARA PUBLIC 'DATA'
	X dw 5
	F dw ?

DSEG ENDS

CSEG SEGMENT PARA PUBLIC 'CODE'
	assume CS:CSEG, DS:DSEG, SS:STK
main:
	mov ax, DSEG
	mov ds, ax

	mov bx,X
	mov cx, offset F
	mov ax, 1
	call factorial	

	mov word ptr[bx], ax
	
	;mov cx, word ptr[bx]

	mov ax, 4c00h
	int 21h
CSEG ENDS

END main
