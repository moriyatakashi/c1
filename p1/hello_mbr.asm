; hello_mbr.asm
BITS 16
ORG 0x7C00

start:
    mov si, msg        ; DS:SI points to message
    mov ah, 0x0E       ; BIOS teletype output

.print_loop:
    lodsb              ; Load next char into AL
    cmp al, 0
    je .done
    int 0x10           ; Print character
    jmp .print_loop

.done:
    cli
    hlt                ; Halt CPU

msg db 'HELLO WORLD', 0

times 510 - ($ - $$) db 0  ; Fill up to 510 bytes
dw 0xAA55                  ; Boot signature (last 2 bytes)
