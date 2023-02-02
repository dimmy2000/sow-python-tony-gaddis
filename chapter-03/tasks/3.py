# Классификатор возраста

age = float(input("Введите возраст человека: "))

if age <= 1:
    print('Младенец')
elif age < 13:
    print('Ребёнок')
elif age < 20:
    print('Подросток')
else:
    print('Взрослый')
