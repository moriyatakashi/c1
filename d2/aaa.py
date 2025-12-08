from datetime import datetime
def calculate_crc(code):
    crc = len(code) * 0x0101
    for i in range(len(code) - 1, -1, -1):
        octed = code[i]
        octed = int(octed, 2)  
        for j in range(8):
            carry_bit = ((crc >> 8) ^ octed) & 0x80 != 0
            crc = (crc << 1) & 0xffff
            octed = (octed << 1) & 0xff
            if carry_bit:
                crc ^= 0x1021
    return format(crc & 0x07ff, "011b")
def split_string(string):
    chunks = [string[i:i+8] for i in range(0, len(string), 8)]
    if len(chunks[-1]) < 8:
        chunks[-1] = chunks[-1].ljust(8, '0')
    return chunks
def aa1(bytes_str,passDict):
  bytes = split_string(bytes_str)
  crc = calculate_crc(bytes)
  bytes[0] = crc[6:] + bytes[0][5:]
  bytes[8] = bytes[8][:2] + crc[:6]
  password = []
  combined_str = ''.join(bytes)
  remainder = len(combined_str) % 6
  if remainder > 0:
    combined_str += '0' * (6 - remainder)
  password = [combined_str[i:i+6] for i in range(0, len(combined_str), 6)]
  nShift = int(password[0][3:5], 2) + 1
  for i in range(1, len(password)):
    password[i] = format(((int(password[i], 2) + int(password[i - 1], 2) + nShift) & 0x3f), "06b")
  jumon = ""
  passTemp = password.copy()
  for i in range(len(password)):
    char = passTemp.pop(0) 
    jumon += passDict[int(char, 2)]
  return jumon