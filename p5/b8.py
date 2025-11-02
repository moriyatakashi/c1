l1 = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわがぎぐげござじずぜぞばびぶべぼぱぴぷぺぽ")

def f2(pa): return [pa[i:i+8].ljust(8, '0') for i in range(0, len(pa), 8)]

def f3(pa):
    b = len(pa) * 257
    for i in reversed(range(len(pa))):
        a = int(pa[i], 2)
        for _ in range(8):
            b = ((b << 1) ^ 4129 if ((b >> 8) ^ a) & 128 else b << 1) & 0xFFFF
            a = (a << 1) & 0xFF
    return format(b & 2047, "011b")

a3 = f2("0" * 98)
a4 = f3(a3)
a3[0] = a4[6:] + a3[0][5:]
a3[8] = a3[8][:2] + a4[:6]
a5 = ''.join(a3)
a6 = a5 + '0' * ((6 - len(a5) % 6) % 6)
a7 = [a6[i:i+6] for i in range(0, len(a6), 6)]

for i in range(1, len(a7)):
    a7[i] = format((int(a7[i], 2) + int(a7[i-2], 2) + int(a7[0][3:5], 2) + 1) & 63, "06b")

print(''.join([l1[int(x, 2)] for x in a7]))