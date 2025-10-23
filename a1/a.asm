org 0x7C00

start:
    mov si, message

.print:
    lodsb
    cmp al, 0
    je .hang
    mov ah, 0x0E
    mov bh, 0x00
    mov bl, 0x07
    int 0x10
    jmp .print

.hang:
    jmp .hang

message db "Hello, world!", 0

pad:
    times 510 - (pad - start) db 0
    dw 0xAA55
