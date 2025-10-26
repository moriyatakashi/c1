BITS 16
ORG 0x7C00
start:
    mov ax, 0x0013
    int 0x10
    mov ax, 0xA000
    mov es, ax
    mov cx, 60
.draw_loop:
    mov ax, 150
    mov bx, 320
    imul ax, bx
    add ax, cx
    mov di, ax
    mov al, 1
    mov [es:di], al
    inc cx
    cmp cx, 160
    jl .draw_loop
hang:
    jmp hang
times 510 - ($ - $$) db 0
dw 0xAA55