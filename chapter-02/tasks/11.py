# Процент учащихся обоего пола.

boys = int(input('Введите количество учащихся мужского пола: '))
girls = int(input('Введите количество учащихся женского пола: '))

total = boys + girls

boys_percent = 100 * boys / total
girls_percent = 100 * girls / total

print(
    f"Процент учащихся юношей: {boys_percent:.2f}%",
    f"Процент учащихся девушек: {girls_percent:.2f}%",
    sep='\n'
)
