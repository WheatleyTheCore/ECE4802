from prettytable import PrettyTable

class LFSR:
    def __init__(self, m, gate_pos, initial_State):
        self.state = initial_State
        self.m = m
        self.initial_state = initial_State
        self.gate_pos = gate_pos

        
    def getNextBit(self): 
        newbit = None
        # next line is kinda illegable, just iterates over bits of gate pos from lsb to msb
        for i, bit in enumerate(reversed(bin(self.gate_pos)[2:])):
            bit = int(bit)
            if (bit == 0):
                continue
            if newbit == None:
                newbit = self.state >> i
            else: 
                newbit = newbit ^ (self.state >> i)
        newbit = newbit & 1
        newState = (self.state >> 1) | (newbit << (self.m - 1)) 
        retVal = self.state & 1
        self.state = newState
        return retVal

    def getPeriod(self):
        self.state = self.initial_state
        count = 0
        while True:
            count = count + 1
            self.getNextBit()
            if (self.state == self.initial_state):
                break
        return count

def vernamCipherEnc(lsfr: LFSR, plainbits):
    cipherbits = ''
    for i, bit in enumerate(bin(plainbits)[2:]):
        bit = int(bit)
        keyBit = lsfr.getNextBit()
        cipherbits = cipherbits + str(keyBit ^ bit)
    return cipherbits
    
            
if __name__ == "__main__":
    t = PrettyTable(['i', 'state', 'output'])
    lfsr1 = LFSR(9, 0b110000101, 0b001011000)
    t.add_row([0, "{0:b}".format(lfsr1.state), None])
    for i in range(30):
        bit = lfsr1.getNextBit()
        t.add_row([i + 1, "{0:b}".format(lfsr1.state), "{0:b}".format(bit)])
        
    print(t)
    
    t2 = PrettyTable(['i', 'state', 'output'])
    lfsr2 = LFSR(9, 0b110000100, 0b001011000)
    t2.add_row([0, "{0:b}".format(lfsr2.state), None])
    for i in range(30):
        bit = lfsr2.getNextBit()
        t2.add_row([i + 1, "{0:b}".format(lfsr2.state), "{0:b}".format(bit)])
        
    print(t2)
    
    lfsr1.state = lfsr1.initial_state # should have setter but,,,, too lazy
    lfsr2.state = lfsr2.initial_state
    
    print(f'encryped i: {vernamCipherEnc(lfsr1, 0b111011000001101110110100111110)}')
    print(f'encryped ii: {vernamCipherEnc(lfsr2, 0b111011000001101110110100111110)}')

