import json
from datetime import *
def aaa(text, filepath):
    data = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": text
    }
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))
def aa1(password, passDict):
    jumon = ""
    passTemp = password.copy()
    for i in range(len(password)):
        char = passTemp.pop(0)
        jumon += passDict[int(char, 2)]
    return jumon
def aa2(password):
    nShift = int(password[0][3:5], 2) + 1
    for i in range(1, len(password)):
        password[i] = format(
            ((int(password[i], 2) + int(password[i - 1], 2) + nShift) & 0x3F), "06b"
        )
    return password
def aa3(combined_str):
    return [combined_str[i : i + 6] for i in range(0, len(combined_str), 6)]
def aa4(bytes):
    combined_str = "".join(bytes)
    remainder = len(combined_str) % 6
    if remainder > 0:
        combined_str += "0" * (6 - remainder)
    return combined_str
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
def aa5(bytes):
    crc = calculate_crc(bytes)
    bytes[0] = crc[6:] + bytes[0][5:]
    bytes[8] = bytes[8][:2] + crc[:6]
    return bytes
def split_string(string):
    chunks = [string[i : i + 8] for i in range(0, len(string), 8)]
    if len(chunks[-1]) < 8:
        chunks[-1] = chunks[-1].ljust(8, "0")
    return chunks
def ba1(bytes_str, passDict):
    bytes = split_string(bytes_str)
    bytes = aa5(bytes)
    combined_str = aa4(bytes)
    password = aa3(combined_str)
    password = aa2(password)
    jumon = aa1(password, passDict)
    return jumon
