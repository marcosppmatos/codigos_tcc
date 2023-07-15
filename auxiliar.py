import time
import random
import re


def formatar_polinomio(polinomio_bruto: list) -> str:
    '''
    Essa função recebe um polinômio bruto (lista de coeficientes e um grau máximo) e retorna o Polinômio Formatado.
    :param polinomio_bruto: É o polinômio que será formatado.
    :param return: Retorna o polinômio formatado.
    '''
    coeficientes: list = polinomio_bruto[0]
    grau: int = polinomio_bruto[1]
    polinomio_formatado: str = ''
    for i in range(0, grau+1):
        if coeficientes[i] > 0:
            termo = f' + {coeficientes[i]}' + '*x^(' + f'{i}'+')'
        else:
            termo = f' - {-1 * coeficientes[i]}' + '*x^(' + f'{i}'+')'
        polinomio_formatado += termo
    return polinomio_formatado


def bd_polinomios() -> dict:
    '''
    Essa função guarda um banco de dados de polinômios.
    :param return: Dicionário cuja chave é um índice, e o valor uma lista de polinômios cuja igualdade é verdadeira.
    '''
    polinomios: dict = {
    'I1': ['3*x^(2) + 0*x^(1) - 1*x^(0)', '1*x^(2) - 2*x^(1) + 1*x^(0)', '3*x^(4) - 6*x^(3) + 2*x^(2) + 2*x^(1) - 1*x^(0)'],
    'I2': ['3*x^(3) + 2*x^(2) + 1*x^(1) + 0*x^(0)', '6*x^(2) + 5*x^(1) + 4*x^(0)', '18*x^(5) + 27*x^(4) + 28*x^(3) + 13*x^(2) + 4*x^(1) + 0*x^(0)'],
    'I3': ['2*x^(4) - 3*x^(3) + 5*x^(2) - 7*x^(1) + 1*x^(0)', '1*x^(6) + 0*x^(5) + 2*x^(4) + 0*x^(3) - 3*x^(2) + 0*x^(1) + 1*x^(0)', '2*x^(10) - 3*x^(9) + 9*x^(8) - 13*x^(7) + 5*x^(6) - 5*x^(5) - 11*x^(4) + 18*x^(3) + 2*x^(2) - 7*x^(1) + 1*x^(0)'],
    'I4': ['3*x^(5) - 2*x^(4) + 4*x^(3) - 1*x^(2) + 2*x^(1) - 1*x^(0)', '4*x^(6) + 0*x^(5) - 3*x^(4) + 1*x^(3) + 2*x^(2) - 5*x^(1) + 1*x^(0)', '12*x^(11) - 8*x^(10) + 7*x^(9) + 5*x^(8) + 0*x^(7) - 16*x^(6) + 14*x^(5) - 19*x^(4) + 12*x^(3) - 13*x^(2) + 7*x^(1) - 1*x^(0)'],
    'I5': ['4*x^(8) - 3*x^(7) + 2*x^(6) - 5*x^(5) + 6*x^(4) - 7*x^(3) + 8*x^(2) - 9*x^(1) + 10*x^(0)', '3*x^(7) + 2*x^(6) - 5*x^(5) + 6*x^(4) - 7*x^(3) + 8*x^(2) - 9*x^(1) + 10*x^(0)', 
           '12*x^(15) - 1*x^(14) - 20*x^(13) + 28*x^(12) - 48*x^(11) + 81*x^(10) - 124*x^(9) + 178*x^(8) - 200*x^(7) + 275*x^(6) - 320*x^(5) + 310*x^(4) - 284*x^(3) + 241*x^(2) - 180*x^(1) + 100*x^(0)'],
    'I6': ['1*x^(5) + 3*x^(4) + 0*x^(3) - 2*x^(2) + 2*x^(1) + 1*x^(0)', '1*x^(5) + 0*x^(4) + 2*x^(3) + 1*x^(2) + 0*x^(1)+ 1*x^(0)', '1*x^(10) + 3*x^(9) + 2*x^(8) + 5*x^(7) + 5*x^(6) - 2*x^(5) + 5*x^(4) + 4*x^(3) - 1*x^(2) + 2*x^(1) + 1*x^(0)'],

}
    return polinomios


def polinomios_igualdade_verdadeira() -> tuple:
    '''Essa função retorna polinômios cuja igualdade F(X)*G(X) = H(X) é verdadeira.
    :param return : Retorna uma tupla com os três polinômios F(X), G(X) e H(X).'''
    quantidade_igualdades: int = len(bd_polinomios())
    indice: int = 'I'+f'{random.randint(1, quantidade_igualdades)}'
    polinomios: list = bd_polinomios()[indice]
    F_x: str = polinomios[0]
    G_x: str = polinomios[1]
    H_x: str = polinomios[2]
    print(f'Os polinômios testados serão:')
    print(f'F(X): {F_x}')
    print(f'G(X): {G_x}')
    print(f'H(X): {H_x}')
    return F_x, G_x, H_x


def polinomios_igualdade_falsa() -> tuple:
    '''Essa função retorna polinômios cuja igualdade F(X)*G(X) = H(X) é falsa.
    :param return : Retorna uma tupla com os três polinômios F(X), G(X) e H(X).'''
    quantidade_igualdades: int = len(bd_polinomios())
    indice: int = 'I'+f'{random.randint(1, quantidade_igualdades)}'
    polinomios: list = bd_polinomios()[indice]
    polinomios[1]: str = polinomios[1].replace('+', '-')
    F_x: str = polinomios[0]
    G_x: str = polinomios[1]
    H_x: str = polinomios[2]
    print(f'Os polinômios testados serão:')
    print(f'F(X): {F_x}')
    print(f'G(X): {G_x}')
    print(f'H(X): {H_x}')
    return F_x, G_x, H_x


def polinomios_usuario() -> tuple:
    '''
    Essa função será executada se o usuário optar por digitar os próprios polinômios.
    '''
    print('****************************************************************************************************************************')
    print('*********************************************************INSTRUÇÕES*********************************************************')
    print('****************************************************************************************************************************')
    print('Digite os polinômios no formato +a*x^(0) - b*x^(1) + c*x^(2) - d*x^(3)...')
    print('Se o coeficiente for diferente de 0, necessariamente precisa explicitar o *x^(grau)')
    print('****************************************************************************************************************************')
    print(' ')
    F_x: str = input('Digite o Polinômio F(X):  ')
    G_x: str = input('Digite o Polinômio G(X):  ')
    H_x: str = input('Digite o Polinômio H(X):  ')
    print(f'Os polinômios testados serão:')
    print(f'F(X): {F_x}')
    print(f'G(X): {G_x}')
    print(f'H(X): {H_x}')
    return F_x, G_x, H_x


def extrair_termos(polinomio: str) -> dict:
    '''
    Essa função extrai termos do polinômio, retornando um dicionário {grau: coeficiente}.
    :param polinomio: Polinômio que será analisado.
    :param return: Retorna um dicionário cujas chaves são os graus e os valores são os coeficientes. 
    '''
    import re
    polinomio = polinomio.replace(' ', '')
    padrao_dos_termos = r"([+-]?\d+)\*?x?\^?\((\d{1,2})?\)"
    retorno: list = re.findall(padrao_dos_termos, polinomio)
    termos: dict = {}
    grau_polinomio: int = 0

    for item in retorno:
        if not item[1]:
            item = list(item)
            item[1] = 0

        grau = int(item[1])
        coeficiente = int(item[0])
        aux: dict = {grau: coeficiente}
        termos.update(aux)

        if grau > grau_polinomio:
            grau_polinomio = grau
    
    return termos, grau_polinomio


