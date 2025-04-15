import rsa
import user_utils

if __name__ == '__main__':
    # print('------a-------')
    # _RSA = rsa.RSA(17, 29, 17)
    # print()
    
    # print('------b-------')
    # encrypted = _RSA.encrypt(13)
    # print(f'ciphertext: {encrypted}')
    # print()
    
    # print('------c-------')
    # decrypted = _RSA.decrypt(encrypted)
    # print(f'decrypted value: {decrypted}')
    
    print('------b-------')
    print(f'gcd(8, 17) = {user_utils.euclidean_gcd(8, 17)}')
    print(f'gcd(1752487, 985213679) = {user_utils.euclidean_gcd(1752487, 985213679)}')
    print(f'gcd(3546218, 7854316985) = {user_utils.euclidean_gcd(3546218, 7854316985)}')
    print()
    
    print('------c-------')
    inv = [(8, 17), (5, 17), (5, 37), (10, 15), (1752487, 9852136479), (3546218, 7854316985)]
    for i, m in inv:
        print(f'inverse of {i} mod {m} = {user_utils.modInv(i, m) or 'DNE'}')
    print()
    
    print('------d-------')
    m = 216
    for i in range(216):
        if (user_utils.modInv(i, m) == None):
            print(i, end=', ')
    print()
    
    print('------d-------')
    for i in [2, 3, 29]:
        print(f'{i} ^ 128 mod 113 = {(i**128) % 113}')
    
