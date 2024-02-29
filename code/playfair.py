def playfair_cipher(plaintext, key, mode):
    # Define the alphabet, excluding 'j'
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    # Remove whitespace and 'j' from the key and convert to lowercase
    key = key.lower().replace(' ', '').replace('j', 'i')
    # Construct the key square
    key_square = ''
    for letter in key + alphabet:
        if letter not in key_square:
            key_square += letter
    # Split the plaintext into digraphs, padding with 'x' if necessary
    plaintext = plaintext.lower().replace(' ', '').replace('j', 'i')
    replaceplaintext = ''
    if mode == 'encrypt':
        it = 0
        while it < len(plaintext) - 1:
            if plaintext[it] == plaintext[it + 1]:
                replaceplaintext += plaintext[it]
                replaceplaintext += 'x'
                it += 1
            else:
                replaceplaintext += plaintext[it]
                replaceplaintext += plaintext[it + 1]
                it += 2
        replaceplaintext += plaintext[-1] if it < len(plaintext) else ''
        plaintext = replaceplaintext

    if len(plaintext) % 2 == 1:
        plaintext += 'x'
    digraphs = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]

    # Define the encryption/decryption functions
    def encrypt(digraph):
        a, b = digraph # Destructuring 
        row_a, col_a = divmod(key_square.index(a), 5) # divmod(5, 2) = 2,1
        row_b, col_b = divmod(key_square.index(b), 5)
        if row_a == row_b:
            col_a = (col_a + 1) % 5
            col_b = (col_b + 1) % 5
        elif col_a == col_b:
            row_a = (row_a + 1) % 5
            row_b = (row_b + 1) % 5
        else:
            col_a, col_b = col_b, col_a
        return key_square[row_a * 5 + col_a] + key_square[row_b * 5 + col_b]

    def decrypt(digraph):
        a, b = digraph
        row_a, col_a = divmod(key_square.index(a), 5)
        row_b, col_b = divmod(key_square.index(b), 5)
        if row_a == row_b:
            col_a = (col_a - 1) % 5
            col_b = (col_b - 1) % 5
        elif col_a == col_b:
            row_a = (row_a - 1) % 5
            row_b = (row_b - 1) % 5
        else:
            col_a, col_b = col_b, col_a
        return key_square[row_a * 5 + col_a] + key_square[row_b * 5 + col_b]

    # Encrypt or decrypt the plaintext
    result = ''
    for digraph in digraphs:
        if mode == 'encrypt':
            result += encrypt(digraph)
        elif mode == 'decrypt':
            result += decrypt(digraph)

    # Return the result
    return result


# Example usage
# plaintext = 'I am improving'
plaintext = 'I am improving'
key = 'MONARCHY'
ciphertext = playfair_cipher(plaintext, key, 'encrypt')
print("----------------------------------------")

print("Plaintext : ",plaintext)  
print("Encrypted Text : ",ciphertext)  # outputs: "sbaeolmnxfyq"
decrypted_text = playfair_cipher(ciphertext, key, 'decrypt')
print("Decrypted Text : ",decrypted_text)  # Output : iamimproving
# (Note: 'x' is added as padding)
