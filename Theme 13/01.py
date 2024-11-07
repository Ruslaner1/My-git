n = int(input())

for i in range(1, n + 1):
    line = input().strip()

    # Ищем первое вхождение "кот"
    index = line.find('кот')

    if index != -1:  # Если вхождение найдено
        # Печатаем номер строки и позицию вхождения с единицы
        print(i, index + 1)