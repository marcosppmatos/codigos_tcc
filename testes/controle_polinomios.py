from auxiliar import bd_polinomios
from deterministico import algoritmo_deterministico
from monte_carlo import algoritmo_monte_carlo


def aux():
    for item in bd_polinomios().keys():
        p1, p2, p3 = bd_polinomios()[item][0], bd_polinomios()[item][1], bd_polinomios()[item][2]
        print(algoritmo_monte_carlo(p1, p2, p3, 5))
        print(algoritmo_deterministico(p1, p2, p3))
        print('***************************************************************************************')

aux()