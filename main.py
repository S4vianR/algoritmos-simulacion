import os
import random
from termcolor import colored, cprint


def algoritmoLineal(x0, a, c, m):
    i = 1
    # Texto para los parametros
    cprint('---------------------------------------------------------', 'light_magenta', attrs=['bold'])
    print(colored('|    Algoritmo Lineal:', 'light_magenta', attrs=['bold']),
          colored(f"x0: {x0}, a: {a}, c: {c}, m: {m}", 'light_grey'), colored('    |', 'light_magenta', attrs=['bold']))
    cprint('---------------------------------------------------------', 'light_magenta', attrs=['bold'])
    while i <= 10:
        res = (a * x0 + c) % m  # Operación para obtener el número pseudoaleatorio
        numPseudo = res / m  # Número pseudoaleatorio
        # Texto para las iteraciones sin los pseudoaleatorios
        cprint(f"Iteracion no.{i}: {colored(f'{res}', 'white')}", 'light_cyan')
        # Texto para los pseudoaleatorios
        cprint(f"Pseudoaleatorio no.{i}: {colored(f'{numPseudo}', 'white')}\n", 'light_cyan')

        i += 1  # Aumentar el contador
        x0 = res  # Actualizar x0 para el siguiente número
    cprint('---------------------------------------------------------', 'light_magenta', attrs=['bold'])


def algoritmoCongruencial(x0, a, b, c, m):
    i = 1
    # Texto para los parametros
    cprint('-----------------------------------------------------------------', 'light_magenta', attrs=['bold'])
    print(colored('|   Algoritmo Congruencial:', 'light_magenta', attrs=['bold']),
          colored(f"x0: {x0}, a: {a}, b: {b}, c: {c}, m: {m}", 'light_grey'),
          colored('  |', 'light_magenta', attrs=['bold']))
    cprint('-----------------------------------------------------------------', 'light_magenta', attrs=['bold'])
    while i <= 10:
        res = ((a * (x0 ** 2)) + (b * x0) + c) % m  # Operación para obtener el número pseudoaleatorio
        numPseudo = res / m  # Número pseudoaleatorio
        # Texto para las iteraciones sin los pseudoaleatorios
        cprint(f"Iteracion no.{i}: {colored(f'{res}', 'white')}", 'light_cyan')
        # Texto para los pseudoaleatorios
        cprint(f"Pseudoaleatorio no.{i}: {colored(f'{numPseudo}', 'white')}\n", 'light_cyan')

        i += 1  # Aumentar el contador
        x0 = res  # Actualizar x0 para el siguiente número
    cprint('-----------------------------------------------------------------', 'light_magenta', attrs=['bold'])


def algoritmoCuadradosMedios(seed, digits):
    i = 1
    # Texto para los parámetros
    cprint('---------------------------------------------------------', 'light_magenta', attrs=['bold'])
    print(colored('| Algoritmo de Cuadrados Medios:', 'light_magenta', attrs=['bold']),
          colored(f"Semilla: {seed}, Dígitos: {digits}", 'light_grey'))
    cprint('---------------------------------------------------------', 'light_magenta', attrs=['bold'])

    X = seed

    # Hacer la operación siempre y cuando X sea mayor a 0
    while i <= 10:
        ## Primero elevar al cuadrado
        X2 = X ** 2

        ## Extraer los dígitos centrales
        X_str = str(X2)

        ## Si la longitud de la cadena es menor a 4, agregar ceros a la izquierda
        while len(X_str) < 4:
            X_str = '0' + X_str

        ## Extraer los dígitos centrales
        X_centro = int(X_str[1:3])

        ## Normalizar el número
        Y_str = f"{X_centro / 100}"

        # Texto para las iteraciones sin los pseudoaleatorios
        cprint(f"Iteracion no.{i}: {colored(f'{X_centro}', 'white')}", 'light_cyan')
        # Texto para los pseudoaleatorios
        cprint(f"Pseudoaleatorio no.{i}: {colored(f'{Y_str}', 'white')}\n", 'light_cyan')

        X = X_centro
        i += 1  # Aumentar el contador

    cprint('---------------------------------------------------------', 'light_magenta', attrs=['bold'])

def varianza_promedio(n):
    # Generar numeros aleatorios
    nums = []
    for i in range(10):
        nums.append(random.randint(1, 100))
    # Calcular el promedio
    promedio = sum(nums) / n
    # Calcular la varianza
    varianza = sum((xi - promedio) ** 2 for xi in nums) / n

    cprint('Numeros generados:', 'light_magenta', attrs=['bold'])
    cprint(f'{nums}', 'white')
    cprint('Resultados:', 'light_magenta', attrs=['bold'])
    cprint(f'{colored('Promedio:', 'light_cyan')} {promedio}', 'white')
    cprint(f'{colored('Varianza:', 'light_cyan')} {varianza}', 'white')



def clear_console():
    # Para sistemas Unix/Linux/Mac
    if os.name == 'posix':
        os.system('clear')
    # Para sistemas Windows
    elif os.name == 'nt':
        os.system('cls')

def menu():
    opt = 0
    while opt != 5:
        cprint('------------------------------------', 'light_magenta', attrs=['bold'])
        cprint('| 1. Algoritmo Lineal              |', 'light_magenta', attrs=['bold'])
        cprint('| 2. Algoritmo Congruencial        |', 'light_magenta', attrs=['bold'])
        cprint('| 3. Algoritmo de Cuadrados Medios |', 'light_magenta', attrs=['bold'])
        cprint('| 4. Varianza y promedio           |', 'light_magenta', attrs=['bold'])
        cprint('| 5. Salir                         |', 'light_magenta', attrs=['bold'])
        cprint('------------------------------------', 'light_magenta', attrs=['bold'])
        opt = int(input(colored('Ingrese una opción: ', 'light_cyan')))
        if opt == 1:
            x0 = int(input(colored('Ingrese el valor de x0: ', 'light_cyan')))
            a = int(input(colored('Ingrese el valor de a: ', 'light_cyan')))
            c = int(input(colored('Ingrese el valor de c: ', 'light_cyan')))
            m = int(input(colored('Ingrese el valor de m: ', 'light_cyan')))
            # Limpiar la consola
            clear_console()
            algoritmoLineal(x0, a, c, m)
        elif opt == 2:
            x0 = int(input(colored('Ingrese el valor de x0: ', 'light_cyan')))
            a = int(input(colored('Ingrese el valor de a: ', 'light_cyan')))
            b = int(input(colored('Ingrese el valor de b: ', 'light_cyan')))
            c = int(input(colored('Ingrese el valor de c: ', 'light_cyan')))
            m = int(input(colored('Ingrese el valor de m: ', 'light_cyan')))
            # Limpiar la consola
            clear_console()
            algoritmoCongruencial(x0, a, b, c, m)
        elif opt == 3:
            seed = int(input(colored('Ingrese el valor de la semilla: ', 'light_cyan')))
            digits = int(input(colored('Ingrese el valor de d (dígitos a tomar): ', 'light_cyan')))
            # Limpiar la consola
            algoritmoCuadradosMedios(seed, digits)
        elif opt == 4:
            n = int(input(colored('Ingrese el valor de n (números a calcular): ', 'light_cyan')))
            # Limpiar la consola
            clear_console()
            varianza_promedio(n)
        elif opt == 5:
            cprint('Saliendo...', 'light_cyan')
        else:
            cprint('Opción no válida', 'red')

def __main__():
    try:
        menu()
    except KeyboardInterrupt:
        cprint('\nInterrupción del programa detectada. Saliendo...', 'red')

if __name__ == '__main__':
    __main__()
