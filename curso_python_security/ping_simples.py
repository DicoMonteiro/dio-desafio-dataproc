import os  # Importar o módulo ou biblioteca os (integra os programas e os recursos do sistema operacional)


print("#" * 60) # Imprimindo #60 vezes
ip_ou_host = input('Digite o Ip ou host a ser verificado: ')  #criamos uma variável que vai receber do usuário o ip/host
print("-" * 60) # Imprimindo -60 vezes
os.system('ping -c 4 {}'.format(ip_ou_host))  # chamando system da biblioteca os - comando ping -c -num de pacotes que serão executados {}
print("-" * 60) # Imprimindo -60 vezes