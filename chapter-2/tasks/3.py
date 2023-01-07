# Расчет площади земельного участка.

METERS_IN_ACRE = 4046.86

meters = float(input('Введите площадь участка земли в квадратных метрах: '))

acres = meters / METERS_IN_ACRE

print(f"Площадь участка земли в акрах: {acres:.2f}")
