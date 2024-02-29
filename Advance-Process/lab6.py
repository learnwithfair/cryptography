import random
import string

alphabet = string.ascii_lowercase
mp = dict(zip(alphabet, range(len(alphabet))))
mp2 = dict(zip(range(len(alphabet)), alphabet))


def generateKey(length):
    key = ''
    for i in range(length):
        key += chr(random.randint(65, 90))
    return key


def encrypt(message, key):
    encrypted_message = ''
    encrypted_code = []
    for i in range(len(message)):
        xor = mp[message[i]] ^ mp[key[i]]
        encrypted_code.append(xor)
        encrypted_message += mp2[(mp['a'] + xor) % 26]
    return encrypted_message, encrypted_code


def decrypt(encrypted_code, key):
    decrypted_message = ''
    for i in range(len(encrypted_code)):
        xor = encrypted_code[i] ^ mp[key[i]]
        decrypted_message += mp2[xor % 26]
    return decrypted_message


message = 'oak'
key = generateKey(len(message)).lower()
# key='son'   #coh
encrypted_message, encrypted_code = encrypt(message, key)
decrypted_message = decrypt(encrypted_code, key)
print(encrypted_message)
print(decrypted_message)