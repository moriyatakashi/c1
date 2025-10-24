org 0x7C00
start:
 mov si,a
.a:
 lodsb
 cmp al,0
 je .b
 mov ah,0x0E
 mov bh,0x00
 mov bl,0x07
 int 0x10
 jmp .a
.b:
 jmp .b
a db "OK",0
b:
 times 510-b+start db 0
 dw 0xAA55