import json
from datetime import datetime
def aaa(text, filepath):
    data = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": text
    }
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))
def calculate_crc(code):
    crc = len(code) * 0x0101
    for i in range(len(code) - 1, -1, -1):
        octed = code[i]
        octed = int(octed, 2)
        for j in range(8):
            carry_bit = ((crc >> 8) ^ octed) & 0x80 != 0
            crc = (crc << 1) & 0xFFFF
            octed = (octed << 1) & 0xFF
            if carry_bit:
                crc ^= 0x1021
    return format(crc & 0x07FF, "011b")
def split_string(string):
    chunks = [string[i : i + 8] for i in range(0, len(string), 8)]
    if len(chunks[-1]) < 8:
        chunks[-1] = chunks[-1].ljust(8, "0")
    return chunks
def remove_elements(items, equip):
    if 0 not in items:
        return items, equip
    index = items.index(0)
    return items[:index], equip[:index]
def nameToBinary(char):
    return format(0, "06b")