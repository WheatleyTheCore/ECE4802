import rsa
import user_utils

if __name__ == '__main__':
    print('------a-------')
    _RSA = rsa.RSA(17, 29, 17)
    print()
    
    print('------b-------')
    encrypted = _RSA.encrypt(13)
    print(f'ciphertext: {encrypted}')
    print()
    
    print('------c-------')
    decrypted = _RSA.decrypt(encrypted)
    print(f'decrypted value: {decrypted}')
    
