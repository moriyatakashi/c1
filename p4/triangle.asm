BITS 16
ORG 0x7C00

start:
    ; モード13hに切り替え
    mov ax, 0x0013
    int 0x10

    ; VGAメモリセグメント設定
    mov ax, 0xA000
    mov es, ax

    ; 三角形の底辺を描画（水平線）
    mov cx, 60         ; x開始
.draw_loop:
    mov ax, 150        ; y座標
    mov bx, 320
    imul ax, bx        ; ax = y * 320
    add ax, cx         ; ax = y * 320 + x
    mov di, ax
    mov al, 1          ; 青色（パレット番号）
    mov [es:di], al
    inc cx
    cmp cx, 160
    jl .draw_loop

hang:
    jmp hang

times 510 - ($ - $$) db 0
dw 0xAA55