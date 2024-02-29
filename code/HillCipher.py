import string
import numpy as np

alphabet = string.ascii_lowercase
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x


def mod_inv(det, modulus):
    gcd, x, y = egcd(det, modulus)
    if gcd != 1:
        raise Exception("Matrix is not invertible.")
    return (x % modulus + modulus) % modulus


def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mod_inv(det, modulus)
    matrix_modulus_inv = (
            det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )
    return matrix_modulus_inv.astype(int)


def encrypt_decrypt(message, K):
    msg = ""
    message_in_numbers = [letter_to_index[letter] for letter in message]
    split_P = [
        message_in_numbers[i: i + len(K)]
        for i in range(0, len(message_in_numbers), len(K))
    ]
    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]
        while P.shape[0] != len(K):
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]
        numbers = np.dot(K, P) % len(alphabet)
        n = numbers.shape[0]
        for idx in range(n):
            number = int(numbers[idx, 0])
            msg += index_to_letter[number]
    return msg


message = "help"
K = np.matrix([[3, 3], [2, 5]])
Kinv = matrix_mod_inv(K, len(alphabet))

encrypted_message = encrypt_decrypt(message, K)
decrypted_message = encrypt_decrypt(encrypted_message, Kinv)

print("Original message: " + message.upper())
print("Encrypted message: " + encrypted_message.upper())
print("Decrypted message: " + decrypted_message.upper())