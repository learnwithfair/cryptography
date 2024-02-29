# Caesar Encryption Algorithm, C = E(k,p) = (p+k) mod 26
def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a')); # Generate ASCII value for lower case
            else:
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A')); # Generate ASCII value for upper case
        else:
            encrypted_text += char
    return encrypted_text

# Caesar Decryption Algorithm, C = E(k,p) = (p-k) mod 26
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a')) # Generate ASCII value lower case
            else:
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A')) # Generate ASCII value for upper case
        else:
            decrypted_text += char
    return decrypted_text


plaintext = input("Enter Plaintext : ") # Plaintext = Hello Rahatul
shift = int(input("Enter Key: ")) # key = 3
print("----------------------------------------")
ciphertext = caesar_encrypt(plaintext, shift) 
print(f"Caesar Cipher Encryption: {ciphertext}")
plaintext=caesar_decrypt(ciphertext,shift)
print(f"Caesar Cipher Decryption: {plaintext}")

# Output
# Caesar Cipher Encryption: Khoor Udkdwxo
# Caesar Cipher Decryption: Hello Rahatul