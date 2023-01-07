# Чаевые, налог и общая сумма

VAT = 0.07
TIPS = 0.18

dish_cost = float(input('Введите стоимость еды: '))

tax_cost = dish_cost * VAT
tips_cost = dish_cost * TIPS
total_cost = dish_cost + tax_cost + tips_cost

print(
    f"Стоимость еды составляет {dish_cost:.2f} денег.",
    f"Сумма НДС составляет {tax_cost:.2f} денег.",
    f"Сумма чаевых составляет {tips_cost:.2f} денег.",
    f"Общая стоимость акта гедонизма составляет {total_cost:.2f} денег.",
    sep='\n')
