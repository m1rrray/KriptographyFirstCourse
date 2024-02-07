from methods import Vizhener, VizhenerOpen, VizhenerClose

alpabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alpabet_special = 'ABCDEFGHIJKLMNOPQRSTUVWabcdefghijklmnopqrstuvwxyz'
alpabet_russian = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

what_to_do = input('Что вы хотите сделать?\n1 - зашифровать \n2 - расшифровать\n')

alphabet = input('Выберите алфавит:\n1 - латиница с заглавными\n2 - латиница с маленькими буквами \n3 - латиница всех регистров\n4 - русский заглавный\n')

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
    print(f'Вы выбрали этот алфавит:{alpabet_russian}')
    alphabet = alpabet_russian
else:
    raise ValueError('Invalid alphabet')

shifr = input('Выберите шифр\n1 - Шифр Вижерена\n2 - Самоключ Виженера по открытому тексту\n3 - Самоключ Виженера по закрытому тексту\n')

mess = input('Введите сообщение\n')

key = input('Введите ключ\n')
if len(key) != 1 and shifr != '1':
    raise ValueError('Invalid key')

if what_to_do == '1':
    if shifr == '1':
        print(Vizhener.encode_decode(mess, key, 1))
    elif shifr == '2':
        print(VizhenerOpen.encode(mess, key))
    elif shifr == '3':
        print(VizhenerClose.encode(mess, key))
    else:
        raise ValueError('Unknown shifr')
elif what_to_do == '2':
    if shifr == '1':
        print(Vizhener.encode_decode(mess, key, -1, alphabet))
    elif shifr == '2':
        print(VizhenerOpen.decode(mess, key, alphabet))
    elif shifr == '3':
        print(VizhenerClose.decode(mess, key, alphabet))
    else:
        raise ValueError('Unknown shifr')
else:
    raise ValueError('Wrong operation')











