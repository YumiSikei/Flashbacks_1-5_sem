p:
  push rbp
  mov rbp, rsp
  sub rsp, 16
  mov DWORD PTR [rbp-4], edi
  mov QWORD PTR [rbp-16], rsi
  cmp DWORD PTR [rbp-4], 0
  je .L5
  cmp DWORD PTR [rbp-4], 1
  je .L5
  mov rax, QWORD PTR [rbp-16]
  mov eax, DWORD PTR [rax]
  imul eax, DWORD PTR [rbp-4]
  mov edx, eax
  mov rax, QWORD PTR [rbp-16]
  mov DWORD PTR [rax], edx
  mov eax, DWORD PTR [rbp-4]
  lea edx, [rax-1]
  mov rax, QWORD PTR [rbp-16]
  mov rsi, rax
  mov edi, edx
  call p
  jmp .L1
.L5:
  nop
.L1:
  leave
  ret
main:
  push rbp
  mov rbp, rsp
  sub rsp, 16
  mov DWORD PTR [rbp-4], 5
  mov DWORD PTR [rbp-8], 1
  lea rax, [rbp-8]
  mov rsi, rax
  mov edi, 5
  call p
  mov eax, 0
  leave
  ret