# a = 10
# b = 5
a = int(input('Digite um número? '))
b = int(input('Digite outro número? '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
# print(soma)
# print('soma: ', soma)
# print(str(soma))
# print(subtracao)
# print(multiplicacao)
# print(divisao)
# print(resto)
resultado = ('Soma: {soma} \nSubtracao: {subtracao}' 
            '\nMultiplicacao: {multiplicacao}'
            '\nDivisao: {divisao}'
            '\nResto: {resto}'.format(soma=soma, 
                                    subtracao=subtracao, 
                                    multiplicacao=multiplicacao, 
                                    divisao=divisao, 
                                    resto=resto))
print(resultado)