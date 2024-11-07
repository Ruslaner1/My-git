input_string = input()

# Разбиваем строку на слова
words = input_string.split()

# Выбираем каждое третье слово (индексы 2, 5, 8 и так далее)
result = ' '.join(words[i] for i in range(2, len(words), 3))

# Выводим результат
print(result)