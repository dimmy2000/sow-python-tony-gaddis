# flake8: noqa
# Очки книжного клуба

total_books = int(input('Введите количество купленных за месяц книг: '))

if total_books < 2:
    total_points = 0
else:
    # При покупке 8 книг начисляется 60 очков
    points_60 = total_books // 8
    books_remained = total_books % 8
    # При покупке 6 книг начисляется 30 очков
    points_30 = books_remained // 6
    books_remained = books_remained % 6
    # При покупке 4 книг начисляется 15 очков
    points_15 = books_remained // 4
    books_remained = books_remained % 4
    # При покупке 2 книг начисляется 5 очков
    points_5 = books_remained // 2
    books_remained = books_remained % 2

    total_points = points_60 * 60 + points_30 * 30 + points_15 * 15 + points_5 * 5

print(f'В этом месяце вы получите {total_points} бонусных очков.')
