p:
  push rbp
  mov rbp, rsp
  sub rsp, 16
  mov DWORD PTR [rbp-4], edi
  cmp DWORD PTR [rbp-4], 0
  js .L2
  cmp DWORD PTR [rbp-4], 0
  je .L3
  mov eax, DWORD PTR [rbp-4]
  sub eax, 1
  mov edi, eax
  call p
  imul eax, DWORD PTR [rbp-4]
  jmp .L6
.L3:
  mov eax, 1
  jmp .L6
.L2:
  mov eax, -1
.L6:
  leave
  ret
main:
  push rbp
  mov rbp, rsp
  sub rsp, 16
  mov DWORD PTR [rbp-4], 5
  mov eax, DWORD PTR [rbp-4]
  mov edi, eax
  call p
  mov DWORD PTR [rbp-8], eax
  mov eax, 0
  leave
  retN