# Калькулятор времени

input_seconds = int(input('Введите количество секунд: '))

days = input_seconds // 86400
hours = (input_seconds % 86400) // 3600
minutes = (input_seconds % 86400) % 3600 // 60
seconds = (input_seconds % 86400) % 3600 % 60

print(f"Дней: {days}; часов: {hours}; минут: {minutes}; секунд: {seconds}")
