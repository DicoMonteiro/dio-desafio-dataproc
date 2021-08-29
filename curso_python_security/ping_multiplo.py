import os
# from datetime import time
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    # print(dump)
    for ip in dump:
        # print(ip)
        # os.system('ping ' + ip)
        print('Verificando o ip')
        print('-' * 60)
        os.system('ping -c 2 {}'.format(ip))
        print('-' * 60)
        time.sleep(5)









# arquivo = open('hosts.txt', 'r')
# dump = arquivo.read()

# print(dump)