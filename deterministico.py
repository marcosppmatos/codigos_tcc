import time
from auxiliar import *


def multiplicador_polinomios(F_x: str, G_x: str) -> str:
    '''
    Essa função multiplica dois polinômios a partir de coeficientes recebidos.
    :param F_x: É o polinômio que fará o papel de F(X).
    :param G_x: É o polinômio que fará o papel de G(X).
    :param return: Retorna o polinômio resultante da multiplicação formatado.
    '''
    termos_F_x: dict = extrair_termos(F_x)[0]
    termos_G_x: dict = extrair_termos(G_x)[0]

    grau_F_x: int = len(termos_F_x) - 1
    grau_G_x: int = len(termos_G_x) - 1

    coeficientes: list = [0] * (grau_F_x + grau_G_x + 1)

    for i in range(grau_F_x + 1):
        for j in range(grau_G_x + 1):
            coeficientes[i + j] += int(termos_F_x[i]) * int(termos_G_x[j])
    
    grau: int = len(coeficientes) - 1
    polinomio_bruto: list = [coeficientes, grau]
    polinomio: str = formatar_polinomio(polinomio_bruto)
    return polinomio


def algoritmo_deterministico(F_x: str, G_x: str, H_x: str) -> str:
    '''
    Recebe 3 polinômios que serão testados para a igualdade F(X)*G(X) = H(X).
    :param F_x: É o polinômio que fará o papel de F(X).
    :param G_x: É o polinômio que fará o papel de G(X).
    :param H_x: É o polinômio que fará o papel de H(X).
    :param return: Retorna o resultado do teste da igualdade F(X)*G(X) = H(X).
    '''
    diferentes = False
    resultado_multiplicacao: str = multiplicador_polinomios(F_x, G_x)
    termos_H_x: dict = extrair_termos(H_x)[0]
    termos_polinomio_resultado: dict = extrair_termos(resultado_multiplicacao)[0]
    if extrair_termos(resultado_multiplicacao)[1] != extrair_termos(H_x)[1]:
        return 'A igualdade de F(X)*G(X) = H(X) é falsa.'
    else:
        for grau in range(extrair_termos(resultado_multiplicacao)[1]):
            if termos_polinomio_resultado[grau] != termos_H_x[grau]:
                diferentes = True
    if not diferentes:
        return 'A igualdade de F(X)*G(X) = H(X) é verdadeira.'
    else:
        return 'A igualdade de F(X)*G(X) = H(X) é falsa.'


def deterministico_igualdade_verdadeira() -> None:
    '''
    Essa função será executada se o usuário optar por executar o algoritmo Determinístico para polinômios cuja igualdade F(X)*G(X) = H(X) será verdadeira.
    '''
    F_x, G_x, H_x = polinomios_igualdade_verdadeira()
    print(algoritmo_deterministico(F_x, G_x, H_x))
    time.sleep(2)
    
    if __name__ == '__main__':
        menu_deterministico()


def deterministico_igualdade_falsa() -> None:
    '''
    Essa função será executada se o usuário optar por executar o algoritmo Determinístico para polinômios cuja igualdade F(X)*G(X) = H(X) será falsa.
    '''
    F_x, G_x, H_x = polinomios_igualdade_falsa()
    print(algoritmo_deterministico(F_x, G_x, H_x))
    time.sleep(2)
    
    if __name__ == '__main__':
        menu_deterministico()


def deterministico_usuario() -> None:
    '''
    Essa função será executada se o usuário optar por digitar os próprios polinômios.
    '''
    F_x, G_x, H_x = polinomios_usuario()
    print(algoritmo_deterministico(F_x, G_x, H_x))
    time.sleep(2)
    
    if __name__ == '__main__':
        menu_deterministico()


def menu_deterministico() -> None:
    '''
    Essa função exerce o papel de menu em relação aos testes com o Algoritmo Determinístico.
    '''
    print('****************************************************************************************************************************')
    print('****************************************************************************************************************************')
    print('Esse é um algoritmo Determinístico para checar 3 polinômios (F(X), G(X) e H(X)) e testar se F(X)*G(X) = H(X).')
    print('****************************************************************************************************************************')
    print('****************************************************************************************************************************')
    print()
    print('Escolha uma opção (S ou s para sair.)')
    print('1 - Polinômios Cuja a igualdade F(X)*G(X) = H(X) é verdadeira')
    print('2 - Polinômios Cuja a igualdade F(X)*G(X) = H(X) é falsa')
    print('3 - Inserir os próprios Polinômios')
    print('4 - Voltar pro Menu da Aplicação')

    resp: str = input('Escolha ->  ')

    if resp not in ['1', '2', '3', '4', 's', 'S']:
        print('Opção Inválida! Tente novamente!')
        menu_deterministico()

    elif resp in ['s', 'S']:
        print('Obrigado por usar esse algoritmo! Saindo...')
        time.sleep(2)
        exit(0)

    elif resp == '1':
        deterministico_igualdade_verdadeira()
        
    elif resp == '2':
        deterministico_igualdade_falsa()

    elif resp == '3':
        deterministico_usuario()

    else:
        return 'Voltando ao menu principal!'

    print()


if __name__ == '__main__':
    menu_deterministico()