# Общий объём продаж

VAT = 0.07  # Налог на добавленную стоимость
NUMBER_OF_GOODS = 5  # Количество купленных товаров

commodity_price = float(input('Введите стоимость товара без учета налогов: '))

cost_of_goods = commodity_price * NUMBER_OF_GOODS
cost_of_taxes = commodity_price * VAT * NUMBER_OF_GOODS
total_cost = cost_of_goods + cost_of_taxes

print(
    f"Стоимость приобретаемых товаров равна {cost_of_goods:.2f}",
    f"Сумма налога с продаж составляет {cost_of_taxes:.2f}",
    f"Итоговая сумма покупки - {total_cost:.2f}",
    sep='\n'
)
