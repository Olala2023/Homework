import random

# Визначення довжини списку
length = int(input("Введіть довжину списку: "))

# Генерування списку
my_list = []
for i in range(length):
    my_list.append(random.randint(0, 9))

# Виведення списку на екран
print("Згенерований список:", my_list)

# Знаходження кількості входжень заданого числа
target_num = int(input("Введіть число, яке потрібно знайти: "))
count = 0
for element in my_list:
    if element == target_num:
        count += 1

# Виведення результату на екран або повідомлення про відсутність числа в списку
if count == 0:
    print("Халепа, такого числа немає в списку")
else:
    print("Кількість входжень числа", target_num, "в списку:", count)