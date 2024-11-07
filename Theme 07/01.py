first_list = []
while True:
    try:
        num = input().strip()
        if num == "":  # Пустая строка — разделитель
            break
        first_list.append(num)
    except EOFError:
        break

second_list = []
while True:
    try:
        num = input().strip()
        if num == "":  # Пустая строка — конец ввода
            break
        second_list.append(num)
    except EOFError:
        break

# Находим пересечение двух списков
intersection = set(first_list) & set(second_list)

# Если пересечение не пустое, выводим его
if intersection:
    for num in intersection:
        print(num)
else:
    print("EMPTY")