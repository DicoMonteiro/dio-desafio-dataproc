import itertools

# resultado = itertools.permutations('abc', 3)

string = input('String a ser permutada: ')

resultado = itertools.permutations(string, len(string))  # Realiza a permutação de combinações possíveis com relação a string passada

for i in resultado:
    print(''.join(i))