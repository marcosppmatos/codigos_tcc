import datetime
from monte_carlo import algoritmo_monte_carlo

def selecao_polinomios(tipo_de_comparacao):
    '''Essa função retorna polinômios F(X), G(X), H(X) para teste no algoritmo.
    :param tipo_de_comparacao : Se tipo_de_comparacao é 0, a função retorna um polinômio cuja igualdade F(X)*G(X) = H(X) é falsa. Se tipo_de_comparacao é 1, a função retorna um polinômio cuja igualdade é verdadeira.
    Os outros casos são sorteados.
    :param return : Retorna uma tupla com os três polinômios F(X), G(X) e H(X).'''
    quantidade_igualdades: int = len(bd_polinomios())
    indice: int = 'I'+f'{random.randint(1, quantidade_igualdades)}'
    polinomios: list = bd_polinomios()[indice]
    tipo_polinomio = None

    if tipo_de_comparacao == '1':
        tipo_polinomio: int = 1

    elif tipo_de_comparacao == '2':
        tipo_polinomio: int = 0
    
    elif tipo_de_comparacao == '3':
        tipo_polinomio: int = random.randint(0, 1)

    if tipo_polinomio == 0:
        # F_x: str = polinomios[0]
        # G_x: str = polinomios[2]
        # H_x: str = polinomios[1]
        polinomios[1] = polinomios[1].replace('+', '-')
        F_x: str = polinomios[0]
        G_x: str = polinomios[1]
        H_x: str = polinomios[2]

    else:
        F_x: str = polinomios[0]
        G_x: str = polinomios[1]
        H_x: str = polinomios[2]

    return F_x, G_x, H_x




print(media_monte_carlo(10, 3, 3))