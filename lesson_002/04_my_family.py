#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Папа', 'Мама', 'Брат']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], 176],
    [my_family[1], 165],
    [my_family[2], 170]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост', my_family_height[0][0], '-', my_family_height[0][1], 'см')
print('Рост', my_family_height[1][0], '-', my_family_height[1][1], 'см')
print('Рост', my_family_height[2][0], '-', my_family_height[2][1], 'см')


# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum_height_family = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
print('Общий рост моей семьи -', sum_height_family,'см')