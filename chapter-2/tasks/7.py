# Расход бензина в расчете на километры пройденного пути.

distance = float(input('Введите пройденное расстояние в километрах: '))

gasoline_consumption = float(input('Введите расход бензина в литрах на километр: '))

total_consumption = distance * gasoline_consumption

print(f"Расход бензина автомобилем составляет {total_consumption:.2f} л.")
