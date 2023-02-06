# Калькулятор сосисок для пикника

SAUSAGES_PER_PKG = 10
BUNS_PER_PKG = 8

eaters = int(input("Введите количество участников пикника: "))
hot_dogs = int(input("Сколько хот-догов будет предложено каждому участнику? "))

hotdogs_total = hot_dogs * eaters

sausage_pkgs_needed = hotdogs_total // SAUSAGES_PER_PKG
leftover_sausages = hotdogs_total % SAUSAGES_PER_PKG
buns_pkgs_needed = hotdogs_total // BUNS_PER_PKG
leftover_buns = hotdogs_total % BUNS_PER_PKG

if leftover_sausages == 0:
    leftover_sausages_in_pkg = 0
else:
    leftover_sausages_in_pkg = SAUSAGES_PER_PKG - leftover_sausages
    sausage_pkgs_needed = sausage_pkgs_needed + 1

if leftover_buns == 0:
    leftover_buns_in_pkg = 0
else:
    leftover_buns_in_pkg = BUNS_PER_PKG - leftover_buns
    buns_pkgs_needed = buns_pkgs_needed + 1

print(f'Понадобится минимум упаковок сосисок - {sausage_pkgs_needed}.')
print(f'Понадобится минимум упаковок булочек - {buns_pkgs_needed}.')
print(f'После пикника останется сосисок - {leftover_sausages_in_pkg}.')
print(f'После пикника останется булочек - {leftover_buns_in_pkg}.')
