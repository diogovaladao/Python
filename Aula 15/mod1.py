import random
from datetime import date

cartoes = ["R$50,00", "R$250,00", "R$120,00"]
hoje = date.today()
data_reg = hoje.strftime("%d/%m/%Y")
valor_sorteado = random.choice(cartoes)

nome = input("Digite seu nome.: ")
idade = int(input("Digite sua idade: "))
aniversario = input("Digite sua data de nascimento no formato dd/mm/aaa: ")

print(f"Olá {nome}, seu registro foi concluído com sucesso no dia  {data_reg} \nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {valor_sorteado}")