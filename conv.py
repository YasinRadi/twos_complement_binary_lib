
ZERO_PAD = 32

# Conversions

def hex_to_bin(h):
    h = int(h, 16) if 'str' in str(type(h)) else h
    return bin(int(h))[2:].zfill(ZERO_PAD)

def hex_to_dec(h):
    b = hex_to_bin(h)
    if int(b[0]):
        b = neg(dec_to_bin(bin_to_dec(b) - 1))
        return -bin_to_dec(b)
    return int(str(h), 16)

def bin_to_hex(b):
    return hex(int(b, 2)).upper().replace('X', 'x')

def bin_to_dec(b):
    if int(b[0]):
        b = neg(b)
        return -(int(b, 2))
    return int(b, 2)

def dec_to_hex(d):
    return hex(d).upper().replace('X', 'x')

def dec_to_bin(d):
    n = False
    if d < 0:
        d = -d
        n = True
    d = bin(d)[2:].zfill(ZERO_PAD)
    return neg(d, 1) if n else d 

# Formatting
def fmt(b):
    off, n = lim(b)
    return (off, ' '.join([n[i : i + 4] for i in range(0, len(n), 4)]))

def fmt_hex(h):
    return f'0x{h[-8:]}' if len(h) > 10 else h

def lim(b):
    off = 1 if len(b) > 32 else 0
    return (off, ((b[::-1])[:ZERO_PAD])[::-1])

# Bin ops
def add_bin(b1, b2):
    return dec_to_bin(bin_to_dec(b1) + bin_to_dec(b2))

# 2's Complement
def add_one(b):
    return bin((int(b, 2) + 1))[2:].zfill(ZERO_PAD)

def operands_comp(b1, b2):
    if int(b1[0]):
        b1 = neg(b1)
    if not int(b2[0]):
        b2 = neg(b2)
    return b1, b2

def neg(n, plus = None):
    l = ''.join(map(lambda x: '0' if int(x) else '1', n))
    return l if not int(l[0]) or plus else add_one(l)

# Operations

def add_2s_hex(h1, h2):
    b1 = hex_to_bin(h1)
    b2 = hex_to_bin(h2)
    r = add_bin(b1, b2)
    return fmt(r), fmt_hex(bin_to_hex(r))

def sub_2s_hex(h1, h2):
    b1, b2 = operands_comp(hex_to_bin(h1), hex_to_bin(h2))
    return add_bin(b1, b2)

def add_2s_dec(d1, d2):
    b1 = dec_to_bin(d1)
    b2 = dec_to_bin(d2)
    return fmt(add_bin(b1, b2))

def sub_2s_dec(d1, d2):
    b1, b2 = operands_comp(dec_to_bin(d1), dec_to_bin(d2))
    return fmt(add_bin(b1, b2))

def add_2s_bin(b1, b2):
    return bin(add_bin(b1, b2))[2:].zfill(ZERO_PAD)

def sub_2s_bin(b1, b2):
    b1, b2 = operands_comp(b1, b2)
    return fmt(add_2s_bin(b1, b2))


if __name__ == '__main__':
    r2 = 0x0f0f0f0f
    r3 = 0x11110000
    
    r3 = neg(hex_to_bin(r3))
    r3 = bin_to_hex(r3)

    # print(neg(hex_to_bin(r3)))

    b = 55
    c = -55
    bb = dec_to_bin(b)
    cc = dec_to_bin(c)

    print(bin_to_dec(bb))
    print(bin_to_dec(cc))

# 1110 1110 1110 1111 0000 0000 0000 0000