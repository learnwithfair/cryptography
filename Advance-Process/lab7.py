import string

alphabet = string.ascii_lowercase
mp = dict(zip(alphabet, range(len(alphabet))))
mp2 = dict(zip(range(len(alphabet)), alphabet))


def bruteforce_encrypt(message):
    for i in range(26):
        encrypted_message = ''
        for j in range(len(message)):
            encrypted_message += mp2[(mp[message[j]] + i) % 26]
        print('%d' % i, encrypted_message)


def bruteforce_decrypt(encrypted_message):
    for i in range(26):
        decrypted_message = ''
        for j in range(len(encrypted_message)):
            decrypted_message += mp2[(mp[encrypted_message[j]] - i + 26) % 26]
        print('%d' % i, decrypted_message)


print('-' * 50)
print('Encryption')
print('-' * 50)
bruteforce_encrypt('hello')
print('-' * 50)
print('Decryption')
print('-' * 50)
bruteforce_decrypt('khoor')
print('-' * 50)
