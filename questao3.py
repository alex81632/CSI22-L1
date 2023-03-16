
def sum_to(n):
    '''
    Retorna a soma de todos os inteiros de 1 até n.
    Um metodo mais rápido seria usar a formula de Gauss:
    n(n+1)/2
    '''

    sum = 0
    for i in range(n+1):
        sum += i
    return sum


if __name__ == "__main__":
    print(sum_to(10))
