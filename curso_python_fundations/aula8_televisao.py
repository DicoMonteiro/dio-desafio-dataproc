class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada == False:
            self.ligada = True
        else:
            self.ligada = False

    def aumentar_canal(self):
        if self.ligada:
            self.canal += 1

    def diminuir_canal(self):
        if self.ligada:
            self.canal -= 1

# print(__name__)    

if __name__ == '__main__':
    televisao = Televisao()

    print('Televisão está ligada: {}'.format(televisao.ligada))

    televisao.power()

    print('Televisão está ligada: {}'.format(televisao.ligada))

    televisao.power()

    print('Televisão está ligada: {}'.format(televisao.ligada))

    print('Canal: {}'.format(televisao.canal))

    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))

    televisao.aumentar_canal()
    televisao.aumentar_canal()

    print('Canal: {}'.format(televisao.canal))

    televisao.diminuir_canal()

    print('Canal: {}'.format(televisao.canal))