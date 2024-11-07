# Чтение входных данных
words = []
while True:
    word = input().strip()
    if word == "стоп":
        break
    words.append(word)

# Нахождение самого короткого и самого длинного слова
shortest_word = min(words, key=len)
longest_word = max(words, key=len)

# Преобразуем слова в множества символов
shortest_set = set(shortest_word)
longest_set = set(longest_word)

# Проверяем, содержатся ли все символы из короткого слова в длинном
if shortest_set.issubset(longest_set):
    print("ДА")
else:
    print("НЕТ")