# flake8: noqa
# Цветовой микшер

print('Введите названия двух основных цветов для смешивания')

color_1 = input('Введите первый цвет с маленькой буквы: ')
color_2 = input('Введите второй цвет с маленькой буквы: ')

if (
    color_1 == 'желтый' or color_1 == 'красный' or color_1 == 'синий'
) and (
    color_2 == 'желтый' or color_2 == 'красный' or color_2 == 'синий'
):
    if color_1 == 'желтый' and color_2 == 'желтый':
        print('Получился желтый цвет')
    elif color_1 == 'красный' and color_2 == 'красный':
        print('Получился красный цвет')
    elif color_1 == 'синий' and color_2 == 'синий':
        print('Получился синий цвет')
    elif color_1 == 'желтый' and color_2 == 'красный' or color_1 == 'красный' and color_2 == 'желтый':
        print('Получился оранжевый цвет')
    elif color_1 == 'желтый' and color_2 == 'синий' or color_1 == 'синий' and color_2 == 'желтый':
        print('Получился зеленый цвет')
    elif color_1 == 'красный' and color_2 == 'синий' or color_1 == 'синий' and color_2 == 'красный':
        print('Получился фиолетовый цвет')
else:
    print('Ошибка. Основными цветами являются желтый, красный и синий.')