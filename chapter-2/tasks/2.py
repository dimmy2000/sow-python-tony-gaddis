# Прогноз продаж.

ANNUAL_PROFIT = 0.23

total_sales = float(input('Введите плановую сумму общего объема продаж: '))

profit = total_sales * ANNUAL_PROFIT

print(f"Прибыль, полученная с продаж за год, составит {profit:.2f} деняк.")
