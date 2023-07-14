import random
import time
import re
from auxiliar import *



def calcular_valor_polinomio(polinomio: str, valor: int) -> int:
    '''
    Função que recebe um polinômio e um valor x, e retorna o resultado desse polinômio quando aplicado o valor x.
    :param polinomio: É o polinômio para o qual será calculado o resultado.
    :param valor: É o valor que será aplicado no polinômio.
    :param return: Retorna o resultado desse polinômio quando aplicado o valor x.
    '''
    # polinomio = polinomio.replace('^', '**')
    # polinomio = polinomio.replace('x', f'{valor}')
    polinomio = re.sub(r'x\^', f'{valor}**', polinomio)
    total: int = eval(polinomio) 
    return total


def teste_valores(valor1, valor2, valor3) -> str:
    '''
    Função que testa a desigualdade F(k)*G(k) é diferente de H(k), sendo x um valor aleatório.
    :param valor1: F(k)
    :param valor2: G(k)
    :param valor3: H(k)
    :param return: Retorna o resultado da comparação se F(k)*G(k) é diferente de H(k).
    '''
    resultado = ''
    if valor1*valor2 != valor3:
        resultado = 'F(k)*G(k) é diferente de H(k)!'
    return resultado


def algoritmo_monte_carlo(F_x: str, G_x: str, H_x: str, iteracoes: int) -> str:
    '''
    Essa função é a aplicação do algoritmo de Monte Carlo.
    :param F_x: É o polinômio que exercerá a função de F(X)
    :param G_x: É o polinômio que exercerá a função de G(X)
    :param H_x: É o polinômio que exercerá a função de H(X)
    :param iteracoes: É o número máximo de iterações do algoritmo de Monte Carlo
    :param return: É o retorno do algoritmo de Monte Carlo Baseado-no-Não, decidindo se F(X)*G(X) = H(X).
    '''
    contador: int = 0
    resultado: str = ''
    grau: int = extrair_grau(H_x)
    percentual_erro: float = 1
    # while contador < iteracoes:
    for contador in range(iteracoes):
        valor: int = random.randint(1, 100*grau)
        valor_F_x: int = calcular_valor_polinomio(F_x, valor) 
        valor_G_x: int = calcular_valor_polinomio(G_x, valor)
        valor_H_x: int = calcular_valor_polinomio(H_x, valor)
        resultado = teste_valores(valor_F_x, valor_G_x, valor_H_x)
        contador += 1
        if resultado:
            return f'A igualdade F(X)*G(X) = H(X) não é verdadeira! \nNúmero de iterações realizadas: {contador}'
        percentual_erro *= (1/100)
    return f'A igualdade F(X)*G(X) = H(X) é verdadeira! O percentual de certeza dessa resposta é maior ou igual a {((1 - percentual_erro)*100):0.12f}%!\
            \nNúmero de iterações realizadas: {contador}'


def monte_carlo_igualdade_verdadeira() -> None:
    '''
    Essa função será executada se o usuário optar por executar o algoritmo de Monte Carlo para polinômios cuja igualdade F(X)*G(X) = H(X) será verdadeira.
    '''
    iteracoes: int = int(input('Número de Iterações: '))
    F_x, G_x, H_x = polinomios_igualdade_verdadeira()
    print(f'Número de Iterações: {iteracoes}')
    print(algoritmo_monte_carlo(F_x, G_x, H_x, iteracoes))
    time.sleep(2)
    if __name__ == '__main__':
        menu_monte_carlo()


def monte_carlo_igualdade_falsa() -> None:
    '''
    Essa função será executada se o usuário optar por executar o algoritmo de Monte Carlo para polinômios cuja igualdade F(X)*G(X) = H(X) será falsa.
    '''
    iteracoes: int = int(input('Número de Iterações: '))
    F_x, G_x, H_x = polinomios_igualdade_falsa()
    print(f'Número de Iterações: {iteracoes}')
    print(algoritmo_monte_carlo(F_x, G_x, H_x, iteracoes))
    time.sleep(2)
    if __name__ == '__main__':
        menu_monte_carlo()


def monte_carlo_polinomios_usuario() -> None:
    '''
    Essa função será executada se o usuário optar por digitar os próprios polinômios.
    '''
    iteracoes: int = int(input('Número de Iterações: '))
    F_x, G_x, H_x = polinomios_usuario()
    print(f'Número de Iterações: {iteracoes}')
    print(algoritmo_monte_carlo(F_x, G_x, H_x, iteracoes))
    time.sleep(2)
    if __name__ == '__main__':
        menu_monte_carlo()


def menu_monte_carlo() -> None:
    '''
    Essa função exerce o papel de menu em relação aos testes com o Algoritmo de Monte Carlo.
    '''
    print('****************************************************************************************************************************')
    print('Esse é um algoritmo de Monte Carlo Baseado-no-Não para checar 3 polinômios (F(X), G(X) e H(X)) e testar se F(X)*G(X) = H(X).')
    print('****************************************************************************************************************************')
    print()
    print('Escolha uma opção (S ou s para sair.)')
    print('1 - Polinômios Cuja a igualdade F(X)*G(X) = H(X) é verdadeira')
    print('2 - Polinômios Cuja a igualdade F(X)*G(X) = H(X) é falsa')
    print('3 - Inserir os próprios Polinômios')
    print('4 - Voltar pro Menu da Aplicação')

    resp: str = input('Escolha ->  ')
    if resp not in ['1', '2', '3', '4','s', 'S']:
        print('Opção Inválida! Tente novamente!')
        menu_monte_carlo()

    elif resp in ['s', 'S']:
        print('Obrigado por usar esse algoritmo! Saindo...')
        time.sleep(2)
        exit(0)

    elif resp == '1':
        monte_carlo_igualdade_verdadeira()

    elif resp == '2':
        monte_carlo_igualdade_falsa()

    elif resp == '3':
        monte_carlo_polinomios_usuario()

    else:
        return 'Voltando ao menu principal!'


if __name__ == '__main__':
    menu_monte_carlo()
