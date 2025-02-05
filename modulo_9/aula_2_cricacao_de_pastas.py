import os

os.chdir('modulo_9')
if os.path.isdir(os.getcwd() + os.sep + 'Arquivos' + os.sep + 'Arquivos Musicais'):
    print('O Diretório já existe')
else:
    os.mkdir('Arquivos')
    os.mkdir('Arquivos' + os.sep + 'Arquivos Musicais')

if os.path.isdir(os.getcwd() + os.sep + 'Musicas'):
    print('O Diretório já existe')
else:
    os.makedirs('Musicas' + os.sep + 'Rock')
 