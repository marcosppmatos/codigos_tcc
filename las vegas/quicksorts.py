import random
import time

def quicksort_randomizado(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    else:
        pivo = random.choice(arr)
        menores: list = [x for x in arr if x < pivo]
        iguais: list = [x for x in arr if x == pivo]
        maiores: list = [x for x in arr if x > pivo]
        return quicksort_randomizado(menores) + iguais + quicksort_randomizado(maiores)


def quicksort_deterministico(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[-1]
        menores: list = [x for x in arr[::-1] if x < pivo]
        iguais: list = [x for x in arr if x == pivo]
        maiores: list = [x for x in arr[::-1] if x > pivo]
        return quicksort_deterministico(menores) + iguais + quicksort_deterministico(maiores)


def gerar_lista_aleatoria(n) -> list:
    return [random.randint(-10000, 10000) for _ in range(n)]


def main():
    tamanho_lista: int = int(input('Digite o tamanho da lista para a qual serão testadas os métodos Quicksort:  '))
    lista_aleatoria = gerar_lista_aleatoria(tamanho_lista)
    print(f'A lista a ser ordenada é: {lista_aleatoria}')

    inicio = time.time()
    quicksort_randomizado(lista_aleatoria)
    tempo_randomizado = time.time() - inicio

    inicio = time.time()
    quicksort_deterministico(lista_aleatoria)
    tempo_deterministico = time.time() - inicio

    print(f"Lista Ordenada pelo randomizado: {quicksort_randomizado(lista_aleatoria)}")
    print(f"Lista Ordenada pelo Determinístico: {quicksort_deterministico(lista_aleatoria)}")
    
    if tempo_deterministico > tempo_randomizado:
        print(f'O algoritmo quicksort foi mais rápido! Tempo de execução {tempo_randomizado}')
    else:
        print(f'O algoritmo Determinístico foi mais rápido! Tempo de execução {tempo_deterministico}')


if __name__ == '__main__':
    main()