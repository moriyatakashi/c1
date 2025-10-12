def ab(pa):
    return open("x.txt").read()
def ac(pa,pb):
    return pa.split("\n")[pb][10:].split(" ")[0]
def ad(pa):
    print(" ".join(f'{pb:02x}'for pb in bytes.fromhex(pa)))
