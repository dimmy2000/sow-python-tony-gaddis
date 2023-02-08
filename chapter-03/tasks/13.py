# Стоимость доставки

WEIGHT_RATE = 100

cargo_weight = float(input('Введите массу пакета в граммах: '))

if cargo_weight <= 200:
    shipping_rate = 150
elif cargo_weight > 200 and cargo_weight <= 600:
    shipping_rate = 300
elif cargo_weight > 600 and cargo_weight <= 1000:
    shipping_rate = 400
else:
    shipping_rate = 475

shipping_cost = cargo_weight / WEIGHT_RATE * shipping_rate

print(f'Стоимость доставки составит: {shipping_cost:.2f} денег')
