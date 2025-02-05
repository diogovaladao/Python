import os

print('-----pasta inicial -----')
os.chdir('modulo_9' + os.sep + 'desafio texto' + os.sep + 'desafio arquivos')
print(os.getcwd()) #caminho
print(os.listdir())
print(os.path.join(os.getcwd() + os.sep + 'data de aniversario.xlsx'))
print(os.path.join(os.getcwd() + os.sep + 'precos.txt'))
print(os.path.join(os.getcwd() + os.sep + 'relatorio.pdf'))

print('\n-----voltando pasta -----')
os.chdir('..') #voltando pasta
print(os.getcwd()) #caminho
print(os.listdir())
print(os.path.join(os.getcwd() + os.sep + 'desafio texto1.txt'))
print(os.path.join(os.getcwd() + os.sep + 'desafio texto2.txt'))
print(os.path.join(os.getcwd() + os.sep + 'desafio texto3.txt'))
