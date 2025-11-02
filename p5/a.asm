.db "NES", $1A
  .db 1
  .db 0
  .db $00
  .db $00
  .db $00, $00, $00, $00

  .org $8000
Reset:
  SEI
  CLD
  LDX #$40
  STX $4017
  LDX #$FF
  TXS

WaitVBlank:
  BIT $2002
  BPL WaitVBlank

  LDX #$FF
  STX $2000
  STX $2001
  STX $2005
  STX $2005

  LDA #$3F
  STA $2006
  LDA #$00
  STA $2006

  LDA #$12
  STA $2007
  LDA #$0F
  STA $2007
  STA $2007
  STA $2007

Forever:
  JMP Forever

  .org $FFFA
  .dw 0
  .dw Reset
  .dw 0