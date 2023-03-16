import turtle


# função para desenhar poligono
def draw_poli(t, n, sz):
    '''
    Desenha um poligono de n lados de tamanho sz
    Utilizando a tartaruga t
    '''

    for i in range(n):
        t.forward(sz)
        t.left(360/n)


if __name__ == "__main__":
    
    # criar a tartaruga
    tess = turtle.Turtle()

    # definições do poligono
    tamanho = 50
    n = 8

    # poligono
    draw_poli(tess, n, tamanho)

    # terminar
    turtle.mainloop()
