import time
from monte_carlo import menu_monte_carlo
from comparacao_tempo import menu_comparacao_tempo
from deterministico import menu_deterministico


def menu() -> None:
    '''
    Função principal do algoritmo da aplicação. Serve de menu para seleção dos testes.
    '''
    print('****************************************************************************************************************************')
    print('****************************************************************************************************************************')
    print('Esse é um algoritmo que recebe 3 polinômios [F(X), G(X) e H(X)], de maneira a checar se F(X)*G(X) = H(X).')
    print('Para realizar essa comparação, podemos usar 2 métodos: Algoritmo Randomizado de Monte Carlo Baseado-no-Não ou Algoritmo Determinístico.')
    print('****************************************************************************************************************************')
    print('****************************************************************************************************************************')
    print("")
    print('Escolha uma opção (S ou s para sair.)')
    print('1 - Algoritmo Randomizado de Monte Carlo Baseado-no-Não')
    print('2 - Algoritmo Determinístico')
    print('3 - Comparação de tempo de execução Algoritmo Determinístico VS. Algoritmo Randomizado')

    resp: str = input('Escolha ->  ')
    if resp not in ['1', '2', '3', 's', 'S']:
        print('Opção Inválida! Tente novamente!')
        menu()

    if resp in ['s', 'S']:
        print('Obrigado por usar esse algoritmo! Saindo...')
        time.sleep(2)
        exit(0)

    elif resp == '1':
        menu_monte_carlo()
        espera = input('Aplicação Pausada, enter para continuar.')
        menu()

    elif resp == '2':
        menu_deterministico()
        espera = input('Aplicação Pausada, enter para continuar.')
        menu()

    elif resp == '3':
        menu_comparacao_tempo()
        espera = input('Aplicação Pausada, enter para continuar.')
        menu()

    print()


if __name__ == '__main__':
    menu()
    