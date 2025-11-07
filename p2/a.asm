org 100h              ; COMファイルの開始位置

mov ah, 09h           ; DOSサービス：文字列表示
mov dx, msg           ; 表示する文字列のアドレス
int 21h               ; 呼び出し

mov ah, 4Ch           ; プログラム終了
int 21h

msg db 'Hello, World!$'