# Программа расчета купли-продажи акций.

BROKER_COMISSION = 0.03

SHARES_PURCHASED = 2000
BUYING_PRICE = 40

SHARES_SOLD = 2000
SELLING_PRICE = 42.75

buying_sum = SHARES_PURCHASED * BUYING_PRICE
buying_comission = BROKER_COMISSION * buying_sum

selling_sum = SHARES_SOLD * SELLING_PRICE
selling_comission = BROKER_COMISSION * selling_sum

profit = (selling_sum - selling_comission) - (buying_sum + buying_comission)
total = selling_sum - selling_comission - buying_comission

print(f"Сумма денег, уплаченная при покупке акций: {buying_sum}")
print(f"Комиссия брокеру, уплаченная при покупке акций: {buying_comission}")
print(f"Сумма денег, полученная при продаже акций: {selling_sum}")
print(f"Комиссия брокеру, уплаченная при продаже акций: {selling_comission}")
print(f"Сумма денег, оставшаяся после продажи акций и выплаты всех комиссий: {total}")
print(f"Прибыль, полученная после продажи акций и выплаты всех комиссий: {profit}")
