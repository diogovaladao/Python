import os

frutas = ['Banana', 'Laranja', 'Maca', 'Melao', 'Mamao']
cores = ['Verde', 'Amarelo', 'Vermelho', 'Azul', 'Preto']
linguagens = ['Python', 'JavaScript', 'Java', 'Cobol', 'C']
arquivos = ['musica.mp3', 'foto.jpg', 'relatorio.pdf', 'senha.txt']
os.chdir('modulo_9' + os.sep + 'Arquivos')

#=========CRIANDO ARQUIVO DE FRUTAS=========
with open('frutas.txt', 'w', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)

print('=========LENDO ARQUIVO=========')
with open('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

#=========ADICIONANDO CORES=========
with open('frutas.txt', 'a', newline='') as arquivo:
    for cor in cores:
        arquivo.write( os.linesep + cor)

print('=========LENDO ARQUIVO NOVAMENTE=========')
with open('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

#=========CRIANDO ARQUIVO DE LINGUAGENS=========
with open('Top 5 Linguagens.txt', 'w', newline='') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep)

#=========CRIANDO VÁRIOS ARQUIVOS=========
for arquivo in arquivos:
    with open(arquivo, 'w') as arquivo:
        pass