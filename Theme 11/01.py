n = int(input())

numbers = [int(input()) for _ in range(n)]

target = int(input())

# Проверяем, можно ли выразить target как произведение двух разных чисел
for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] * numbers[j] == target:
            print("ДА")
            exit()

# Если не нашли такую пару, выводим "НЕТ"
print("НЕТ")