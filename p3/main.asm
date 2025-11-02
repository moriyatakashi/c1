
; NES ROMヘッダー (iNES format)
  .db "NES", $1A         ; マジックナンバー
  .db 1                  ; PRG ROMサイズ（16KB x 1）
  .db 0                  ; CHR ROMサイズ（0KB）
  .db $00                ; フラグ6
  .db $00                ; フラグ7
  .db $00, $00, $00, $00 ; 予約領域

; リセットベクタ
  .org $8000
Reset:
  SEI         ; 割り込み禁止
  CLD         ; 10進モード解除
  LDX #$40
  STX $4017   ; APUフレームカウンタ
  LDX #$FF
  TXS         ; スタック初期化

  INX
  STX $2000   ; PPU制御レジスタ1
  STX $2001   ; PPU制御レジスタ2
  STX $2005
  STX $2005

WaitVBlank:
  BIT $2002
  BPL WaitVBlank

  LDA #$3F
  STA $2006
  LDA #$00
  STA $2006

  LDA #$12    ; 背景色を青に設定
  STA $2007

Forever:
  JMP Forever

; 割り込みベクタ
  .org $FFFA
  .dw 0       ; NMI
  .dw Reset   ; RESET
  .dw 0       ; IRQ
