# Numpy [Python]
# Ejercicios de práctica

# Autor: Ing.Jesús Matías R.González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Utilizar comprensión de listas para filtrar

    accesos = [10, 50, 7, 5, 15, 25, 3, 4, 13]

    # La lista accesso contiene los números de ID de personal
    # que ingresaron por ese molinete

    # 1)
    # Generar una lista por comprensión de la lista "accesos"
    # una lista que solo contenga (filtrado) los ID de personal
    # entre 1 al 10 inclusive, se desea separar del grupo de accesos
    # los ID entre el 1 y 10.
    # De la lista resultante informar cuantas personas/personal
    # comprendido en dicho rango pasó por ese molinete

    # personal_1_10 = [.....]

    # 2)
    # Generar una lista por comprensión de la listas "accesos"
    # cuyo ID de personal esté dentro de los ID válidos para ingresar
    # por ese molinete:
    id_validos = [3, 4, 7, 8, 15]
    # Debe generar una nueva lista basada en "accesos" filtrada por los ID
    # aprobados en "id_validos".
    # TIP: Utilizar el operador "in" para chequear si un ID de accesos está
    # dentro de "id_validos"

    # personal_valido = [.....]

    # Desarrollo de 1) ***************************
    print('Vamos a trabajar las dos consignas con el siguiente listado de ID:')
    print(accesos)
    print('')

    print('Desarrollo 1')
    print('')


    filtro = [ x for x in accesos if (x < 11)]
    cantidad = len(filtro)
    
    print(f'Las personas que pasaron por el molinete con (ID < 10) fueron {cantidad} en total')
    print('y los ID fueron', filtro )  
    print('')

    # Desarrollo de 2) ***************************
    print('Desarrollo 2')
    print('')

    personal_valido = [ x for x in accesos if x in id_validos]

    print(f'Solo pueden ingresar los siguientes ID:')
    print(personal_valido)
