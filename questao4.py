import turtle


# função para desenhar uma espiral quadrada
def espiral(t, tamanho, quantidade, passo, angulo):
    '''
    Desenha uma série de espirais quadradas de tamaho inicial "tamanho"
    e quantidade de quadrados "quantidade"
    com um passo de "passo" entre cada quadrado
    e um angulo de "angulo" entre cada quadrado
    Utilizando a tartaruga t
    '''

    for i in range(quantidade*4):
        t.forward(tamanho)
        t.left(angulo)
        tamanho += passo


if __name__ == "__main__":
    # criar a tartaruga
    tess = turtle.Turtle()

    quatidade = 14
    tamanho = 1
    passo = 3
    angulo = 90

    # ir para tras para dar espaço
    tess.penup()
    tess.backward(100)
    tess.pendown()

    # desenhar a espiral sem rotação
    espiral(tess, tamanho, quatidade, passo, angulo)

    # ir para frente para dar espaço

    tess.penup()
    tess.forward(300)
    tess.left(90)
    tess.forward(100)
    tess.right(90)
    tess.pendown()

    # desenhar a espiral com rotação
    espiral(tess, tamanho, quatidade, passo, angulo+2)

    # terminar
    turtle.mainloop()
