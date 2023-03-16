import turtle


# função para desenhar um quadrado
def quadrado(t, tamanho):
    '''
    Desenha um quadrado de tamanho "tamanho"
    Utilizando a tartaruga t
    '''

    for i in range(4):
        t.forward(tamanho)
        t.left(90)


# função para ir para o próximo quadrado
def proximo_quadrado(t, tamanho):
    '''
    Move a tartaruga para o próximo quadrado
    '''

    t.penup()
    t.right(90)
    t.forward(tamanho//2)
    t.right(90)
    t.forward(tamanho//2)
    t.right(180)
    t.pendown()


if __name__ == "__main__":
    # criar a tartaruga
    tess = turtle.Turtle()

    # tamanho do quadrado
    tamanho = 20

    # quantidade de quadrados
    quantidade = 5

    # desenhar os quadrados
    for i in range(quantidade):
        quadrado(tess, tamanho)
        proximo_quadrado(tess, 20)
        tamanho += 20

    # terminar
    turtle.mainloop()
