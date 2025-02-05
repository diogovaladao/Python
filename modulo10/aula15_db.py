import sqlite3

with sqlite3.connect('artista.db') as conexao:
    sql = conexao.cursor()
    #sql.execute('CREATE TABLE banda(nome text, estilo text, membros integer);')

    nome = input('Digite o nome de uma banda: ')
    estilo = input('Digite o estilo da banda: ')
    qtd_membros = int(input('Quantidade de membros: '))

    sql.execute('INSERT INTO banda VALUES (?,?,?)', [nome, estilo, qtd_membros])
    conexao.commit()
    bandas = sql.execute('SELECT * FROM banda;')
    for banda in bandas:
        print(banda)