import string

alphabetic = string.ascii_lowercase
mp = dict(zip(alphabetic, range(len(alphabetic))))
mp2 = dict(zip(range(len(alphabetic)), alphabetic))


def generateKey(message, key):
    key_word = ''
    for i in range(len(message)):
        key_word += key[i % len(key)]
    return key_word


def encrypt(message, key):
    encrypted_message = ''
    for i in range(len(message)):
        encrypted_message += mp2[(mp[message[i]] + mp[key[i]]) % 26]
    return encrypted_message


def decrypt(encrypted_message, key):
    decrypted_message = ''
    for i in range(len(encrypted_message)):
        decrypted_message += mp2[(mp[encrypted_message[i]] - mp[key[i]] + 26) % 26]
    return decrypted_message


message = 'wearediscoveredsaveyourself'
key = generateKey(message, 'deceptive')
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)
print('Encrypted Message: ', encrypted_message)
print('Decrypted Message: ', decrypted_message)
