# -*- coding: utf8 -*-

from random import uniform
from time import sleep


def sale(data_file, discount_file):
    '''Перемножаем списки "цена до" и "скидка",
    получаем список с "ценами после",
    формируем словарь {продукт: "цена после"}.

    '''
    print("Подождите, проставляются скидки...")
    sleep(1)
    products = list(data_file)
    prices = list(data_file.values())
    new_prices = [int(prices * (1.0 - discount_file)) for prices, discount_file in zip(prices, discount_file)]
    after_discounts = dict(zip(products, new_prices)) # Упаковка в итоговый словарь с помощью zip
    for new_price in new_prices:
        try:
            assert 0 <= new_price
        except AssertionError:
            print("Хотите доплатить за товар? Исправьте размер скидки, иначе цена будет такой:", new_price)
            print("Рекомендованная сгенерированная скидка:",
                  round(uniform(0.1, 0.7), 2), "(Замените значение в файле со скидками)\n")
        else:
            print("Все ок, такую цену можно залить:", new_price, "\n")

    print("А вот ваши цены со скидками", after_discounts)


'''Обрабатываем файл data в формате txt,
чтобы получить словарь с продуктом и его ценой.

'''
data = {}
with open('data.txt', encoding="utf-8") as datafile:
    for line in (line.replace(' ', '').strip() for line in datafile.readlines()):
        '''Преобразуем входные данные:
        
        replace(' ', '') заменяет лишние пробелы
        strip() удаляет переносы срок
        
        '''
        key, value = line.split(",")  # С помощью split(,) обозначаем разделитель в строке
        value = int(value)
        data[key] = value
print("Ваш исходный файл до скидок:", data)


'''Обрабатываем файл discount в формате txt,
чтобы получить список скидок.

Чтобы увидеть AssertionError,
используйте файл discount_bad.txt
'''
discounts = []
with open('discount.txt', encoding="utf-8") as file:
    for elem in (elem.strip() for elem in file.readlines()):
        elem = float(elem)
        discounts.append(elem)
print("Скидки из файла:", discounts, "\n")


sale(data, discounts)