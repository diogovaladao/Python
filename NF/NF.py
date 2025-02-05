from datetime import datetime
import tkinter as tk
from tkinter import ttk
from geranota import geraNota

DATA_ATUAL = datetime.now().strftime("%d/%m/%Y")

def habilita_Botao(*args):
    if cnpj.current() != -1 and valor.get().strip():
        botao.config(state="normal")
    else:
        botao.config(state="disabled")

def pegaPosicao():
    pyautogui.sleep(3)
    print(pyautogui.position())

def passaValores():
    geraNota(
    data.get(),
    cnpj.current(),
    mes.get(),
    valor.get()
    )

# JANELA
janela = tk.Tk()

janela.geometry("300x200")
janela.title("Gerar NF Automática")

# pega e mostra a data do dia
text_data = tk.Label(janela, text="Digite a data de hoje")
text_data.grid(column=5, row=0)
data = tk.Entry(janela, width=23)
data.grid(column=10, row=0, pady=10)
data.insert(0, DATA_ATUAL)

# mostra o mês atual
texto_mes = tk.Label(janela, text="Escolha o mês")
texto_mes.grid(column=5, row=3)
mes = ttk.Combobox (janela, values=["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO",
                                    "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"])
mes.grid(column=10, row=3)
mes.current(datetime.now().month -1)

# seleção da empresa 
texto_cnpj = tk.Label(janela, text="Escolha a empresa")
texto_cnpj.grid(column=5, row=5, pady=10)
cnpj = ttk.Combobox(janela, values=["Atântica Solutions", "Nuseed Brasil"], state="readonly")
cnpj.grid(column=10, row=5)
cnpj.set("Empresa")

# digitação do valor
texto_valor = tk.Label(janela, text="Digite o valor da nota")
texto_valor.grid(column=5, row=7)
valor = tk.Entry(janela, width=23)
valor.grid(column=10, row=7)

# Botão para disparar a ação desabilitado por padrão
botao = tk.Button(janela, text="Gerar Nota", state="disabled", command=passaValores)
botao.grid(column=10, row=15, pady=10)

# Vincula eventos para validar as entradas
cnpj.bind("<<ComboboxSelected>>",habilita_Botao)
valor.bind("<KeyRelease>",habilita_Botao)

janela.mainloop()