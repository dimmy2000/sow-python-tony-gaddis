# flake8: noqa
# Реализация программного обеспечения

PRICE = 99

copies_buyed = int(input('Введите количество купленных копий ПО: '))

# Рассчитать скидку в процентах
if copies_buyed >= 10 and copies_buyed <= 19:
    discount = 10
elif copies_buyed >= 20 and copies_buyed <= 49:
    discount = 20
elif copies_buyed >= 50 and copies_buyed <= 99:
    discount = 30
elif copies_buyed >= 100:
    discount = 40
else:
    discount = 0

# Рассчитать стоимость с учетом скидки
total_discount = 0.01 * (100 - discount)
full_price = copies_buyed * PRICE
total_price = total_discount * full_price
profit = full_price - total_price

output_msg = (
    'Стоимость заказа с учетом скидки '
    f'{discount}% составит {total_price:.2f} денег.'
)

if discount > 0:
    output_msg = output_msg + f' Ваша выгода составит {profit:.2f} денег.'

print(output_msg)
