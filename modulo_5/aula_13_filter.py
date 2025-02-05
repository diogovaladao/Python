vagas = [
    ['vagta 1', 1200 ],
    ['vagta 2', 2550 ],
    ['vagta 3', 5000 ]
]

def compara_salario(vagas):
    if vagas[1] > 2500:
        return True
    else:
        return False

print(list(filter(compara_salario, vagas)))