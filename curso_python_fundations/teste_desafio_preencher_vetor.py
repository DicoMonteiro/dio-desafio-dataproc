# Desafio
# Você recebeu o desafio de ler um valor e criar um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.

# Entrada
# A entrada contém um valor inteiro (V<=50).

# Saída
# Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i. O primeiro número do vetor N (N[0]) irá receber o valor de V.

# Exemplos
# Entrada	Saída
# 1	N[0] = 1 N[1] = 2 N[2] = 4 ...



# FUNCIONOU
# x = int(input())
# for i in range (0,10):
#     # N = []
#     # N.append(x)
#     print("N[{}] = {}".format(i, x))
#         # print("N[%i] = %x" %(i-1, x))
#     x*=2
    
    
    # if i == 10:
    #     break


# x = int(input())
# for i in range (1,x+1):
   #complete
        # square = i*i
        # print("%i^2 = %i" %(i, square))
        # print("%i^2 = %i" %(i, square))

# FUNCIONOU
x = int(input())
N = [10]
N[0] = x
for i in range (1,11):
    print("N[%.d] = " %(i-1), N[i-1])
    x*=2
    N.append(x)


# for y in range (0, len(N)):
#     print("N[{}] = {}".format(y, N[y]))


# RECONHECIDO PELA DIO

# x = int(input())
# vetor = [10]
# vetor[0]=x
# for i in range (1, 11):
#   vetor.append(vetor[i-1]*2)
#   print("N[%.d] = " %(i-1), vetor[i-1])