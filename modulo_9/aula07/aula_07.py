from csv import DictReader, DictWriter
import os

os.chdir('modulo_9' + os.sep + 'aula07')

# criando arquivo
with open('dados.csv', 'w', newline='', encoding='utf-8') as arquivo:
    cabecalho = ['nome', 'idade', 'altura']
    csv_writer = DictWriter(arquivo, fieldnames=cabecalho)
    csv_writer.writeheader()
    csv_writer.writerow({
        'nome': 'Mark',
        'idade': 25,
        'altura': 170
    })
    csv_writer.writerow({
        'nome': 'Carol',
        'idade': 19,
        'altura': 160
    })
    csv_writer.writerow({
        'nome': 'Roberto',
        'idade': 65,
        'altura': 175
    })

# alterando arquivo
with open('dados.csv', 'r', newline='', encoding='utf-8') as arquivo_original:
    dados_originais = DictReader(arquivo_original)
    dados = list(dados_originais)
    with open('dados2.csv', 'w', newline='', encoding='utf-8') as novo_arquivo:
        cabecalho = ['nome', 'idade', 'altura']  
        csv_writer = DictWriter(novo_arquivo, fieldnames=cabecalho)
        csv_writer.writeheader()
        for dado in dados:
            csv_writer.writerow({
                'nome': dado['nome'],
                'idade': dado['idade'],
                'altura': dado['altura'] + 'cm'
            })
