import numpy as np
import string
from egcd import egcd

alphabet = string.ascii_lowercase
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


# def matrix_mod_inverse(matrix, modulus):
#     det = int(np.linalg.det(matrix))
#     det_inv = egcd(det, modulus)[1] % modulus
#     matrix_modulus_inv = (
#             det_inv * np.round(det * np.linalg.inv(matrix).astype(int)) % modulus
#     )
#     return matrix_modulus_inv

def matrix_mod_inv(matrix, modulus):
    det = int(np.linalg.det(matrix))
    det_inv = egcd(matrix, modulus)[1] % modulus
    matrix_modulus_inv = (
            det_inv * np.round(np.linalg.inv(matrix).astype(int)) % modulus
    )
    return matrix_modulus_inv


def encrypt(message, K):
    encrypted_message = ""
    message_in_number = []
    for char in message:
        message_in_number.append(letter_to_index[char])
    split_p = [
        message_in_number[i:i + int(K.shape[0])]
        for i in range(0, len(message_in_number), int(K.shape[0]))
    ]
