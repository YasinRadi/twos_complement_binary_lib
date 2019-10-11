import numpy as np

BIT_PAD = 32 + 1 # Offset to detect overflow

# Conversions

def hex_to_bin(h):
    h = int(h, 16) if 'str' in str(type(h)) else h
    return np.binary_repr(int(h), BIT_PAD)

def hex_to_dec(h):
    b = hex_to_bin(h)
    if int(b[0]):
        b = neg(dec_to_bin(bin_to_dec(b)))
        return -bin_to_dec(b)
    return int(str(h), 16)

def bin_to_hex(b):
    return fmt_hex(hex(int(b, 2)))

def bin_to_dec(b):
    if int(b[0]):
        b = neg(bin((int(b, 2)))[2:])
        return -(int(b, 2))
    return int(b, 2)

def dec_to_hex(d):
    return fmt_hex(hex(d))

def dec_to_bin(d):
    return np.binary_repr(d, BIT_PAD)

# Formatting
def fmt(b):
    off, n = lim(b)
    return (off, ' '.join([n[i : i + 4] for i in range(0, len(n), 4)]))

def fmt_hex(h):
    return f'0x{h[2:].zfill(BIT_PAD // 4).upper()}'

def lim(b):
    off = 1 if len(b) > 32 else 0
    return (off, ((b[::-1])[:BIT_PAD])[::-1])

# Bin ops
def add_bin(b1, b2):
    return dec_to_bin(bin_to_dec(b1) + bin_to_dec(b2))

# 2's Complement
def operands_comp(b1, b2):
    if b1[0] == b2[0]:
        b2 = neg(b2)
    return b1, b2

def neg(n):
    i = n.rfind('1')
    l = ''.join(map(lambda x: '0' if int(x) else '1', n[:i]))
    return f'{l}{n[i:]}'

# Operations

def add_2s_hex(h1, h2):
    r = add_bin(hex_to_bin(h1), hex_to_bin(h2))
    return fmt(r), fmt_hex(bin_to_hex(r))

def sub_2s_hex(h1, h2):
    b1, b2 = operands_comp(hex_to_bin(h1), hex_to_bin(h2))
    r = add_bin(b1, b2)
    return fmt(r), fmt_hex(bin_to_hex(r))

def add_2s_dec(d1, d2):
    b1 = dec_to_bin(d1)
    b2 = dec_to_bin(d2)
    return fmt(add_bin(b1, b2))

def sub_2s_dec(d1, d2):
    b1, b2 = operands_comp(dec_to_bin(d1), dec_to_bin(d2))
    return fmt(add_bin(b1, b2))

def add_2s_bin(b1, b2):
    return fmt(add_bin(b1, b2))

def sub_2s_bin(b1, b2):
    b1, b2 = operands_comp(b1, b2)
    return fmt(add_2s_bin(b1, b2))