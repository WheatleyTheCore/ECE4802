from prettytable import PrettyTable
from functools import reduce

def euclidean_gcd(a, b):
    while True:
        r = a % b 
        if r == 0:
            break
        a = b
        b = r
    return b
    
    
def extended_euclidean(a, b):
    # referenced crypto101 v6b 
    if b == 0:
        d = a
        x = 1
        y = 0
        return (d, x, y)
    
    x1 = y2 = 0
    x2 = y1 = 1
    
    q = x = y = None
    
    while b > 0:
        r = a % b
        q = (a - r)/b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
        
    d = a
    x = x2
    y = y2
    return (d, x, y)
        
def modInv(a, m):
    # can just use pow(a, -1, m) but just here for completeness of answer
    d, x, y = extended_euclidean(a, m)
    assert d == 1, 'a and m aren\'t coprime! :(('
    return x % m

def bits_to_int(bit_array):
    out = 0
    for bit in bit_array:
        out = (out << 1) | bit
    return out

def int_to_bits(n):
    return [int(digit) for digit in bin(n)[2:]]

def stringify_bit_arr(bit_arr):
    output = ""
    for bit in bit_arr:
        output = output + str(bit)
    return output

def squareAndMult(a, e, m):
    bits = int_to_bits(e)
    table = PrettyTable(['stage', 'value'])
    table.add_row(['(a, e, n)', f'{a}, {e}, {m}'])
    table.add_row(['binary', stringify_bit_arr(bits)])
    bits.reverse() # so we get lsb first
    squares = []
    for index, bit in enumerate(bits):
        if bit:
            squares.append(a**(2**index) % m)
    table.add_row(['m^2^i mod n', reduce(lambda x,y: x + f'*{y}', squares[1:], str(squares[0]))]) # mod n introduced here so the numbers don't get too huge
    value = reduce(lambda x, y: (x * y) % m, squares, 1) # mod m every time to also keep numbers small
    table.add_row(['result', value])
    print(table)
    return value

