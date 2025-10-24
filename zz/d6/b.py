import ctypes
def aa(pa):
    a = ctypes.CDLL("bin/a.so")
    a.a.argtypes = [ctypes.c_char_p]
    a.a(pa.encode("utf8"))
