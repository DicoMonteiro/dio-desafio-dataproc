import ctypes
# from ctypes import *

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar) #Funciona no SO windows

if retorno:
    print('Arquivo foi ocultado')
else:
    print('Arquivo não foi ocultado')