def brute_force_decrypt(ciphertext):
    for shift in range(26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")


def brute_force_encrypt(plainText):
    for shift in range(26):
        encrypted_text = caesar_encrypt(plainText, shift)
        print(f"Shift {shift}: {encrypted_text}")


def caesar_encrypt(plainText, shift):
    encrypted_text = ""
    for char in plainText:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text


plantext='hello'
print('Brute Force Encryption for Caesar Cipher:')
brute_force_encrypt(plantext)

ciphertext = "khoor"
print("\nBrute Force Decryption for Caesar Cipher:")
brute_force_decrypt(ciphertext)