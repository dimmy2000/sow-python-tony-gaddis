# Регулятор ингредиентов

BUNS = 48
SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75

required_num_of_buns = int(input(
    'Введите количество булочек, которое хотите приготовить: ',
))

print(
    f"Для выпечки булочек в количестве {required_num_of_buns} шт. требуется:",
    f"Сахара - {(SUGAR / BUNS * required_num_of_buns):.2f} ст.",
    f"Масла - {(BUTTER / BUNS * required_num_of_buns):.2f} ст.",
    f"Муки - {(FLOUR / BUNS * required_num_of_buns):.2f} ст.",
    sep='\n',
)
