# Считываем количество покупок
n = int(input())

# Считываем все покупки в список
purchases = [input() for _ in range(n)]

# Выводим каждую покупку по очереди
for purchase in purchases:
    print(purchase)