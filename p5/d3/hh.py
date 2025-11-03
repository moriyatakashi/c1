# HELLO.bin を読み込む
with open("HELLO.bin", "rb") as f:
    bin_data = f.read()

# 仮想メモリ（64KB）にロード
memory = [0x00] * 0x10000
load_addr = 0x0200
for i, byte in enumerate(bin_data):
    memory[load_addr + i] = byte

# $0200 から文字列を抽出
output = []
addr = load_addr
while memory[addr] != 0x00 and addr < 0x10000:
    output.append(chr(memory[addr]))
    addr += 1

print("6502メモリ出力:", "".join(output))
