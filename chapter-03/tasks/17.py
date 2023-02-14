# flake8: noqa
# Диагностическое дерево проверки качества Wi-Fi

QUESTION = 'Вы исправили проблему? '

print('Перезагрузите компьютер и попробуйте подключиться')
answer = input(QUESTION)

if answer == 'нет':
    print('Перезагрузите маршрутизатор и попробуйте подключиться')
    answer = input(QUESTION)

    if answer == 'нет':
        print('Убедитесь, что кабели между маршрутизатором и модемом прочно подсоединены')
        answer = input(QUESTION)

        if answer == 'нет':
            print('Переместите маршрутизатор на новое место')
            answer = input(QUESTION)

            if answer == 'нет':
                print('Возьмите новый маршрутизатор')
