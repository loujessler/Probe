#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

films = dict()
films['первый фильм'] = my_favorite_movies[:my_favorite_movies.find(',')]
films['последний'] = my_favorite_movies[my_favorite_movies.find(',', 34)+2:len(my_favorite_movies)]
films['второй'] = my_favorite_movies[my_favorite_movies.find(',')+2:my_favorite_movies.find(',', my_favorite_movies.find(',')+2)]
films['второй с конца'] = my_favorite_movies[my_favorite_movies.find(',', (my_favorite_movies.find(',')+2+(my_favorite_movies.find(',')+2))+2)+2:40]

pprint(films)
