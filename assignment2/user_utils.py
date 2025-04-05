def bits_to_int(bit_array):
    out = 0
    for bit in bit_array:
        out = (out << 1) | bit
    return out

def int_to_bits(n):
    return [int(digit) for digit in '{0:04b}'.format(n)]

def stringify_bit_arr(bit_arr):
    output = ""
    for bit in bit_arr:
        output = output + str(bit)
    return output

def computeSBox(sbox, bits):
    assert len(bits) == 6, "incorrect number of bits"
    sbox_row = (bits[0] << 1) | bits[1]
    sbox_col = bits_to_int(bits[1:5])
    sbox_val = sbox[sbox_row, sbox_col]
    return int_to_bits(sbox_val)

def gfMultiply(a, b):
    # help from https://stackoverflow.com/questions/70261458/how-to-perform-addition-and-multiplication-in-f-28
    irreducable_poly_coef = 0b100011011             
    result = 0                       
    for i in range(8):
        result = result << 1
        if result & 0b100000000:
            result = result ^ irreducable_poly_coef  # if big enough, do modulo of irriducable poly.
        if b & 0b010000000:
            result = result ^ a
        b = b << 1
    return result
            
            