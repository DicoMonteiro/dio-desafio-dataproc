list_num = [1, 2, 3, 4, 5, 6, 7]
list_animals = ['cachorro', 'gato', 'elefante']

# print(list_num)
# print(list_animals)

# print(list_animals[1])


# for x in list_num:
#     print(x)

# for x in list_animals:
#     print(x)


# print(sum(list_num))
# print(max(list_num))
# print(min(list_num))


# if 'lobo' in list_animals:
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo na lista')
#     list_animals.append('lobo')
#     list_animals.append('arara')
#     print(list_animals)
#     # list_animals.pop()  # retira da ultima posicao na list_animals, sem passar o indice, se passado o indice, ele remove o elemento do indice indicado
#     # print(list_animals)
#     list_animals.sort()  # ordena os elementos em ordem alfabética
#     print(list_animals)
#     list_animals.reverse()  # ordena os elementos ao contrário do que está na lista
#     print(list_animals)

# list_animals.pop(1)  # retirar o elemento que está na posição 2 da list_animals. Nesse caso o elemento 'gato'
# print(list_animals)

# list_animals.remove('elefante') # com o remove é passado o nome do elemento que deseja excluir.
# print(list_animals)


# new_list_animals = list_animals * 3
# print(new_list_animals)



tupla = (1, 10, 12, 14)  # tupla é imutável, não conseguimos alterar os valores dentros dela, diferente de uma lista.
print(tupla)
print(len(list_animals))
print(len(tupla))

tupla_animal = tuple(list_animals)
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(lista_numerica)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)