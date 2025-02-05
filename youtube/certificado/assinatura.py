# R$1000,00 Com Esse Projeto Python Freelancer! [Como Fazer] -> https://www.youtube.com/watch?v=VwYqakOB4ow
import openpyxl
from PIL import Image, ImageDraw, ImageFont

# abrir a planilha
planilha_assinatura = openpyxl.load_workbook('Assinaturas.xlsx')
sheet_assinatura = planilha_assinatura['Planilha1']

for indice, linha in enumerate(sheet_assinatura.iter_rows(min_row=2)):
    # acesar cada célula que contém a info que precisamos
    nome = linha[0].value
    cargo = linha[1].value
    telefone = linha[2].value
    
    #  Transferrir os dados da planilha para a assinatura
    # para ficar centralizado o cargo tem que ficar 24 pxs da direita e da esquerda do nome
    fonte_nome = ImageFont.truetype('calibrib.ttf', 20)
    fonte_cargo = ImageFont.truetype('calibri.ttf', 10)

    imagem = Image.open('assinatura_padrao.png')
    desenhar = ImageDraw.Draw(imagem)
    desenhar.text((234,15), nome, font=fonte_nome, fill='#49529b')
    desenhar.text((260,38), cargo, font=fonte_cargo, fill='#49529b')
    desenhar.text((235,54), telefone, font=fonte_cargo, fill='#49529b')

    '''size = width, height = imagem.size
    coordenada = x, y = 239,18
    print(imagem.getpixel(coordenada))'''
        
    imagem.save(f'./imagens/{nome}.png')