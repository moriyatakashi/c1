plain_chars = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわがぎぐげござじずぜぞばびぶべぼぱぴぷぺぽ")
normal_chars = list("０１２３４５６７８９あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんっゃゅょ゛゜　")
def to_binary(char, table):
    return format(table.index(char), "06b")
def split_to_8bit_chunks(binary_str):
    return [binary_str[i:i+8].ljust(8, '0') for i in range(0, len(binary_str), 8)]
def format_for_display(s):
    return '\n'.join(['  '.join([s[i:i+3], s[i+3:i+6], s[i+6:i+9]]) for i in range(0, len(s), 10)])
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
input_str = "００００"
binary_list = [to_binary(c, normal_chars) for c in input_str]
fixed_bits = "0" * (16 + 20)
bitstream = (
    "00000000" +              
    binary_list[2] +         
    binary_list[1][:2] +     
    fixed_bits[:8] +         
    binary_list[1][3:5] +    
    binary_list[0] +         
    fixed_bits[8:16] +       
    binary_list[1][5] +      
    binary_list[3] +         
    binary_list[1][2] +      
    "0000000000000000000000000" +
    fixed_bits[16:] +        
    "00000"
)
bit_chunks = split_to_8bit_chunks(bitstream)
crc_result = crc(bit_chunks)
bit_chunks[0] = crc_result[6:] + bit_chunks[0][5:]
bit_chunks[8] = bit_chunks[8][:2] + crc_result[:6]
combined_bits = ''.join(bit_chunks)
padding = '0' * ((6 - len(combined_bits) % 6) % 6)
final_bits = combined_bits + padding
six_bit_chunks = [final_bits[i:i+6] for i in range(0, len(final_bits), 6)]
shift_value = int(six_bit_chunks[0][3:5], 2) + 1
for i in range(1, len(six_bit_chunks)):
    prev = int(six_bit_chunks[i-1], 2)
    curr = int(six_bit_chunks[i], 2)
    six_bit_chunks[i] = format((curr + prev + shift_value) & 63, "06b")
output = ''.join([plain_chars[int(x, 2)] for x in six_bit_chunks])
print(format_for_display(output))