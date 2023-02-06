# flake8: noqa
# Игра в подсчитывание монет

ONE_ROUBLE = 100
LOWEST_COIN_DENOMINATION = 5
MIDDLE_COIN_DENOMINATION = 10
HIGHEST_COIN_DENOMINATION = 50
WELCOME_MSG = 'Введите количество монет достоинством {} копеек: '
WIN_MSG = 'Поздравляю с победой!'
OUTPUT_MSG = 'Стоимость введенного количества монет {} одного рубля'

low_coin_denom_amount = int(input(WELCOME_MSG.format(LOWEST_COIN_DENOMINATION)))
mid_coin_denom_amount = int(input(WELCOME_MSG.format(MIDDLE_COIN_DENOMINATION)))
high_coin_denom_amount = int(input(WELCOME_MSG.format(HIGHEST_COIN_DENOMINATION)))

total_cost = (
    low_coin_denom_amount * LOWEST_COIN_DENOMINATION
) + (
    mid_coin_denom_amount * MIDDLE_COIN_DENOMINATION
) + (
    high_coin_denom_amount * HIGHEST_COIN_DENOMINATION
)

if total_cost == ONE_ROUBLE:
    output_msg = WIN_MSG
elif total_cost < ONE_ROUBLE:
    matching_relation = 'менее'
    output_msg = OUTPUT_MSG.format(matching_relation)
else:
    matching_relation = 'более'
    output_msg = OUTPUT_MSG.format(matching_relation)

print(output_msg)
