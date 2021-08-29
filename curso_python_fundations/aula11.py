
lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    # print('fechando arquivo')
    # arquivo.close()
    # x = a
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma opração aritimetica')
except IndexError:
    print('Error ao acessar o indice inválido da lista')
# except BaseException as ex:
#     print('erro desconhecido. Error: {}'.format(ex))
except Exception as ex:
    print('erro desconhecido. Error: {}'.format(ex))
else:
    print('Execute se não ocorrer nenhum error.')
finally:
    print('sempre executar')
    print('fechando arquivo')
    arquivo.close()