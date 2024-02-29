import string


def playfair_cipher(message, key, mode):
    alphabet = string.ascii_lowercase.replace('j', '')
    message = message.lower().replace(' ', '').replace('j', 'i')
    key = key.lower().replace(' ', '').replace('j', 'i')
    keySquare = ''
    for char in key + alphabet:
        if char not in keySquare:
            keySquare += char
    operation = ''
    if mode == 'encrypt':
        it = 0
        while it < len(message) - 1:
            if message[it] == message[it + 1]:
                operation += message[it]
                operation += 'x'
                it += 1
            else:
                operation += message[it]
                operation += message[it + 1]
                it += 2
        operation += message[-1] if it < len(message) else ''
        message = operation
    if len(message) % 2 == 1:
        message += 'x'
    digraphs = [message[i:i + 2] for i in range(0, len(message), 2)]

    def encrypt(digraph):
        a, b = digraph
        row_a, col_a = divmod(keySquare.index(a), 5)
        row_b, col_b = divmod(keySquare.index(b), 5)
        if row_a == row_b:
            col_a = (col_a + 1) % 5
            col_b = (col_b + 1) % 5
        elif col_a == col_b:
            row_a = (row_a + 1) % 5
            row_b = (row_b + 1) % 5
        else:
            col_a, col_b = col_b, col_a
        return keySquare[row_a * 5 + col_a] + keySquare[row_b * 5 + col_b]

    def decrypt(digraph):
        a, b = digraph
        row_a, col_a = divmod(keySquare.index(a), 5)
        row_b, col_b = divmod(keySquare.index(b), 5)
        if row_a == row_b:
            col_a = (col_a - 1) % 5
            col_b = (col_b - 1) % 5
        elif col_a == col_b:
            row_a = (row_a - 1) % 5
            row_b = (row_b - 1) % 5
        else:
            col_a, col_b = col_b, col_a
        return keySquare[row_a * 5 + col_a] + keySquare[row_b * 5 + col_b]

    result = ''
    for digraph in digraphs:
        if mode == 'encrypt':
            result += encrypt(digraph)
        elif mode == 'decrypt':
            result += decrypt(digraph)
    return result


message = 'communication'
key = 'computer'
ciphertext = playfair_cipher(message, key, 'encrypt')
print('Cipher Text:', ciphertext)
decrypted_text = playfair_cipher(ciphertext, key, 'decrypt')
print('Decrypted Text:', decrypted_text)  # (Note: 'x' is added as padding)
