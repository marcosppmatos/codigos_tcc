# import time
# import random
# import re




# def bd_polinomios() -> dict:
#     '''
#     Essa função guarda um banco de dados de polinômios.
#     :param return: Dicionário cuja chave é o nome do polinômio, e o valor o polinômio.
#     '''
#     polinomios: dict = {
#     'F1': '3*x^2 + 0*x^1 - 1',
#     'G1': '1*x^2 - 2*x^1 + 1',
#     'H1': '3*x^4 - 6*x^3 + 2*x^2 + 2*x^1 - 1',

#     'F2': '3*x^3 + 2*x^2 + 1*x^1 + 0',
#     'G2': '6*x^2 + 5*x^1 + 4',
#     'H2': '18*x^5 + 27*x^4 + 28*x^3 + 13*x^2 + 4*x^1 + 0',

#     # 'F3': '3*x^9 + 0*x^8 + 0*x^7 + 0*x^6 + 0*x^5 + 0*x^4 - 2*x^3 + 0*x^2 - 0*x^1 - 8',
#     # 'G3': '4*x^3 + 2*x^2 - 2*x^1 + 0',
#     # 'H3': '12*x^12 + 6*x^11 + 6*x^10 - 0*x^9 + 0*x^8 + 0*x^7 - 8*x^6 - 4*x^5 - 28*x^4 - 0*x^3 + 16*x^2 + 16*x^1 - 0',

#     # 'F4': '4*x^4 - 7*x^3 + 2*x^2 + 5*x^1 - 3',
#     # 'G4': '3*x^3 + 1*x^2 - 4*x^1 + 2',
#     # 'H4': '12*x^7 - 17*x^6 + 6*x^5 + 4*x^4 - 25*x^3 + 19*x^2 - 23*x^1 + 6',
# }
#     return polinomios


# def igualdade_verdadeira() -> list:
#     '''
#     Essa função guarda alguns polinomios cuja identidade F(X)*G(X) = H(X) será Verdadeira.
#     :param return: Retornará uma lista de listas. Em cada lista que faz parte da lista maior, o 1o valor será o polinômio F(X), o 2o valor G(X) e o 3o valor o H(X).
#     '''
#     polinomios_1: list = []
#     polinomios_2: list = []
#     # polinomios_3: list = []
#     # polinomios_4: list = []

#     LISTA_POLINOMIOS = bd_polinomios()

#     for nome_polinomio in LISTA_POLINOMIOS.keys():
#         if '1' in nome_polinomio:
#             polinomios_1.append(LISTA_POLINOMIOS[nome_polinomio])

#         elif '2' in nome_polinomio:
#             polinomios_2.append(LISTA_POLINOMIOS[nome_polinomio])

#         # elif '3' in nome_polinomio:
#         #     polinomios_3.append(LISTA_POLINOMIOS[nome_polinomio])

#         # elif '4' in nome_polinomio:
#         #     polinomios_4.append(LISTA_POLINOMIOS[nome_polinomio])
    
#     # polinomios_igualdade_verdadeira = [polinomios_1, polinomios_2, polinomios_3, polinomios_4]
#     polinomios_igualdade_verdadeira = [polinomios_1, polinomios_2]
#     return polinomios_igualdade_verdadeira


# def igualdade_falsa():
#     '''
#     Essa função guarda alguns polinomios cuja identidade F(X)*G(X) = H(X) será Falsa.
#     :param return: Retornará uma lista de listas. Em cada lista que faz parte da lista maior, o 1o valor será o polinômio F(X), o 2o valor G(X) e o 3o valor o H(X).
#     '''
#     polinomios_falsos_1: list = []
#     polinomios_falsos_2: list = []
#     polinomios_falsos_3: list = []
#     polinomios_falsos_4: list = []

#     LISTA_POLINOMIOS = bd_polinomios()

#     for nome_polinomio in LISTA_POLINOMIOS.keys():
#         if 'F1' in nome_polinomio:
#             polinomios_falsos_1.append(LISTA_POLINOMIOS['F1'])
#             polinomios_falsos_1.append(LISTA_POLINOMIOS['G2'])
#             polinomios_falsos_1.append(LISTA_POLINOMIOS['H2'])

#         elif 'F2' in nome_polinomio:
#             polinomios_falsos_2.append(LISTA_POLINOMIOS['F2'])
#             polinomios_falsos_2.append(LISTA_POLINOMIOS['G4'])
#             polinomios_falsos_2.append(LISTA_POLINOMIOS['H4'])

#         elif 'F3' in nome_polinomio:
#             polinomios_falsos_3.append(LISTA_POLINOMIOS['F3'])
#             polinomios_falsos_3.append(LISTA_POLINOMIOS['G1'])
#             polinomios_falsos_3.append(LISTA_POLINOMIOS['H1'])

#         elif '4' in nome_polinomio:
#             polinomios_falsos_3.append(LISTA_POLINOMIOS['F4'])
#             polinomios_falsos_3.append(LISTA_POLINOMIOS['G3'])
#             polinomios_falsos_3.append(LISTA_POLINOMIOS['H3'])
    
#     polinomios_igualdade_falsa = [polinomios_falsos_1, polinomios_falsos_2, polinomios_falsos_3, polinomios_falsos_4]
#     return polinomios_igualdade_falsa


# def calcular_valor_polinomio(polinomio: str, valor: int) -> int:
#     '''
#     Função que recebe um polinômio e um valor x, e retorna o resultado desse polinômio quando aplicado o valor x.
#     :param polinomio: É o polinômio para o qual será calculado o resultado.
#     :param valor: É o valor que será aplicado no polinômio.
#     :param return: Retorna o resultado desse polinômio quando aplicado o valor x.
#     '''
#     polinomio = polinomio.replace('^', '**')
#     polinomio = polinomio.replace('x', f'{valor}')
#     total: int = eval(polinomio) 
#     return total


# def teste_igualdade(valor1, valor2, valor3) -> str:
#     '''
#     Função que testa a desigualdade F(x)*G(x) é diferente de H(x), sendo x um valor aleatório.
#     :param valor1: F(x)
#     :param valor2: G(x)
#     :param valor3: H(x)
#     :param return: Retorna o resultado da comparação se F(x)*G(x) é diferente de H(x).
#     '''
#     resultado = 'iguais'
#     if valor1*valor2 != valor3:
#         resultado = 'diferentes'
#     return resultado


# def extrair_grau(polinomio: str) -> int:
#     graus: list = []
#     polinomio = polinomio.replace(' ', '')
#     padrao_dos_coeficientes = r"([+-]?\d+)\*?x?\^?(\d{1,2})?"
#     retorno: list = re.findall(padrao_dos_coeficientes, polinomio)
#     for item in retorno:
#         if not item[1]:
#             item = list(item)
#             item[1] = 0
#         grau = int(item[1])
#         graus.append(grau)

#     return max(graus)


# def algoritmo_monte_carlo(F_x: str, G_x: str, H_x: str, iteracoes: int) -> str:
#     '''
#     :param F_x: É o polinômio que exercerá a função de F(X)
#     :param G_x: É o polinômio que exercerá a função de G(X)
#     :param H_x: É o polinômio que exercerá a função de H(X)
#     :param iteracoes: É o número máximo de iterações do algoritmo de Monte Carlo
#     :param return: É o retorno do algoritmo de Monte Carlo Baseado-no-Não, decidindo se F(X)*G(X) = H(X).
#     '''
#     contador: int = 0
#     resultado: str = ''
#     percentual_erro: float = 1
#     grau = extrair_grau(H_x)
#     while contador < iteracoes:
#         valor: int = random.randint(1, 10*grau)
#         valor_F_x: int = calcular_valor_polinomio(F_x, valor) 
#         valor_G_x: int = calcular_valor_polinomio(G_x, valor)
#         valor_H_x: int = calcular_valor_polinomio(H_x, valor)
#         resultado = teste_igualdade(valor_F_x, valor_G_x, valor_H_x)
#         contador += 1
#         if resultado == 'diferentes':
#             return f'A igualdade F(X)*G(X) = H(X) não é verdadeira! \nNúmero de iterações realizadas: {contador}'
#         percentual_erro *= (1/10)
#     return f'A igualdade F(X)*G(X) = H(X) é verdadeira! O percentual de certeza dessa resposta é {((1 - percentual_erro)*100):0.12f}%!\
#             \nNúmero de iterações realizadas: {contador}'


# def monte_carlo_igualdade_falsa() -> None:
#     '''
#     Essa função será executada se o usuário optar por executar o algoritmo de Monte Carlo para polinômios cuja igualdade F(X)*G(X) = H(X) será falsa.
#     '''
#     print('****************************************************************************************************************************')
#     print('Essa é a execução do algoritmo de Monte Carlo Baseado-no-Não para polinômios [F(X), G(X) e H(X)] cuja igualdade F(X)*G(X) = H(X) é falsa.')
#     print('****************************************************************************************************************************')
#     aux: list = igualdade_falsa()
#     indice: int = random.randint(0, 3)
#     polinomios = aux[indice] 
#     F_x, G_x, H_x = polinomios[0], polinomios[1], polinomios[2]
#     iteracoes: int = int(input('Número de Iterações: '))
#     print(f'Os polinômios testados serão:')
#     print(f'F(X): {F_x}')
#     print(f'G(X): {G_x}')
#     print(f'H(X): {H_x}')
#     print(f'Número de Iterações: {iteracoes}')
#     print(algoritmo_monte_carlo(F_x, G_x, H_x, iteracoes))
#     time.sleep(2)
#     main()


# def monte_carlo_igualdade_verdadeira():
#     '''
#     Essa função será executada se o usuário optar por executar o algoritmo de Monte Carlo para polinômios cuja igualdade F(X)*G(X) = H(X) será verdadeira.
#     '''
#     print('****************************************************************************************************************************')
#     print('Essa é a execução do algoritmo de Monte Carlo Baseado-no-Não para polinômios [F(X), G(X) e H(X)] cuja igualdade F(X)*G(X) = H(X) é verdadeira.')
#     print('****************************************************************************************************************************')
#     aux: list = igualdade_verdadeira()
#     indice: int = random.randint(0, 3)
#     polinomios = aux[indice]
#     F_x, G_x, H_x = polinomios[0], polinomios[1], polinomios[2]
#     iteracoes: int = int(input('Número de Iterações: '))
#     print(f'Os polinômios testados serão:')
#     print(f'F(X): {F_x}')
#     print(f'G(X): {G_x}')
#     print(f'H(X): {H_x}')
#     print(f'Número de Iterações: {iteracoes}')
#     print(algoritmo_monte_carlo(F_x, G_x, H_x, iteracoes))
#     time.sleep(2)
#     main()


# def monte_carlo_polinomios_usuario() -> None:
#     '''
#     Essa função será executada se o usuário optar por digitar os próprios polinômios.
#     '''
#     print('****************************************************************************************************************************')
#     print('*********************************************************INSTRUÇÕES*********************************************************')
#     print('****************************************************************************************************************************')
#     print('Digite os polinômios no formato -1*x^1 + 2*x^2...')
#     print('****************************************************************************************************************************')
#     print(' ')
#     polinomio1: str = input('Digite o Polinômio F(X)')
#     polinomio2: str = input('Digite o Polinômio G(X)')
#     polinomio3: str = input('Digite o Polinômio H(X)')
#     iteracoes: int = int(input('Número de Iterações: '))
#     print(f'Os polinômios testados serão:')
#     print(f'F(X): {polinomio1}')
#     print(f'G(X): {polinomio2}')
#     print(f'H(X): {polinomio3}')
#     print(f'Número de Iterações: {iteracoes}')
#     print(algoritmo_monte_carlo(polinomio1, polinomio2, polinomio3, iteracoes))
#     time.sleep(2)
#     main()


# #TODO: Funções relacionadas À função main(), servem para chamar os algoritmos.
# def monte_carlo() -> None:
#     '''
#     Função principal de Monte Carlo Baseado-no-Não.
#     '''
#     print('****************************************************************************************************************************')
#     print('****************************************************************************************************************************')
#     print('Esse é um algoritmo de Monte Carlo Baseado-no-Não para checar 3 polinômios (F(X), G(X) e H(X)) e testar se F(X)*G(X) = H(X).')
#     print('****************************************************************************************************************************')
#     print('****************************************************************************************************************************')
#     print()
#     print('Escolha uma opção (S ou s para sair.)')
#     print('1 - Polinômios Cuja a igualdade F(X)*G(X) = H(X) é verdadeira')
#     print('2 - Polinômios Cuja a igualdade F(X)*G(X) = H(X) é falsa')
#     print('3 - Inserir os próprios Polinômios')
#     resp: str = input('Escolha ->  ')

#     if resp not in ['1', '2', '3','s', 'S']:
#         print('Opção Inválida! Tente novamente!')
#         print('Deseja voltar ao Menu do Algoritmo de Monte Carlo (1), Menu Geral da Aplicação (2) ou Sair (3)?  ')
#         escolha: str = ''

#         while escolha not in ['1', '2', '3']:
#             escolha: str = input('Digite sua escolha ->  ')
#             if escolha == '1':
#                 monte_carlo()
        
#             elif escolha == '2':
#                 main()
            
#             else:
#                 print('Obrigado por usar esse algoritmo! Saindo...')
#                 time.sleep(2)


#     if resp in ['s', 'S']:
#         print('Obrigado por usar esse algoritmo! Saindo...')
#         time.sleep(2)
#         exit(0)

#     elif resp == '1':
#         monte_carlo_igualdade_verdadeira()

#     elif resp == '2':
#         monte_carlo_igualdade_falsa()

#     else:
#         monte_carlo_polinomios_usuario()
#     print()


# def extrair_termos(polinomio: str) -> dict:
#     '''
#     Essa função extrai termos do polinômio, retornando um dicionário {grau: coeficiente}.
#     :param polinomio: Polinômio que será analisado.
#     :param return: Retorna um dicionário cujas chaves são os graus e os valores são os coeficientes. 
#     '''
#     polinomio = polinomio.replace(' ', '')
#     padrao_dos_coeficientes = r"([+-]?\d+)\*?x?\^?(\d{1,2})?"
#     retorno: list = re.findall(padrao_dos_coeficientes, polinomio)
#     termos: dict = {}
#     for item in retorno:
#         if not item[1]:
#             item = list(item)
#             item[1] = 0
#         grau = int(item[1])
#         coeficiente = int(item[0])
#         aux: dict = {grau: coeficiente}
#         termos.update(aux)
#     return termos


# def formatar_polinomio(polinomio_bruto: list) -> str:
#     '''
#     Essa função recebe um polinômio bruto (lista de coeficientes e um grau máximo) e retorna o Polinômio Formatado.
#     :param polinomio_bruto: É o polinômio que será formatado.
#     :param return: Retorna o polinômio formatado.
#     '''
#     coeficientes: list = polinomio_bruto[0]
#     grau: int = polinomio_bruto[1]
#     polinomio_formatado: str = ''
#     primeiro_termo: str = f'{coeficientes[0]}'
#     for i in range(1, grau):
#         if coeficientes[i] > 0:
#             termo = f' + {coeficientes[i]}' + '*x^' + f'{i}'
#         else:
#             termo = f' - {-1 * coeficientes[i]}' + '*x^' + f'{i}'
#         polinomio_formatado += termo
#     polinomio_formatado = primeiro_termo + polinomio_formatado
#     return polinomio_formatado


# def comparacao_polinomios(polinomio1: str, polinomio2: str, polinomio3: str) -> str:
#     '''
#     Recebe 3 polinômios que serão testados para a igualdade F(X)*G(X) = H(X).
#     :param polinomio1: É o polinômio que fará o papel de F(X).
#     :param polinomio2: É o polinômio que fará o papel de G(X).
#     :param polinomio3: É o polinômio que fará o papel de H(X).
#     :param return: Retorna o resultado do teste da igualdade F(X)*G(X) = H(X).
#     '''
#     resultado_multiplicacao: str = multiplicador_polinomios(polinomio1, polinomio2)
#     termos_polinomio3: dict = extrair_termos(polinomio3)
#     termos_polinomio_resultado: dict = extrair_termos(resultado_multiplicacao)
#     if termos_polinomio3 == termos_polinomio_resultado:
#         return 'A igualdade de F(X)*G(X) = H(X) é verdadeira.'
#     return 'A igualdade de F(X)*G(X) = H(X) é falsa.'


# def polinomio_apartir_coeficientes(coeficientes: list, grau: int) -> str:
#     '''
#     Essa função gera um polinômio a partir de coeficientes recebidos.
#     :param coeficientes: É a lista dos coeficientes do polinômio que será gerado.
#     :param grau: É o grau do polinômio que será gerado.
#     :param return: Retorna o polinômio gerado e formatado.
#     '''
#     polinomio: str = ''
#     polinomio_bruto: list = [coeficientes, grau]
#     polinomio: str = formatar_polinomio(polinomio_bruto)
#     return polinomio


# def multiplicador_polinomios(polinomio1: str, polinomio2: str):
#     '''
#     Essa função multiplica dois polinômios a partir de coeficientes recebidos.
#     :param polinomio1: É o polinômio que fará o papel de F(X).
#     :param polinomio2: É o polinômio que fará o papel de G(X).
#     :param return: Retorna o polinômio resultante da multiplicação formatado.
#     '''
#     termos_polinomio1: dict = extrair_termos(polinomio1)
#     termos_polinomio2: dict = extrair_termos(polinomio2)

#     grau_polinomio1: int = len(termos_polinomio1) - 1
#     grau_polinomio2: int = len(termos_polinomio2) - 1

#     coeficientes: list = [0] * (grau_polinomio1 + grau_polinomio2 + 1)

#     # isso aqui serve pra criar uma lista de 0, cujo tamanho é a quantidade de coeficientes do resultado da multiplicação.
#     aux = [0] * (grau_polinomio1 + grau_polinomio2 + 1)
    
#     for i in range(grau_polinomio1 + 1):
#         for j in range(grau_polinomio2 + 1):
#             coeficientes[i + j] += int(termos_polinomio1[i]) * int(termos_polinomio2[j])
    
#     grau: int = len(coeficientes)
#     polinomio: str = polinomio_apartir_coeficientes(coeficientes, grau)
#     return polinomio


# def deterministico_igualdade_verdadeira():
#     '''
#     Essa função será executada se o usuário optar por executar o algoritmo Determinístico para polinômios cuja igualdade F(X)*G(X) = H(X) será verdadeira.
#     '''
#     print('****************************************************************************************************************************')
#     print('Essa é a execução do algoritmo Determinístico para polinômios [F(X), G(X) e H(X)] cuja igualdade F(X)*G(X) = H(X) é verdadeira.')
#     print('****************************************************************************************************************************')
#     aux: list = igualdade_verdadeira()
#     indice: int = random.randint(0, 3)
#     polinomios = aux[indice] 
#     F_x, G_x, H_x = polinomios[0], polinomios[1], polinomios[2]
#     print(f'Os polinômios testados serão:')
#     print(f'F(X): {F_x}')
#     print(f'G(X): {G_x}')
#     print(f'H(X): {H_x}')
#     print(comparacao_polinomios(F_x, G_x, H_x))
#     time.sleep(2)
#     main()


# def deterministico_igualdade_falsa():
#     '''
#     Essa função será executada se o usuário optar por executar o algoritmo Determinístico para polinômios cuja igualdade F(X)*G(X) = H(X) será falsa.
#     '''
#     print('****************************************************************************************************************************')
#     print('Essa é a execução do algoritmo Determinístico para polinômios [F(X), G(X) e H(X)] cuja igualdade F(X)*G(X) = H(X) é falsa.')
#     print('****************************************************************************************************************************')
#     aux: list = igualdade_falsa()
#     indice: int = random.randint(0, 3)
#     polinomios = aux[indice] 
#     F_x, G_x, H_x = polinomios[0], polinomios[1], polinomios[2]
#     print(f'Os polinômios testados serão:')
#     print(f'F(X): {F_x}')
#     print(f'G(X): {G_x}')
#     print(f'H(X): {H_x}')
#     print(comparacao_polinomios(F_x, G_x, H_x))
#     time.sleep(2)
#     main()


# def deterministico_usuario():
#     '''
#     Essa função será executada se o usuário optar por digitar os próprios polinômios.
#     '''
#     print('****************************************************************************************************************************')
#     print('*********************************************************INSTRUÇÕES*********************************************************')
#     print('****************************************************************************************************************************')
#     print('Digite os polinômios no formato -1*x^1 + 2*x^2...')
#     print('****************************************************************************************************************************')
#     print(' ')
#     polinomio1: str = input('Digite o Polinômio F(X)')
#     polinomio2: str = input('Digite o Polinômio G(X)')
#     polinomio3: str = input('Digite o Polinômio H(X)')
#     print(f'Os polinômios testados serão:')
#     print(f'F(X): {polinomio1}')
#     print(f'G(X): {polinomio2}')
#     print(f'H(X): {polinomio3}')
#     print(comparacao_polinomios(polinomio1, polinomio2, polinomio3))
#     time.sleep(2)
#     main()



# def deterministico():
#     '''
#     Função principal de Determinístico.
#     '''
#     print('****************************************************************************************************************************')
#     print('****************************************************************************************************************************')
#     print('Esse é um algoritmo Determinístico para checar 3 polinômios (F(X), G(X) e H(X)) e testar se F(X)*G(X) = H(X).')
#     print('****************************************************************************************************************************')
#     print('****************************************************************************************************************************')
#     print()
#     print('Escolha uma opção (S ou s para sair.)')
#     print('1 - Polinômios Cuja a igualdade F(X)*G(X) = H(X) é verdadeira')
#     print('2 - Polinômios Cuja a igualdade F(X)*G(X) = H(X) é falsa')
#     print('3 - Inserir os próprios Polinômios')
#     resp: str = input('Escolha ->  ')

#     if resp not in ['1', '2', '3','s', 'S']:
#         print('Opção Inválida! Tente novamente!')
#         print('Deseja voltar ao Menu do Algoritmo Determinístico (1), Menu Geral da Aplicação (2) ou Sair (3)?  ')
#         escolha: str = ''

#         while escolha not in ['1', '2', '3']:
#             escolha: str = input('Digite sua escolha ->  ')
#             if escolha == '1':
#                 deterministico()
        
#             elif escolha == '2':
#                 main()
            
#             else:
#                 print('Obrigado por usar esse algoritmo! Saindo...')
#                 time.sleep(2)


#     if resp in ['s', 'S']:
#         print('Obrigado por usar esse algoritmo! Saindo...')
#         time.sleep(2)
#         exit(0)

#     elif resp == '1':
#         deterministico_igualdade_verdadeira()
#     elif resp == '2':
#         deterministico_igualdade_falsa()
#     else:
#         deterministico_usuario()
#     print()




# def main() -> None:
#     '''
#     Função principal do algoritmo da aplicação.
#     '''
#     print('****************************************************************************************************************************')
#     print('****************************************************************************************************************************')
#     print('Esse é um algoritmo que recebe 3 polinômios [F(X), G(X) e H(X)], de maneira a checar se F(X)*G(X) = H(X).')
#     print('Para realizar essa comparação, podemos usar 2 métodos: Algoritmo Randomizado de Monte Carlo Baseado-no-Não ou Algoritmo Determinístico.')
#     #print('Para realizar essa comparação, podemos usar 3 métodos: Algoritmo Randomizado de Monte Carlo Baseado-no-Não, Algoritmo Determinístico ou Biblioteca Especializada do Python.')
#     print('****************************************************************************************************************************')
#     print('****************************************************************************************************************************')
#     print("")
#     print('Escolha uma opção (S ou s para sair.)')
#     print('1 - Algoritmo Randomizado de Monte Carlo Baseado-no-Não')
#     print('2 - Algoritmo Determinístico')
#     print('3 - Comparação de tempo de execução Algoritmo Determinístico VS. Algoritmo Randomizado')
#     # print('3 - Comparação de tempo de execução Algoritmo Determinístico VS. Algoritmo Randomizado VS. Biblioteca Especializada')
#     resp: str = input('Escolha ->  ')
#     if resp not in ['1', '2', '3', '4','s', 'S']:
#         print('Opção Inválida! Tente novamente!')
#         main()

#     if resp in ['s', 'S']:
#         print('Obrigado por usar esse algoritmo! Saindo...')
#         time.sleep(2)
#         exit(0)

#     elif resp == '1':
#         monte_carlo()

#     elif resp == '2':
#         deterministico()

#     elif resp == '3':
#         comparacao_tempo()

#     # else:
#     #     biblioteca_especializada()
#     print()


# #TODO: Código para chamar a função main() quando o código for executado.
# if __name__ == '__main__':
#     main()


# # print(comparacao_polinomios(F1, G1, H1))
# # print(algoritmo_monte_carlo(F1, G1, H1, 5))