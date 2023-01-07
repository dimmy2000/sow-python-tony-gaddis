# Налог с продаж

FED_TAX = 0.05  # федеральный налог на продажи
REG_TAX = 0.025  # региональный налог на продажи

total_cost = float(input('Введите стоимость покупки: '))

fed_tax_cost = total_cost * FED_TAX
reg_tax_cost = total_cost * REG_TAX
tax_cost = fed_tax_cost + reg_tax_cost
purchase_cost = total_cost - tax_cost

print(
    f"Сумма покупки составляет {purchase_cost:.2f} денег.",
    f"Федеральный налог с продаж составляет {fed_tax_cost:.2f} денег.",
    f"Региональный налог с продаж составляет {reg_tax_cost:.2f} денег.",
    f"Общий налог с продаж составляет {tax_cost:.2f} денег.",
    f"Общая сумма продажи составляет {total_cost:.2f} денег.",
    sep='\n'
)
