#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import  pprint
# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
name_shops = list(shops.keys())
sweets = {
    shops[name_shops[0]][0]['name']: [
        {'shop': name_shops[0], 'price': shops[name_shops[0]][0]['price']},
        {'shop': name_shops[1], 'price': shops[name_shops[1]][0]['price']},
        {'shop': name_shops[2], 'price': shops[name_shops[2]][0]['price']},
    ],
    shops[name_shops[0]][1]['name']: [
        {'shop': name_shops[0], 'price': shops[name_shops[0]][1]['price']},
        {'shop': name_shops[1], 'price': shops[name_shops[1]][1]['price']},
        {'shop': name_shops[2], 'price': shops[name_shops[2]][1]['price']},
    ],
    shops[name_shops[0]][2]['name']: [
        {'shop': name_shops[0], 'price': shops[name_shops[0]][2]['price']},
        {'shop': name_shops[1], 'price': shops[name_shops[1]][2]['price']},
        {'shop': name_shops[2], 'price': shops[name_shops[2]][2]['price']},
    ],
    shops[name_shops[0]][3]['name']: [
        {'shop': name_shops[0], 'price': shops[name_shops[0]][3]['price']},
        {'shop': name_shops[1], 'price': shops[name_shops[1]][3]['price']},
        {'shop': name_shops[2], 'price': shops[name_shops[2]][3]['price']},
    ],

}

pprint(sweets)

# Указать надо только по 2 магазина с минимальными ценами

