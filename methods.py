alpabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alpabet_special = 'ABCDEFGHIJKLMNOPQRSTUVWabcdefghijklmnopqrstuvwxyz'


class Simple_replacement():

    def encode(self, alpabet, message, key):
        d = dict()
        for x, y in zip(alpabet, key):
            d[x] = y
        newmessage = ''
        for i in message:
            newmessage += d.get(i)

        return newmessage

    def decode(self, alpabet, message, key):
        d = dict()
        p = dict()
        newmessage = ''

        for x, y in zip(alpabet, key):
            d[x] = y
        for x, y in zip(d.values(), d.keys()):
            p[x] = y
        for i in message:
            newmessage += p.get(i)

        return newmessage


class Affine():

    def encode(self, alpabet, message, key_1, key_2):
        newmessage = []
        message = [alpabet.index(i) for i in message]
        for i in message:
            newmessage += [(key_1 * i + key_2) % len(alpabet)]

        newmessage = [alpabet[i] for i in newmessage]

        return ''.join(newmessage)

    def decode(self, alpabet, message, key_1, key_2):
        message = [alpabet.index(i) for i in message]

        numbers = [(len(alpabet) * i + 1) for i in range(1, len(alpabet) * 10)]
        inverskey = inverse(key_1, len(alpabet))

        newmessage = []
        for i in message:
            newmessage += [((i - key_2) * inverskey) % len(alpabet)]

        newmessage = [alpabet[i] for i in newmessage]

        return ''.join(newmessage)


class Affine_rec():

    def encode(self, alpabet, message, key_1, key_2, key_3, key_4):
        message = [alpabet.index(i) for i in message]
        newmessage = [(key_1 * message[0] + key_2) % len(alpabet), (key_3 * message[1] + key_4) % len(alpabet)]

        for i in range(2, len(message)):
            new_key_1 = (key_1 * key_3) % len(alpabet)
            new_key_2 = (key_2 + key_4) % len(alpabet)

            newmessage += [(new_key_1 * message[i] + new_key_2) % len(alpabet)]
            key_1 = key_3
            key_2 = key_4
            key_3 = new_key_1
            key_4 = new_key_2

        newmessage = [alpabet[i] for i in newmessage]
        return ''.join(newmessage)

    def decode(self, alpabet, message, key_1, key_2, key_3, key_4):

        message = [alpabet.index(i) for i in message]

        key_1 = inverse(key_1, len(alpabet))
        key_3 = inverse(key_3, len(alpabet))

        if key_1 == -1 or key_3 == -1:
            return 'Введите другие ключи'

        newmessage = [((message[0] - key_2) * key_1) % len(alpabet), ((message[1] - key_4) * key_3) % len(alpabet)]

        for i in range(2, len(message)):
            new_key_1 = (key_1 * key_3) % len(alpabet)
            new_key_2 = (key_2 + key_4) % len(alpabet)

            newmessage += [((message[i] - new_key_2) * new_key_1) % len(alpabet)]

            key_1 = key_3
            key_2 = key_4
            key_3 = new_key_1
            key_4 = new_key_2

        newmessage = [alpabet[i] for i in newmessage]
        return ''.join(newmessage)


def inverse(a, b):
    for i in range(b):
        if a * i % b == 1:
            return i
    else:
        return -1
