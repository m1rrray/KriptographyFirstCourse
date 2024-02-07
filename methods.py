alphabetEn = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Vizhener:
    def encode_decode(message: str, key: str, indicator: int, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        message = [alphabet.index(i) for i in message]
        key = [alphabet.index(i) for i in key]
        repeats = len(message) // len(key) + 1
        key *= repeats
        new_message = []
        for x, y in zip(message, key):
            new_message += [(x + y * indicator) % len(alphabet)]
        new_message = [alphabet[i] for i in new_message]
        return ''.join(new_message)


class VizhenerOpen:
    @staticmethod
    def encode(message: str, key: str, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        message = [alphabet.index(i) for i in message]
        key = [alphabet.index(i) for i in key]
        key += message[0:-len(key)]
        new_message = []
        for x, y in zip(message, key):
            new_message += [(x + y) % len(alphabet)]
        new_message = [alphabet[i] for i in new_message]

        return ''.join(new_message)

    @staticmethod
    def decode(message: str, key: str, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        message = [alphabet.index(i) for i in message]
        key = [alphabet.index(i) for i in key]
        new_message = [(message[0] - key[0]) % len(alphabet)]

        for i in range(1, len(message)):
            new_message += [(message[i] - new_message[-1]) % len(alphabet)]
        new_message = [alphabet[i] for i in new_message]
        return ''.join(new_message)


class VizhenerClose:
    @staticmethod
    def encode(message: str, key: str, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        message = [alphabet.index(i) for i in message]
        key = [alphabet.index(i) for i in key]
        new_message = [(key[0] + message[0]) % len(alphabet)]

        for i in range(1, len(message)):
            new_message += [(message[i] + new_message[-1]) % len(alphabet)]
        new_message = [alphabet[i] for i in new_message]
        return ''.join(new_message)

    @staticmethod
    def decode(message: str, key: str, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        message = [alphabet.index(i) for i in message]
        print(message)
        key = [alphabet.index(i) for i in key]
        print(key)
        gamma = [key[0]] + message[:-1]
        print(gamma)

        new_message = []
        for x, y in zip(message, gamma):
            new_message += [(x - y) % len(alphabet)]
        print(new_message)
        new_message = [alphabet[i] for i in new_message]
        return ''.join(new_message)


def vigenere_cipher(message, key):
    # Преобразуем сообщение и ключ в верхний регистр
    message = message.upper()
    key = key.upper()

    # Создаем список для хранения зашифрованного сообщения
    encrypted_message = []

    # Проходим по каждой букве в сообщении
    for i in range(len(message)):
        # Получаем текущую букву сообщения и ключа
        message_char = message[i]
        key_char = key[i % len(key)]

        # Вычисляем номера букв в алфавите
        message_num = ord(message_char) - ord('A')
        key_num = ord(key_char) - ord('A')

        # Вычисляем номер зашифрованной буквы
        encrypted_num = (message_num + key_num) % 26

        # Преобразуем номер зашифрованной буквы в символ и добавляем его в список
        encrypted_char = chr(encrypted_num + ord('A'))
        encrypted_message.append(encrypted_char)

    # Возвращаем зашифрованное сообщение в виде строки
    return ''.join(encrypted_message)

mes = 'WHOISVIZHENER'
key = 'KEY'
