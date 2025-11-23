BITS 16
ORG 0x7C00

start:
    mov si, msg

print_loop:
    lodsb
    or al, al
    jz restart
    mov ah, 0x0E
    int 0x10
    jmp print_loop

restart:
    mov si, msg
    jmp print_loop

msg db 'HELLO WORLD ', 0

times 510-($-$$) db 0
dw 0xAA55
