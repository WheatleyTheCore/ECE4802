from user_utils import *

class RSA:
    def __init__(self, p, q, e):
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = e
        
        assert euclidean_gcd(self.e, self.phi) == 1, 'e and phi must be coprime'
        self.d = int(modInv(self.e, self.phi))
        
        print(f'public key: {self.n, self.e}, private key: {self.d}')
        
    def encrypt(self, m, n = 'default', e = 'default'):
        if (n == 'default'):
            n = self.n
        if (e == 'default'):
            e = self.e
            
        ciphertext = squareAndMult(m, e, n)
        return ciphertext
            
            
    def decrypt(self, ciphertext):
        return squareAndMult(ciphertext, self.d, self.n)