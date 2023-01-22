# Эта программа определяет, удовлетворяет ли
# клиент требованиям банка на получение ссуды.

MIN_SALARY = 30000.0  # Минимально допустимый годовой доход
MIN_YEARS = 2        # Минимально допустимый стаж на текущем месте работы

# Получить размер годового дохода клиента.
salary = float(input('Введите свой годовой доход: '))

# Получить количество лет на текущем месте работы.
years_on_job = int(input('Введите количество лет' +
                         'рабочего стажа: '))

# Определить, удовлетворяет ли клиент требованиям.
if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
    print('Ваша ссуда одобрена.')
else:
    print('Ваша ссуда не одобрена.')
