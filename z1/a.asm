[org 0x7c00]        ; ブートローダの開始位置
mov si, msg         ; SIに文字列のアドレスをセット

print_loop:
    lodsb           ; ALに文字をロード
    cmp al, 0
    je done
    mov ah, 0x0E    ; BIOSテレタイプ出力
    int 0x10
    jmp print_loop

done:
    hlt             ; CPU停止

msg db 'Hello World!', 0

times 510-($-$$) db 0  ; パディング
dw 0xAA55              ; ブートシグネチャ