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

    quatidade = 30
    tamanho = 1
    passo = 3
    angulo = 92

    # desenhar a espiral
    espiral(tess, tamanho, quatidade, passo, angulo)    

    # terminar
    turtle.mainloop()
