# CRC-16-CCITT implementation and byte adjustment algorithm

POLY = 0x1021
INIT = 0xFFFF

# Compute CRC-16-CCITT
def crc16_ccitt(data: bytes) -> int:
    crc = INIT
    for byte in data:
        crc ^= (byte << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = ((crc << 1) ^ POLY) & 0xFFFF
            else:
                crc = (crc << 1) & 0xFFFF
    return crc

# Adjust specified positions to achieve target CRC
# positions: list of indices in data to adjust
# target_crc: desired CRC value
# returns modified data
def adjust_bytes_for_crc(data: bytearray, positions, target_crc):
    # Compute current CRC
    current_crc = crc16_ccitt(data)
    print(f"Current CRC: {current_crc:04X}")

    # For demo: brute force last 2 bytes (positions length = 2)
    if len(positions) != 2:
        raise ValueError("Demo supports exactly 2 adjustable bytes")

    # Brute force search for values that produce target CRC
    for val in range(0, 65536):
        b1 = (val >> 8) & 0xFF
        b2 = val & 0xFF
        data[positions[0]] = b1
        data[positions[1]] = b2
        if crc16_ccitt(data) == target_crc:
            print(f"Found adjustment: byte[{positions[0]}]={b1:02X}, byte[{positions[1]}]={b2:02X}")
            return data

    raise RuntimeError("No solution found (unexpected)")

# Example usage
data = bytearray(b"HELLOCRC00")  # last two bytes will be adjusted
positions = [len(data)-2, len(data)-1]
target_crc = 0xABCD  # desired CRC

print(f"Original data: {data}")
adjusted_data = adjust_bytes_for_crc(data, positions, target_crc)
print(f"Adjusted data: {adjusted_data}")
print(f"Final CRC: {crc16_ccitt(adjusted_data):04X}")