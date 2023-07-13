import datetime
import time
from auxiliar import*
from deterministico import algoritmo_deterministico
from monte_carlo import algoritmo_monte_carlo


def menu_comparacao_tempo() -> None:
    '''
    Essa função serve como menu de opções para comparar os algoritmos em relação aos polinômios.
    '''
    print('****************************************************************************************************************************')
    print('Esse algoritmo irá comparar o tempo de execução do Algoritmo de Monte Carlo com o Determinístico, com número de repetições informado pelo usuário ')
    print('Será analisado a média do tempo que cada algoritmo leva para retornar se F(X)*G(X) = H(X).')
    print('****************************************************************************************************************************')
    print('Escolha uma opção (S ou s para sair.)')
    print('1 - Polinômios Cuja a igualdade F(X)*G(X) = H(X) é verdadeira')
    print('2 - Polinômios Cuja a igualdade F(X)*G(X) = H(X) é falsa')
    print('3 - Polinômios Cuja a igualdade F(X)*G(X) = H(X) é Desconhecida')
    print('4 - Voltar pro Menu da Aplicação')

    resp: str = input('Escolha ->  ')
    if resp not in ['1', '2', '3', '4', 's', 'S']:
        print('Opção Inválida! Tente novamente!')
        menu_comparacao_tempo()

    if resp in ['s', 'S']:
        print('Obrigado por usar esse algoritmo! Saindo...')
        time.sleep(2)
        exit(0)

    else:
        menu_comparacao_iteracoes(resp)


def menu_comparacao_iteracoes(selecao) -> None:
    '''
    Essa função serve como menu de opções para comparar os algoritmos em relação aos polinômios.
    '''
    print('****************************************************************************************************************************')
    print('Esse algoritmo irá comparar a média de tempo de execução do Algoritmo de Monte Carlo com o Determinístico, para um valor específico de iterações. ')
    print('Será analisado o tempo que cada algoritmo leva para retornar se F(X)*G(X) = H(X).')
    print('****************************************************************************************************************************')
    print('Informe o número de repetições (0 para sair, 1 voltar pro menu da aplicação)')

    resp: str = input('Repetições ->  ')
    if not resp.isnumeric():
        print('Opção Inválida! Tente novamente!')
        menu_comparacao_iteracoes()
        pass
    
    elif resp == '0':
        print('Obrigado por usar esse algoritmo! Saindo...')
        time.sleep(2)
        exit(0)
        
    elif resp == '1':
        return
        
    else:
        print('****************************************************************************************************************************')
        print('Começo Algoritmo de Monte Carlo')
        print('****************************************************************************************************************************')
        seg_monte_carlo, microsseg_monte_carlo = media_monte_carlo(resp, selecao)
        print('****************************************************************************************************************************')
        print('Começo Algoritmo Determinístico')
        print('****************************************************************************************************************************')
        seg_deterministico, microsseg_deterministico = media_deterministico(resp, selecao)
        print(f'A média de tempo de execução do algoritmo de Monte Carlo para cada iteração foi: {seg_monte_carlo} segundos e {microsseg_monte_carlo}')
        print(f'A média de tempo de execução do algoritmo Determinístico para cada iteração foi: {seg_deterministico} segundos e {microsseg_deterministico}')


def media_monte_carlo(iteracoes, selecao):
    inicio_monte_carlo = datetime.datetime.now()

    for iteracao in range(int(iteracoes)):
        F_x, G_x, H_x = selecao_polinomios(selecao)
        print(f'Iteração {iteracao + 1}: {print(algoritmo_monte_carlo(F_x, G_x, H_x, 5))}')

    final_monte_carlo = datetime.datetime.now()
    tempo_monte_carlo = final_monte_carlo - inicio_monte_carlo
    media_monte_carlo_segundos, media_monte_carlo_microssegundos = int(tempo_monte_carlo.seconds)/int(iteracoes), int(tempo_monte_carlo.microseconds)/int(int(iteracoes))
    return media_monte_carlo_segundos, media_monte_carlo_microssegundos


def media_deterministico(iteracoes, selecao):
    inicio_deterministico = datetime.datetime.now()

    for iteracao in range(int(iteracoes)):
        F_x, G_x, H_x = selecao_polinomios(selecao)
        print(f'Iteração {iteracao + 1}: {print(algoritmo_deterministico(F_x, G_x, H_x))}')

    final_deterministico = datetime.datetime.now()
    tempo_deterministico = final_deterministico - inicio_deterministico
    media_deterministico_segundos, media_deterministico_microssegundos = int(tempo_deterministico.seconds)/int(iteracoes), int(tempo_deterministico.microseconds)/int(iteracoes)
    return media_deterministico_segundos, media_deterministico_microssegundos


def selecao_polinomios(aux):
    '''Essa função retorna polinômios F(X), G(X), H(X) para teste no algoritmo.
    :param aux : Se aux é 0, a função retorna um polinômio cuja igualdade F(X)*G(X) = H(X) é falsa. Se aux é 1, a função retorna um polinômio cuja igualdade é verdadeira.
    Os outros casos são sorteados.
    :param return : Retorna uma tupla com os três polinômios F(X), G(X) e H(X).'''
    quantidade_igualdades: int = len(bd_polinomios())
    indice: int = 'I'+f'{random.randint(1, quantidade_igualdades)}'
    polinomios: list = bd_polinomios()[indice]
    tipo_polinomio = None

    if aux == '1':
        tipo_polinomio: int = 1

    elif aux == '2':
        tipo_polinomio: int = 0
    
    elif aux == '3':
        tipo_polinomio: int = random.randint(0, 1)

    if tipo_polinomio == 0:
        F_x: str = polinomios[0]
        G_x: str = polinomios[2]
        H_x: str = polinomios[1]

    else:
        F_x: str = polinomios[0]
        G_x: str = polinomios[1]
        H_x: str = polinomios[2]

    return F_x, G_x, H_x



if __name__ == '__main__':
    menu_comparacao_tempo()