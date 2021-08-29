import shutil

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    # print(texto)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for i in aluno_nota:
        # print(i)
        lista_notas = i.split(',')
        # print(lista_notas)
        aluno = lista_notas[0]
        # print(aluno)
        lista_notas.pop(0)
        # print(lista_notas)
        # nota1 = int(lista_notas[0])
        # nota2 = int(lista_notas[1])
        # nota3 = int(lista_notas[2])
        # nota4 = int(lista_notas[3])
        # media = (nota1 + nota2 + nota3 + nota4) / 4
        # print('O aluno {} tem a média: {}'.format(aluno, media))
        media = lambda notas: sum([int(i) for i in notas]) / 4
        # print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
    
def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '../curso_python/notas_alunos.txt')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '../digital_innovation_one-master/')

if __name__ == '__main__':
    # escrever_arquivo('Primeira linha. \n')
    # atualizar_arquivo('Segunda linha. \n')
    # ler_arquivo('teste.txt')
    # aluno = 'Monteiro,5,9,10,4\n'
    # atualizar_arquivo('notas.txt', aluno)
    lista_media = media_notas('notas.txt')
    print(lista_media)
    # copia_arquivo('notas.txt')
    move_arquivo('notas_alunos.txt')