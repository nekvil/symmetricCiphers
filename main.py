from collections import Counter
from colorama import Fore, Style, init


def encrypt(k, m):
    return ''.join(map(chr, [x + k for x in map(ord, m)]))


def encrypt_caesar(k, m):
    return ''.join(map(chr, [(x + k) % N for x in map(ord, m)]))


def decrypt_caesar(k, m):
    return ''.join(map(chr, [(x - k) % N for x in map(ord, m)]))


def hack(m):
    return decrypt_caesar(ord(Counter(m).most_common()[0][0]) - ord(' '), m)


def encrypt_vernam(k, m):
    k = k * (len(m) // len(k)) + k[:len(m) % len(k)]
    return ''.join(map(chr, [(x ^ y) % N for x, y in zip(map(ord, m), map(ord, k))]))


def decrypt_vernam(k, m):
    return encrypt_vernam(k, m)


if __name__ == '__main__':
    init()
    N = 65536
    # print(encrypt(4124, 'Hello!'))

    print(Style.BRIGHT + 'Caesar cipher' + Style.RESET_ALL)
    while True:
        try:
            caesar_key = int(input("Enter the key: "))
            break
        except ValueError:
            print(Fore.RED+"Invalid input"+Fore.RESET)
    caesar_text = 'Don’t wanna see me by yourself, by yourself, by yourself, by yourself'
    encrypt_caesar_text = encrypt_caesar(caesar_key, caesar_text)
    print('Encrypted text:', encrypt_caesar_text)
    print('Decrypted text:', decrypt_caesar(caesar_key, encrypt_caesar_text))
    print('Hacked text:', hack(encrypt_caesar_text))

    print(Style.BRIGHT + '\nVernam cipher' + Style.RESET_ALL)
    vernam_key = input('Enter the key: ')
    vernam_text = 'Don’t wanna see me by yourself, by yourself, by yourself, by yourself'
    encrypt_vernam_text = encrypt_vernam(vernam_key, vernam_text)
    print('Encrypted text:', encrypt_vernam_text)
    print('Decrypted text:', decrypt_vernam(vernam_key, encrypt_vernam_text))
