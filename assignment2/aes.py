import numpy as np
from prettytable import PrettyTable
from user_utils import *

np.set_printoptions(formatter={'int':hex})

# used claude.ai to extract data from images

input_bits = np.zeros(128, dtype=int)

# First 32 bits (bits 1-32)
input_bits[0:32] = [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0]

# Next 32 bits (bits 33-64)
input_bits[32:64] = [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]

# Next 32 bits (bits 65-96)
input_bits[64:96] = [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]

# Last 32 bits (bits 97-128)
input_bits[96:128] = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1]


round_key_bits = np.zeros(128, dtype=int)

# First 32 bits (bits 1-32)
round_key_bits[0:32] = [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]

# Next 32 bits (bits 33-64)
round_key_bits[32:64] = [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1]

# Next 32 bits (bits 65-96)
round_key_bits[64:96] = [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1]

# Last 32 bits (bits 97-128)
round_key_bits[96:128] = [1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0]

sbox = np.array([
    # 0     1     2     3     4     5     6     7     8     9     a     b     c     d     e     f
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76], # 0
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0], # 1
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15], # 2
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75], # 3
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84], # 4
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf], # 5
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8], # 6
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2], # 7
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73], # 8
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb], # 9
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79], # a
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08], # b
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a], # c
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e], # d
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf], # e
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]  # f
], dtype=np.uint16)

def aes_sbox_sub(byte):
    hexByte = "{:02x}".format(byte)
    row = int(f'0x{hexByte[0:1]}', 16)
    col = int(f'0x{hexByte[1:2]}', 16)
    return sbox[row, col]

class AES:
    def __init__(self, input):
        assert len(input) == 128, "128-bit input requried"
        self.state = np.zeros((4, 4), dtype=np.uint16)
        for i in range(16):
            row = i // 4
            col = i % 4
            self.state[row, col] = bits_to_int(input[i * 8: i * 8 + 8])
        
    def getState(self): 
        return self.state
    
    def subBytes(self):
        newState = np.zeros((4, 4), dtype=np.uint16)
        for rowIndex, row in enumerate(self.state):
            for colIndex, element in enumerate(row):
                newState[rowIndex, colIndex] = aes_sbox_sub(element)
        self.state = newState
        
    def shiftRows(self):
        newState = np.zeros((4, 4), dtype=np.uint16)
        for rowIndex, row in enumerate(self.state):
            for colIndex, element in enumerate(row):
                newState[rowIndex, colIndex - rowIndex] = element
        self.state = newState
    
    def mixSingleColumn(self, col):
        # referenced https://en.wikipedia.org/wiki/Rijndael_MixColumns
        elementOne = gfMultiply(col[0], 2) ^ gfMultiply(col[1], 3) ^ gfMultiply(col[2], 1) ^ gfMultiply(col[3], 1) 
        elementTwo = gfMultiply(col[0], 1) ^ gfMultiply(col[1], 2) ^ gfMultiply(col[2], 3) ^ gfMultiply(col[3], 1) 
        elementThree = gfMultiply(col[0], 1) ^ gfMultiply(col[1], 1) ^ gfMultiply(col[2], 2) ^ gfMultiply(col[3], 3) 
        elementFour = gfMultiply(col[0], 3) ^ gfMultiply(col[1], 1) ^ gfMultiply(col[2], 1) ^ gfMultiply(col[3], 2) 
        
        return np.array([elementOne, elementTwo, elementThree, elementFour])
    
    def mixColumns(self):
        newState = np.zeros((4, 4), dtype=np.uint16)
        for i in range(4):
            newState[:, i] = self.mixSingleColumn(self.state[:, i])
        self.state = newState
        
    def getBits(self):
        flattened_bytes = self.state.flatten()
        byteStr = ""
        for byte in flattened_bytes:
            byteStr = byteStr + "{:08b}".format(byte)
        val = int(f'0b{byteStr}', 2)
        return int_to_bits(val)
    
    def final_key_xor(self):
        combined_with_key = []
        for bits in zip(self.getBits(), round_key_bits):
            combined_with_key.append(bits[0] ^ bits[1])
        return hex(bits_to_int(combined_with_key))
        

        
if __name__ == "__main__":
    
    assert aes_sbox_sub(0x01) == 0x7c, "sub issue"
    
    table = PrettyTable(['part', 'output'])
    table.padding_width = 3
    table.add_row(['a', hex(bits_to_int(input_bits))])    
    table.add_row(['', ''])    
    
    aes = AES(input_bits)
    table.add_row(['b', aes.getState()])
    table.add_row(['', ''])    
    
    aes.subBytes()
    table.add_row(['c', aes.getState()])
    table.add_row(['', ''])    
    
    aes.shiftRows()
    table.add_row(['d', aes.getState()])
    table.add_row(['', ''])    
    
    aes.mixColumns()
    table.add_row(['e', aes.getState()])
    table.add_row(['', ''])    
    
    table.add_row(['f', aes.final_key_xor()])
    table.add_row(['', ''])    
    
    print(table)

    
    
    