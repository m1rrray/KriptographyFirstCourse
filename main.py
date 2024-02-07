from methods import Simple_replacement, Affine, Affine_rec

alpabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alpabet_special = 'ABCDEFGHIJKLMNOPQRSTUVWabcdefghijklmnopqrstuvwxyz'

what_to_do = input('Что вы хотите сделать?\n1 - зашифровать \n2 - расшифровать\n')

alphabet = input(
    'Выберите алфавит:\n1 - латиница с заглавными\n2 - латиница с маленкьими \n3 - латиница всех регистров\n4 - введу свой\n')

if alphabet == '1':
    print(f'Вы выбрали этот алфавит:{alpabet_upper}')
    alphabet = alpabet_upper
elif alphabet == '2':
    print(f'Вы выбрали этот алфавит:{alpabet_lower}')
    alphabet = alpabet_lower
elif alphabet == '3':
    print(f'Вы выбрали этот алфавит:{alpabet_special}')
    alphabet = alpabet_special
elif alphabet == '4':
    alphabet = input('Введите алфавит:')
    print(f'Вы выбрали этот алфавит:{alphabet}')

shifr = input('Выберите шифр\n1 - шифро простой замены\n2 - аффинный шифр\n3 - аффинный рекуррентный\n')

mess = input('Введите сообщение\n').split(' ')

if shifr == '1':
    key = input('Введите ключ\n')
elif shifr == '2':
    key_1 = int(input('Введите первый ключ:\n'))
    key_2 = int(input('Введите второй ключ:\n'))
elif shifr == '3':
    key_1 = int(input('Введите первый ключ:\n'))
    key_2 = int(input('Введите второй ключ:\n'))
    key_3 = int(input('Введите третий ключ:\n'))
    key_4 = int(input('Введите четвертый ключ:\n'))

res = []

if what_to_do == '1':
    for i in range(len(mess)):
        if shifr == '1':
            res += [Simple_replacement.encode(alphabet, mess[i], key)]
        elif shifr == '2':
            res += [Affine.encode(alphabet, mess[i], key_1, key_2)]
        elif shifr == '3':
            res += [Affine_rec.encode(alphabet, mess[i], key_1, key_2, key_3, key_4)]
elif what_to_do == '2':
    for i in range(len(mess)):
        if shifr == '1':
            res += [Simple_replacement.decode(alphabet, mess[i], key)]
        elif shifr == '2':
            res += [Affine.decode(alphabet, mess[i], key_1, key_2)]
        elif shifr == '3':
            res += [Affine_rec.decode(alphabet, mess[i], key_1, key_2, key_3, key_4)]

print(*res)
