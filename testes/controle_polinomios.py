from auxiliar import bd_polinomios
from deterministico import algoritmo_deterministico
from monte_carlo import algoritmo_monte_carlo
import random


def aux():
    for item in bd_polinomios().keys():
        p1, p2, p3 = bd_polinomios()[item][0], bd_polinomios()[item][1], bd_polinomios()[item][2]
        print(algoritmo_monte_carlo(p1, p2, p3, 5))
        print(algoritmo_deterministico(p1, p2, p3))
        print('***************************************************************************************')
aux()


def main():
    def generate_polynomial(grau):
        coeficientes = [random.randint(-10, 10) for _ in range(grau + 1)]
        polinomio = ""
        for i in range(grau, -1, -1):
            coeficiente = coeficientes[grau - i]
            if coeficiente != 0:
                polinomio += f"{coeficiente}x^({i} + "
        polinomio = polinomio.rstrip(" + ")
        return polinomio

    polinomios = []
    for _ in range(20):
        grau = random.randint(7, 10)
        polinomio = generate_polynomial(grau)
        polinomios.append(polinomio)

    for polinomio in polinomios:
        print(polinomio)
# main()