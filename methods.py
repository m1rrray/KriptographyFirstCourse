import numpy as np

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_37 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ., ?'


class Xill():
    '''
    Класс, который шифрует и расшифровывает сообщение с помощью шифра Хилла
    '''

    def encode(self, message, key, alphabet):
        message = [alphabet.index(i) for i in message]
        size_matrix = key.shape[0]
        new_message = []

        for i in range(0, len(message), size_matrix):

            casual_size = []
            breed = []

            for j in range(size_matrix):
                casual_size += [message[i + j]]

            vector = np.array(casual_size) % len(alphabet)
            new_vector = ((vector @ key) % len(alphabet)).flatten().tolist()
            for j in range(size_matrix):
                breed += [alphabet[int(new_vector[j])]]

            new_message += breed

        return ''.join(new_message)

    def decode(self, message, key, alphabet):
        message = [alphabet.index(i) for i in message]
        size_matrix = key.shape[0]
        new_message = []
        key = find_inverse_key(key, alphabet)

        for i in range(0, len(message), size_matrix):

            casual_size = []
            breed = []

            for j in range(size_matrix):
                casual_size += [message[i + j]]

            vector = np.array(casual_size) % len(alphabet)
            new_vector = ((vector @ key) % len(alphabet)).flatten().tolist()
            for j in range(size_matrix):
                breed += [alphabet[int(new_vector[j])]]

            new_message += breed

        return ''.join(new_message)


class Rec_xill():
    @staticmethod
    def encode(message, key_1, key_2, alphabet):
        message = [alphabet.index(i) for i in message]
        size_matrix = key_1.shape[0]
        first_let = message[0:size_matrix] @ key_1
        second_let = message[size_matrix:2 * size_matrix] @ key_2

        new_message = (first_let % len(alphabet)).tolist()
        new_message += (second_let % len(alphabet)).tolist()

        for i in range(2 * size_matrix, len(message), size_matrix):
            new_key = key_2 @ key_1

            casual_size = []
            breed = []

            for j in range(size_matrix):
                casual_size += [message[i + j]]

            vector = np.array(casual_size) % len(alphabet)

            new_vector = ((np.dot(vector, new_key)) % len(alphabet)).flatten().tolist()

            for j in range(size_matrix):
                breed += [int(new_vector[j])]

            new_message += breed

            key_1 = key_2
            key_2 = new_key
        new_message = [alphabet[i] for i in new_message]
        return ''.join(new_message)

    @staticmethod
    def decode(message, key_1, key_2, alphabet):
        message = [alphabet.index(i) for i in message]

        size_matrix = key_1.shape[0]
        key_1_inv = find_inverse_key(key_1, alphabet)
        key_2_inv = find_inverse_key(key_2, alphabet)
        first_let = message[0:size_matrix] @ key_1_inv
        second_let = message[size_matrix:2 * size_matrix] @ key_2_inv
        new_message = (first_let % len(alphabet)).tolist()
        new_message += (second_let % len(alphabet)).tolist()

        for i in range(2 * size_matrix, len(message), size_matrix):
            new_key = key_1_inv @ key_2_inv

            casual_size = []
            breed = []

            for j in range(size_matrix):
                casual_size += [message[i + j]]

            vector = np.array(casual_size) % len(alphabet)

            new_vector = ((np.dot(vector, new_key)) % len(alphabet)).flatten().tolist()
            for j in range(size_matrix):
                breed += [int(new_vector[j])]

            new_message += breed

            key_1_inv = key_2_inv
            key_2_inv = new_key

        new_message = [alphabet[i] for i in new_message]
        return ''.join(new_message)


def find_inverse_key(K, alphabet):
    det = int(round(np.linalg.det(K))) % len(alphabet)

    if det == 0:
        raise ValueError("Матрица не имеет обратной по модулю len(alphabet).")

    A = np.zeros_like(K)
    for i in range(K.shape[0]):
        for j in range(K.shape[1]):
            A[i, j] = ((-1) ** (i + j)) * int(
                round(np.linalg.det(np.delete(np.delete(K, i, axis=0), j, axis=1)) % len(alphabet)))

    det_inv = pow(det, -1, len(alphabet))

    K_inv = (A.T * det_inv) % len(alphabet)

    return K_inv

