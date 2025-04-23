# Numpy [Python]
# Ejercicios de práctica

# Autor: Ing.Jesús Matías R.González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas
from random import random
import random


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Práctica de comprensión de listas
    # 1)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá tener un tamaño de 11
    # números, conteniendo del 0 al 10 inclusive

    # lista_0_10 = [......]

    # 2)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener la tabla del 5,
    # desde el múltiplo 0 al múltiplo 10
    # El resultado esperado es:
    # [0 5 10 15 20 25 30 35 40 45 50]
    # Utilizar comprensión de listas para generar essa lista
    # Lo esperable es que realicen una lista de 11 elementos,
    # del 0 al 10 (como el ejer anterior) pero que cada
    # elemento lo multipliquen x5.

    # tabla_5 = [......]

    # 3)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener 10 números aleatorios,
    # estos números deberán estar entre el rango 1 al 30 representando
    # números posibles de un mes (los números pueden repetirse).
    # NOTA: Importar el módulo random y utilizar randrange
    # o randint para generar números aleatorios.
    # https://docs.python.org/3/library/random.html

    # dias_mes = [.....]

    # Desarrollo de 1) ***************************
    print('Desarrollo 1')
    print('')
    print('Generacion de numeros del uno al diez mediante comprension de listas')

    listado = [x for x in range(11)]

    print(listado)
    print('')

    # Desarrollo de 2) ***************************
    print('Desarrollo 2')
    print('')
    print('Multiplicamos la lista anterior *5: ')

    x_5 = [x*5 for x in range(11)]

    print(x_5)
    print('')

    # Desarrollo de 3) ***************************
    print('Desarrollo 3')
    print('')
    print('Generacion de numeros aleatorios mediante random y generacion de listas')

    dias = [random.randint(1, 30) for x in range(10)]

    print(dias)
    print('')
    print("terminamos")