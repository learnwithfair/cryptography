import string

alphabet = string.ascii_uppercase
# letter to number mapping
mp = dict(zip(alphabet, range(len(alphabet))))
# number to letter mapping
mp2 = dict(zip(range(len(alphabet)), alphabet))


def caesar_encrypt(message, shift):
    encrypted_message = ''
    for char in message:
        encrypted_message += mp2[(mp[char] + shift) % 26]
    return encrypted_message


def caesar_decrypt(caesar_message, shift):
    decrypted_message = ''
    for char in caesar_message:
        decrypted_message += mp2[(mp[char] - shift + 26) % 26]  # plus 26 is used to prevent negative value
    return decrypted_message


message = input("Enter Message to encrypt: ").upper()
shift = int(input("Enter Shift To Encrypt: "))
encrypted_message = caesar_encrypt(message, shift)
print('Encrypted Message:', encrypted_message)
print('Decrypted Message:', caesar_decrypt(encrypted_message, shift))