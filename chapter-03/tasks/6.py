# Магические даты

month = int(input('Придумайте дату. Введите месяц в виде числа: '))
day = int(input('Введите день в виде числа: '))
year = int(input('Введите год в виде двузначного числа: '))

if day * month == year:
    date_is_magic = True
else:
    date_is_magic = False

if date_is_magic:
    print('Выбранная дата магическая. Поздравляю!')
else:
    print('Выбранная дата не магическая. Фи.')
