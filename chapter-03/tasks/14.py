# Индекс массы тела

OUTPUT_MSG = 'Ваша масса является {} для вашего роста.'

body_weight = float(input('Введите свою массу в килограммах: '))
body_height = float(input('Введите свой рост в метрах: '))

bmi = body_weight / body_height ** 2

if bmi < 18.5:
    rating = 'недостаточной'
elif bmi > 25:
    rating = 'избыточной'
else:
    rating = 'оптимальной'

print(f'Ваш индекс массы тела - {bmi:.2f}.', OUTPUT_MSG.format(rating))
