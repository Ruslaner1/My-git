word = input().strip()

# Проверяем, что длина слова больше или равна 5
if len(word) >= 5:
    # Выводим пятую букву (индекс 4)
    print(word[4])
else:
    # Если слова слишком короткое, выводим "НЕТ"
    print("НЕТ")