[org 0x7c00]
bits 16

start:
    mov ax, 0x4F02        ; VBE function 02h - Set VBE Mode
    mov bx, 0x101         ; 640x480x8bpp (Mode 0x101)
    int 0x10              ; BIOS interrupt

    ; 画面を黒で塗りつぶす（簡易ループ）
    mov ax, 0xA000        ; VGA frame buffer segment
    mov es, ax
    xor di, di
    mov cx, 640*480
    xor al, al            ; 色（黒）
    rep stosb

hang:
    jmp hang              ; 無限ループ

times 510 - ($ - $$) db 0
dw 0xAA55