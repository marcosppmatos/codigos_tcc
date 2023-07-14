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


def menu_comparacao_iteracoes(tipo_de_comparacao) -> None:
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
        iter_monte_carlo: int = int(input('Informe o número de iterações do algoritmo de monte carlo: '))
        print('****************************************************************************************************************************')
        print('Começo Algoritmo de Monte Carlo')
        print('****************************************************************************************************************************')
        seg_monte_carlo, microsseg_monte_carlo, maior_iter_monte_carlo, menor_iter_monte_carlo = media_monte_carlo(resp, tipo_de_comparacao, iter_monte_carlo)
        print('****************************************************************************************************************************')
        print('Começo Algoritmo Determinístico')
        print('****************************************************************************************************************************')
        seg_deterministico, microsseg_deterministico, maior_iter_deterministico, menor_iter_deterministico = media_deterministico(resp, tipo_de_comparacao)
        print('****************************************************************************************************************************')
        print(f'A média de tempo de execução do algoritmo de Monte Carlo para cada iteração foi: {seg_monte_carlo} segundos e {microsseg_monte_carlo} microssegundos')
        print(f'A execução mais demorada do algoritmo de Monte Carlo durou {maior_iter_monte_carlo.seconds} segundos e {maior_iter_monte_carlo.microseconds} microssegundos')
        print(f'A execução mais curta do algoritmo de Monte Carlo durou {menor_iter_monte_carlo.seconds} segundos e {menor_iter_monte_carlo.microseconds} microssegundos')
        print('****************************************************************************************************************************')
        print('****************************************************************************************************************************')
        print(f'A média de tempo de execução do algoritmo Determinístico para cada iteração foi: {seg_deterministico} segundos e {microsseg_deterministico}')
        print(f'A execução mais demorada do algoritmo Determinístico durou {maior_iter_deterministico.seconds} segundos e {maior_iter_deterministico.microseconds} microssegundos')
        print(f'A execução mais curta do algoritmo Determinístico durou {menor_iter_deterministico.seconds} segundos e {menor_iter_deterministico.microseconds} microssegundos')
        print('****************************************************************************************************************************')


def media_monte_carlo(repeticoes, tipo_de_comparacao, iter_monte_carlo):
    '''
    Essa função recebe o número de iterações e o tipo de comparação a ser feita, e retorna a média dos tempos de execução do algoritmo de monte carlo.
    :param iteracoes: numero de repetições do algoritmo de monte carlo que serão realizadas. 
    :param selecao: tipo de comparação da igualdade de polinômios que será realizada, igualdade verdadeira, falsa ou desconhecida. 
    :param return: Retorna a média de segundos e microssegundos dos tempos de execução, a execução mais rápida e a mais demorada do algoritmo de monte carlo. 
    '''
    auxiliar = 0
    inicio_monte_carlo = datetime.datetime.now()

    for repeticao in range(int(repeticoes)):
        inicio_iter_monte_carlo = datetime.datetime.now()
        F_x, G_x, H_x = selecao_polinomios(tipo_de_comparacao)
        print(f'Repetição {repeticao + 1}: {print(algoritmo_monte_carlo(F_x, G_x, H_x, iter_monte_carlo))}')
        final_iter_monte_carlo = datetime.datetime.now()
        tempo_iter_monte_carlo = final_iter_monte_carlo - inicio_iter_monte_carlo
        if auxiliar == 0:
            maior_iteracao_monte_carlo = tempo_iter_monte_carlo
            menor_iteracao_monte_carlo = tempo_iter_monte_carlo
        else:
            if tempo_iter_monte_carlo >= maior_iteracao_monte_carlo:
                maior_iteracao_monte_carlo = tempo_iter_monte_carlo
            if tempo_iter_monte_carlo <= menor_iteracao_monte_carlo:
                menor_iteracao_monte_carlo = tempo_iter_monte_carlo
        auxiliar += 1 

    final_monte_carlo = datetime.datetime.now()
    tempo_monte_carlo = final_monte_carlo - inicio_monte_carlo
    media_monte_carlo_segundos = int(tempo_monte_carlo.seconds)/int(repeticoes)
    media_monte_carlo_microssegundos = int(tempo_monte_carlo.microseconds)/int(repeticoes)
    return media_monte_carlo_segundos, media_monte_carlo_microssegundos, maior_iteracao_monte_carlo, menor_iteracao_monte_carlo


def media_deterministico(repeticoes, tipo_de_comparacao):
    '''
    Essa função recebe o número de iterações e o tipo de comparação a ser feita, e retorna a média dos tempos de execução do algoritmo determinístico.
    :param iteracoes: numero de repetições do algoritmo determinístico que serão realizadas. 
    :param selecao: tipo de comparação da igualdade de polinômios que será realizada, igualdade verdadeira, falsa ou desconhecida. 
    :param return: Retorna a média de segundos e microssegundos dos tempos de execução, a execução mais rápida e a mais demorada do algoritmo determinístico. 
    '''
    auxiliar = 0
    inicio_deterministico = datetime.datetime.now()

    for iteracao in range(int(repeticoes)):
        inicio_iter_deterministico = datetime.datetime.now()
        F_x, G_x, H_x = selecao_polinomios(tipo_de_comparacao)
        print(f'Repetição {iteracao + 1}: {print(algoritmo_deterministico(F_x, G_x, H_x))}')
        final_iter_deterministico = datetime.datetime.now()
        tempo_iter_deterministico = final_iter_deterministico - inicio_iter_deterministico
        if auxiliar == 0:
            maior_iteracao_deterministico = tempo_iter_deterministico
            menor_iteracao_deterministico = tempo_iter_deterministico
        else:
            if tempo_iter_deterministico >= maior_iteracao_deterministico:
                maior_iteracao_deterministico = tempo_iter_deterministico
            if tempo_iter_deterministico <= menor_iteracao_deterministico:
                menor_iteracao_deterministico = tempo_iter_deterministico
        auxiliar += 1 
    final_deterministico = datetime.datetime.now()
    tempo_deterministico = final_deterministico - inicio_deterministico
    media_deterministico_segundos = int(tempo_deterministico.seconds)/int(repeticoes)
    media_deterministico_microssegundos = int(tempo_deterministico.microseconds)/int(repeticoes)
    return media_deterministico_segundos, media_deterministico_microssegundos, maior_iteracao_deterministico, menor_iteracao_deterministico


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


if __name__ == '__main__':
    menu_comparacao_tempo()