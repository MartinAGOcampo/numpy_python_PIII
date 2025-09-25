# Numpy [Python]
# Ejercicios de práctica

# Autor: Ing.Jesús Matías R.González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Utilizar comprensión de listas con condicionales

    # 1)
    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # sería un conversor string --> int
    # Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # reemplazar dicho str "no numérico" por 0
    # TIP: Recomendamos ver el método "isdigit" de strings
    # para aplicar en este caso.

    print('Desarrollo')
    print('')
    import random

    lista_inicial = ["caso", "lila", "mora"] + [random.randint(1, 100) for _ in range(5)]
    random.shuffle(lista_inicial)

    print(f'Vamos a trabajar con el siguiente listado {lista_inicial}')
    print('La lista anterior fue generada con 3 palabras predefinidas y 5 numeros elegidos al azar')
    print('')
    
    print('Vamos a extraer las 3 palabras en cualquier ubicacion que este para convertirla a cero:')
    lista_final = [int(x) if str(x).isdigit() else 0 for x in lista_inicial]    
    print('')

    print(f'Con las 3 palabras convertidas la lista queda: {lista_final}')
    print('')

    # ¿Ya terminaron el ejercicio? ¿Por qué no prueban
    # hacer negativo alguno de los números de la lista?
    # ¿Qué sucede con isdigit? Sorprendente no?
    
    print('Prueba de "isdigit()" con los numeros convertidos en negativo')
    print(f'Trabajamos con: {lista_final}')
    print('')

    lista_neg = [-abs(x) if isinstance(x, int) else x for x in lista_final]
    print(f'La lista con los valores negativos es {lista_neg}')
    print('')
        
    isdigit_result = [str(x).isdigit() for x in lista_neg]
    print('Ahora con el metodo isdigit el resultado con valores negativos es:')
    print(isdigit_result)

    print('Vemos como isdigit lo toma como un strings y no como un nro.negativo')
    print('')
    print("terminamos")