# Дни в феврале

input_year = int(input('Введите год: '))

if input_year % 100 == 0 and input_year % 400 == 0:
    days = 29
elif input_year % 100 != 0 and input_year % 4 == 0:
    days = 29
else:
    days = 28

print(f"В {input_year} году в феврале {days} дней.")
