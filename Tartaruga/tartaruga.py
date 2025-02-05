from turtle import Turtle

t = Turtle()
t.speed(1)

while True:
    direcao = input("Para qual direção devemos ir? 'f:frente' ou 't:trás' ")
    px = int(input(f"Quantos pixels devemos movimentar? "))
    rotacao = input("Rotacionar para d:direita, e:esquerda n:não rotacionar: ")
    if rotacao != 'n':
        angulo = int(input(f"Quantos graus devemos rotacionar? "))

    if rotacao == 'd':
        t.right(angulo)
    elif rotacao == 'e':
        t.left(angulo)
    elif rotacao == 'n':
        t.right(0)
        t.left(0)
    
    if direcao == 'f':
        t.forward(px)
    elif direcao == 't':
        t.backward(px)
    else:
        print("Direção inválida!")
    
    resposta = input("Deseja continuar? (s)sim (n)não ")
    if resposta != 's':
        break 