# FOR, WHILE e RANGE
# for x in range(101):
#     print(x)

# a = int(input("Entre com o número: "))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div = div + 1
#         # div += 1

# if div == 2:
#     print("número {} é primo".format(a))
# else:
#     print("número {} não é primo".format(a))

# for num in range(101):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1

#     if div == 2:
#         print(num)



# a = 0
# while a < 10:
#     print(a)
#     a += 1

# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com a nota correta: '))
# print(nota)




# Refatorando a estrutura da aula3
a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Vodê digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Vodê digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Vodê digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Vodê digitou errado. Quarto bimestre: '))

media = (a + b + c + d) / 4
print('media: {}'.format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}'.format(media))
# else:
#     print('foi informado alguma nota errada')