nobel_laureates = {
    "Боб Дилан": 2016,
    "Эрнест Хемингуэй": 1954,
    "Марио Варгас Льоса": 2010,
    "Владимир Набоков": 1974,
    "Габриэль Гарсия Маркес": 1982,
    "Альбер Камю": 1957,
    "Франсуа Моряк": 1966,
}

def get_nobel_year(laureate_name):
    # Проверяем, если имя есть в словаре, возвращаем год
    if laureate_name in nobel_laureates:
        return nobel_laureates[laureate_name]
    else:
        return "Лауреат не найден"

laureate_name = input().strip()

print(get_nobel_year(laureate_name))