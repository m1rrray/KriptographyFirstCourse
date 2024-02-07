import numpy as np
from methods import Xill, Rec_xill

alphabet_cl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_37 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ., ?'

what_to_do = int(input('Что вы хотите сделать?\n1 - зашифровать \n2 - расшифровать\n'))

alphabet = input(
    'Выберите алфавит:\n1 - латиница с заглавными\n2 - русский алфавит заглавные \n3 - русский плюс знаки\n')

if alphabet == '1':
    print(f'Вы выбрали этот алфавит:{alphabet}')
    alphabet = alphabet_cl
elif alphabet == '2':
    print(f'Вы выбрали этот алфавит:{alphabet_ru}')
    alphabet = alphabet_ru
elif alphabet == '3':
    print(f'Вы выбрали этот алфавит:{alphabet_37}')
    alphabet = alphabet_37
shifr = input('Выберите шифр\n1 - Шифр Хилла\n2 - Рекуррентный шифр Хилла\n')

mess = input('Введите сообщение\n')

size_of_matrix = int(input('Введи размерность матрицы\n'))

if shifr == '1':
    print('Введи ключ матрицу')
    matrix = []
    for i in range(size_of_matrix):
        string = list(map(int, input().split()))
        matrix += [string]

    matrix = np.array(matrix)

    if what_to_do == 1:
        print('Ваш зашифрованный текст:')
        print(Xill.encode(mess, matrix, alphabet))
    elif what_to_do == 2:
        print('Ваш расшифрованный текст:')
        print(Xill.decode(mess, matrix, alphabet))
    else:
        raise ValueError('1 или 2 плиз')



elif shifr == '2':
    print('Введи перую ключ матрицу')
    string_1 = list(map(int, input().split()))
    string_2 = list(map(int, input().split()))
    string_3 = list(map(int, input().split()))

    matrix_1 = np.array([string_1, string_2, string_3])

    print('Введи вторую ключ матрицу')
    string_4 = list(map(int, input().split()))
    string_5 = list(map(int, input().split()))
    string_6 = list(map(int, input().split()))

    matrix_2 = np.array([string_4, string_5, string_6])

    if what_to_do == 1:
        print('Ваш зашифрованный текст:')
        print(Rec_xill.encode(mess, matrix_1, matrix_2, alphabet))
    elif what_to_do == 2:
        print('Ваш расшифрованный текст:')
        print(Rec_xill.decode(mess, matrix_1, matrix_2, alphabet))
    else:
        raise ValueError('1 или 2 плиз')
