global main
extern main
extern sleep

section .data
i dq 0
max dq 20
s db "i is %d\n", 0

section .text
main:
sub rsp, 0x28

L4:
mov rax, [i]
cmp rax, [max]
jge L9

L5:
mov rax, [i]
mov rax, [1]
jz L7

L6:
mov rdi, [s]
mov rsi, [i]
mov rdx, [0]
call printf

L7:
mov rax, [i]
inc rax
mov [i], rax

L8:
jmp L4

L9:
add rsp, 0x28
ret