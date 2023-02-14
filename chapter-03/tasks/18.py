# Селектор ресторанов

MSG = 'Будет ли на ужине '

vegetarian = False
vegan = False
gluten_free = False

is_vegetarian = input(MSG + 'вегетарианец? ')
is_vegan = input(MSG + 'веган? ')
is_gluten_free = input(MSG + 'приверженец безглютеновой диеты? ')

if is_vegetarian == 'да':
    vegetarian = True
if is_vegan == 'да':
    vegan = True
if is_gluten_free == 'да':
    gluten_free = True

print('Вот ваши варианты ресторанов')

if not vegetarian and not vegan and not gluten_free:
    print('Изысканные гамбургеры от Джо')
if not vegan:
    print('Центральная пиццерия')
if not vegan and not gluten_free:
    print('Блюда от итальянской мамы')
print('Кухня шеф-повара')
print('Кафе за углом')
