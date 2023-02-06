# Цвета колеса рулетки

roulette_pocket = int(input('Введите сектор рулетки: '))

if roulette_pocket < 0 or roulette_pocket > 36:
    print(
        'Ошибка. '
        'На колесе рулетки секторы пронумерованы от 0 до 36. '
        'Попробуйте еще раз.'
    )
else:
    if roulette_pocket == 0:
        print(f'Сектор {roulette_pocket} - зеленый.')
    elif roulette_pocket >= 1 and roulette_pocket <= 10:
        if roulette_pocket % 2 == 0:
            print(f'Сектор {roulette_pocket} - черный.')
        else:
            print(f'Сектор {roulette_pocket} - красный.')
    elif roulette_pocket >= 11 and roulette_pocket <= 18:
        if roulette_pocket % 2 == 0:
            print(f'Сектор {roulette_pocket} - красный.')
        else:
            print(f'Сектор {roulette_pocket} - черный.')
    elif roulette_pocket >= 19 and roulette_pocket <= 28:
        if roulette_pocket % 2 == 0:
            print(f'Сектор {roulette_pocket} - черный.')
        else:
            print(f'Сектор {roulette_pocket} - красный.')
    elif roulette_pocket >= 29 and roulette_pocket <= 36:
        if roulette_pocket % 2 == 0:
            print(f'Сектор {roulette_pocket} - красный.')
        else:
            print(f'Сектор {roulette_pocket} - черный.')
