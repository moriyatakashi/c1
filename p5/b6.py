# 文字リスト（変換用）
plain_chars = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわがぎぐげござじずぜぞばびぶべぼぱぴぷぺぽ")
normal_chars = list("０１２３４５６７８９あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんっゃゅょ゛゜　")

# 文字を6ビットのバイナリに変換
def to_binary(char, table):
    return format(table.index(char), "06b")

# 文字列を8ビットずつに分割（最後は0で埋める）
def split_to_8bit_chunks(binary_str):
    return [binary_str[i:i+8].ljust(8, '0') for i in range(0, len(binary_str), 8)]

# 表示用に整形
def format_for_display(s):
    return '\n'.join(['  '.join([s[i:i+3], s[i+3:i+6], s[i+6:i+9]]) for i in range(0, len(s), 10)])

# CRC計算
def crc(bits):
    r = len(bits) * 257
    for i in reversed(range(len(bits))):
        o = int(bits[i], 2)
        for _ in range(8):
            if ((r >> 8) ^ o) & 128:
                r = ((r << 1) ^ 4129) & 0xFFFF
            else:
                r = (r << 1) & 0xFFFF
            o = (o << 1) & 0xFF
    return format(r & 2047, "011b")

# 入力文字列（4文字）
input_str = "００００"

# 入力文字列をバイナリに変換
binary_list = [to_binary(c, normal_chars) for c in input_str]

# extra = 0 を直接使用（20ビット回転）
rotated_extra = "0" * 20
rotated_extra = rotated_extra[4:] + rotated_extra[:4]

# group = 0 を直接使用（16ビット）
group_bits = "0" * 16

# メインのビット列構築
bitstream = (
    "00000000" +
    binary_list[2] +
    binary_list[1][:2] +
    group_bits[:8] +
    binary_list[1][3:5] +
    binary_list[0] +
    group_bits[8:] +
    binary_list[1][5] +
    binary_list[3] +
    binary_list[1][2] +
    "000000000000" +
    "00000" +
    "00000000" +
    rotated_extra +
    "0000" +
    "0"
)

# 8ビット分割
bit_chunks = split_to_8bit_chunks(bitstream)

# 特定条件で置き換え
if len(bit_chunks) == 40:
    bit_chunks[8] = bit_chunks[39]

# CRC適用
crc_result = crc(bit_chunks)
bit_chunks[0] = crc_result[6:] + bit_chunks[0][5:]
bit_chunks[8] = bit_chunks[8][:2] + crc_result[:6]

# 6ビットに再分割
combined_bits = ''.join(bit_chunks)
padding = '0' * ((6 - len(combined_bits) % 6) % 6)
final_bits = combined_bits + padding
six_bit_chunks = [final_bits[i:i+6] for i in range(0, len(final_bits), 6)]

# シフト値と加算処理
shift_value = int(six_bit_chunks[0][3:5], 2) + 1
for i in range(1, len(six_bit_chunks)):
    prev = int(six_bit_chunks[i-1], 2)
    curr = int(six_bit_chunks[i], 2)
    six_bit_chunks[i] = format((curr + prev + shift_value) & 63, "06b")

# 最終出力
output = ''.join([plain_chars[int(x, 2)] for x in six_bit_chunks])
print(format_for_display(output))