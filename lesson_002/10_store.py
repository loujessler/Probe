#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

names = list(goods.keys())

lamps_quantity = store[goods[names[0]]][0]['quantity']
lamps_price = store[goods[names[0]]][0]['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

tables_quantity = store[goods[names[1]]][0]['quantity']
tables_price = store[goods[names[1]]][0]['price']
tables_quantity_2 = store[goods[names[1]]][1]['quantity']
tables_price_2 = store[goods[names[1]]][1]['price']
tables_cost = tables_quantity * tables_price + tables_quantity_2 * tables_price_2
print('Стол -', tables_quantity + tables_quantity_2, 'шт, стоимость', tables_cost, 'руб')

sofas_quantity = store[goods[names[2]]][0]['quantity']
sofas_price = store[goods[names[2]]][0]['price']
sofas_quantity_2 = store[goods[names[2]]][1]['quantity']
sofas_price_2 = store[goods[names[2]]][1]['price']
sofas_cost = sofas_quantity * sofas_price + sofas_quantity_2 * sofas_price_2
print('Диван -', sofas_quantity + sofas_quantity_2, 'шт, стоимость', sofas_cost, 'руб')

chairs_quantity = store[goods[names[3]]][0]['quantity']
chairs_price = store[goods[names[3]]][0]['price']
chairs_quantity_2 = store[goods[names[3]]][1]['quantity']
chairs_price_2 = store[goods[names[3]]][1]['price']
chairs_quantity_3 = store[goods[names[3]]][2]['quantity']
chairs_price_3 = store[goods[names[3]]][2]['price']
chairs_cost = chairs_quantity * chairs_price + chairs_quantity_2 * chairs_price_2 + chairs_quantity_3 * chairs_price_3
print('Стул -', chairs_quantity + chairs_quantity_2 + chairs_quantity_3, 'шт, стоимость', chairs_cost, 'руб')



# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.








