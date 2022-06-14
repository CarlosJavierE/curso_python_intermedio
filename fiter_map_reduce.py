# FILTER
# lista1 = [1, 4, 5, 6, 9, 13, 19, 21]

# con list comprehesions, filtrar excluyendo los numero pares
# filtro = [i for i in lista1 if i % 2 != 0]
# print(filtro)

# my_filter = list(filter(lambda x: x % 2 != 0, lista1))
# print(my_filter)


# MAP
# lista2 = [1, 2, 3, 4, 5]

# con list comprehesions, elevar al cuadrado
# mapa = [i ** 2 for i in lista2]
# print(mapa)

# my_map = list(map(lambda x: x ** 2, lista2))
# print(my_map)


# REDUCE

# lista3 = [2, 2, 2, 2, 2]

# producto = 1
# for i in lista3:
#     producto *= i
# print(producto)

# from functools import reduce

# lista3 = [2, 2, 2, 2, 2]

# my_reduce = reduce(lambda a, b: a * b, lista3)
# print(my_reduce)


