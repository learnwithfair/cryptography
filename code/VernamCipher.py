import random

alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
mp = dict(zip(alphabet, range(len(alphabet)))) # letter_to_index
mp2 = dict(zip(range(len(alphabet)), alphabet)) # Index to letter


def generate_key(length):
    key = ""
    for i in range(length):
        key += chr(random.randint(65, 90))  # ASCII codes for A-Z
    return key


def encrypt(plaintext, key):
    ciphertext = ""
    cipherCode = []
    for i in range(len(plaintext)):
        xor = mp[plaintext[i]] ^ mp[key[i]]
        cipherCode.append(xor)
        ciphertext += mp2[(mp['A'] + xor) % 26]
    return ciphertext, cipherCode


def decrypt(cipherCode, key):
    plaintext = ""
    for i in range(len(cipherCode)):
        xor = cipherCode[i] ^ mp[key[i]]
        plaintext += mp2[xor % 26]
    return plaintext


plaintext = "Rahatul Rabbi"
plaintext = plaintext.upper().replace(' ','')
# key = "RANCHOBABA"
key = generate_key(len(plaintext))
ciphertext, cipherCode = encrypt(plaintext, key)
ciphertext, cipherCode = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decryptedtext = decrypt(cipherCode, key)
print("Decrypted text:", decryptedtext)