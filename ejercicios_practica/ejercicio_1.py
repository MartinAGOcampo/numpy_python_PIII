# Numpy [Python]
# Ejercicios de práctica

# Autor: Ing.Jesús Matías R.González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con lambda


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro

    # potencia_2 = lambda x:......
    # pot_3 = potencia_2(3)

    # 2)
    # Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista numeros
    # El resultado (la potencia de cada numero) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line", es decir,
    # no declarar la lambda fuera del map sino diretamente dentro
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "potencia_2" dentro del map, debe colocar
    # directamente la lambda.

    # Lista de numeros
    numeros = [1, -5, 4, 3]

    # numeros_potencia = list(map....)

    # Desarrollo de 1) ***************************

    print('Desarrollo 1)')
    print('')

    funcion_lambda = lambda x: x ** 2
    # Calculo de potencia en base al ingreso manual
    ingreso_manual = int(input('Ingrese un numero cualquiera para saber su cuadrado: '))
    potencia_ = funcion_lambda(ingreso_manual)
    print(f'El cuadrado de {ingreso_manual} es {potencia_}')

    print('')
    # Desarrollo de 2) ***************************

    print('Desarrollo 2)')
    print('')

    print('Lo que vamos a relizar a continuacion es practica con map')
    print('Los numeros a continuacion vamos a recorrer y calcular su cuadrado')

    # Se muestra la lista original "numeros"
    print(numeros)

    print('')

    # Desarrollo de lambda y la lista nueva "numeros_potencia" en una sola linea
    numeros_potencia = list(map(lambda x: x**2, numeros))
    print('Elevados cada uno al cuadrado quedan:')
    print(f'{numeros_potencia}, todos guardados en una lista nueva llamada numeros_potencia')

    print('')

    print("terminamos")