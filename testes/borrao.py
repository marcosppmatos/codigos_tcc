def extrair_coeficientes_grau(polinomio: str) -> tuple:
    '''Essa função retorna os coeficientes e o Grau do Polinômio Analisado.'''
    import re
    graus_final: list = []
    polinomio = polinomio.replace(' ', '')
    padrao_dos_coeficientes = r"(?<!x\^)(?<!x\^-)-?\d+"
    coeficientes: list = re.findall(padrao_dos_coeficientes, polinomio)
    padrao_dos_graus = r"(?=!x\^)(?=!x\^-)-?\d+"
    graus: list = re.findall(padrao_dos_graus, polinomio)

    

    # padrao_dos_graus = r'(\^[0-9]+){1}'
    # graus: list = re.findall(padrao_dos_graus, polinomio)
    # for grau in graus:
    #     graus_final.append(int(grau.split('^')[1]))

    return coeficientes, graus



def testes_coef_grau(polinomio):
    import re
    polinomio = polinomio.replace(' ', '')
    padrao_dos_coeficientes = r"([+-]?\d+)\*?x?\^?(\d{1,2})?"
    retorno: list = re.findall(padrao_dos_coeficientes, polinomio)
    print(retorno)
    termos: dict = {}
    for item in retorno:
        if not item[1]:
            item = list(item)
            item[1] = 0
        grau = int(item[1])
        coeficiente = int(item[0])
        aux: dict = {grau: coeficiente}
        termos.update(aux)
    return termos

teste = '+3*x^2 - 2*x^1 + 1'
teste1 = '+ 20*x^1 + 10*x^2  - 40'
print(testes_coef_grau(teste1))

from deterministico import gerador_polinomio

# teste = gerador_polinomio(6)
# print(teste)

def gerador_polinomio(grau: int) -> str:
    '''
    Essa função gera e retorna Polinômios aleatórios.
    :param grau: É o grau do polinômio que será gerado.
    :param return: Retorna o polinômio gerado e formatado.
    '''
    coeficientes: list = []
    for i in range(grau + 1):
        # coeficiente: float = randint(-100, 100) + round(random(), 2) #Vou comentar por enquanto a parte de reais
        coeficiente: float = randint(-100, 100)
        coeficientes.append(coeficiente)
    polinomio_bruto: list = [coeficientes, grau]
    polinomio: str = formatar_polinomio(polinomio_bruto)
    return polinomio


def polinomios_testados() -> tuple:
    '''
    Gera e retorna 3 polinômios que serão testados pelo Algoritmo de Monte Carlo.
    :param return: Retorna 3 polinômios que serão testados pelo Algoritmo de Monte Carlo.
    '''
    polinomio_1: str = gerador_polinomio(GRAU)
    polinomio_2: str = gerador_polinomio(GRAU)
    polinomio_3: str = gerador_polinomio(GRAU)
    return polinomio_1, polinomio_2, polinomio_3