# R$1000,00 Com Esse Projeto Python Freelancer! [Como Fazer] -> https://www.youtube.com/watch?v=VwYqakOB4ow
import openpyxl
from PIL import Image, ImageDraw, ImageFont

# abrir a planilha
planilha_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_aluno = planilha_alunos['Sheet1']

for indice, linha in enumerate(sheet_aluno.iter_rows(min_row=2)):
    # acesar cada célula que contém a info que precisamos
    nome_curso = linha[0].value
    nome_participante = linha[1].value
    tipo_participante = linha[2].value
    data_inicio = linha[3].value
    data_termino = linha[4].value
    carga_horaria = linha[5].value
    data_emissao = linha[6].value
    
    #  Transferrir os dados da planilha para o certificado
    fonte_nome = ImageFont.truetype('tahomabd.ttf', 90)
    fonte_geral = ImageFont.truetype('tahoma.ttf', 80)
    fonte_data = ImageFont.truetype('tahoma.ttf', 55)

    imagem = Image.open('certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(imagem)
    desenhar.text((1020,827), nome_participante, font=fonte_nome, fill='black')
    desenhar.text((1060,950), nome_curso, font=fonte_geral, fill='black')
    desenhar.text((1435,1065), tipo_participante, font=fonte_geral, fill='black')
    desenhar.text((1480,1182), str(carga_horaria), font=fonte_geral, fill='black')
    desenhar.text((750,1770), data_inicio, font=fonte_data, fill='blue')
    desenhar.text((750,1930), data_termino, font=fonte_data, fill='blue')
    desenhar.text((2220,1930), data_emissao, font=fonte_data, fill='blue')
    
    imagem.save(f'./imagens/{indice} {nome_participante}.png')