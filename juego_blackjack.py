import random
import reglas_de_juego


def mostrar_menu():
    """
    Mostrar opciones del menú.
    :return: no retorna nada.
    """
    print('\nSeleccione lo que desea hacer.')
    print('1. Leer las reglas de juego')
    print('2. ¡Jugar!')
    print('3. SALIR')


def generar_mano_del_jugador():
    """
    Generar la mano del jugador.
    :return: el resultado de la mano del jugador, el valor de la primera carta
    que fue guardado en una variable llamada "aux_1" para que su valor no se pierda,
    ya que lo usaremos más adelante, y el valor del palo_1 que también lo usaremos más adelante.

    Esta función genera la mano del jugador en la ronda, usando valores aleatorios para los palos y las cartas.
    """
    print('\nTURNO DEL JUGADOR')
    print('-' * 17)
    print('Lanzamiento de cartas:')

    # Generación aleatoria de los valores de las cartas.
    # Primera carta.
    palo_1 = random.choice(PALOS)
    carta_1 = random.choice(CARTAS)
    aux_1 = carta_1
    print("- Primera carta:", carta_1, 'de', palo_1)
    if carta_1 == J or carta_1 == Q or carta_1 == K:
        carta_1 = 10
    if carta_1 == AS:
        carta_1 = 11

    # Segunda carta.
    palo_2 = random.choice(PALOS)
    carta_2 = random.choice(CARTAS)
    print("- Segunda carta:", carta_2, 'de', palo_2)
    if carta_2 == J or carta_2 == Q or carta_2 == K:
        carta_2 = 10
    if carta_2 == AS and carta_1 == 11:
        carta_2 = 1
    if carta_2 == AS:
        carta_2 = 11

    # Resultado.
    resultado_jugador = carta_1 + carta_2

    # Posibles resultados.
    if 17 <= resultado_jugador <= 21:
        # El puntaje es el máximo (21) y no debe volver a jugar otra carta.
        print("El puntaje es:", resultado_jugador, "PUNTOS. Se planta.")

    if resultado_jugador <= 16:
        # Aún no ha llegado a 21, debe jugar otra carta.
        palo_3 = random.choice(PALOS)
        carta_3 = random.choice(CARTAS)
        print("Puntaje:", resultado_jugador, "PUNTOS. Debe tirar una tercera carta...")
        print("- Tercera carta:", carta_3, 'de', palo_3)
        if carta_3 == J or carta_3 == Q or carta_3 == K:
            carta_3 = 10
        if carta_3 == AS and resultado_jugador > 11:
            carta_3 = 1
        if carta_3 == AS:
            carta_3 = 11

        # Resultado.
        resultado_jugador = carta_1 + carta_2 + carta_3
        print("El puntaje TOTAL es:", resultado_jugador, "PUNTOS.")
        if resultado_jugador > 21:
            print("Se ha excedido de los 21 puntos máximos posibles.")

    return resultado_jugador, aux_1, palo_1


def generar_mano_del_crupier():
    """
    Generar la mano del crupier.
    :return: el resultado de la mano del jugador, el valor de la primera carta
    que fue guardado en una variable llamada "aux_4" para que su valor no se pierda,
    ya que lo usaremos más adelante, y el valor del palo_4 que también lo usaremos más adelante.

    Esta función genera la mano del crupier en la ronda, usando valores aleatorios para los palos y las cartas.
    """
    print('\nTURNO DEL CRUPIER')
    print('-' * 17)
    print('Lanzamiento de cartas:')

    # Generación aleatoria de los valores de las cartas.
    # Primera carta.
    palo_4 = random.choice(PALOS)
    carta_4 = random.choice(CARTAS)
    aux_4 = carta_4
    print("- Primera carta:", carta_4, 'de', palo_4)
    if carta_4 == J or carta_4 == Q or carta_4 == K:
        carta_4 = 10
    if carta_4 == AS:
        carta_4 = 11

    # Segunda carta.
    palo_5 = random.choice(PALOS)
    carta_5 = random.choice(CARTAS)
    print("- Segunda carta:", carta_5, 'de', palo_5)
    if carta_5 == J or carta_5 == Q or carta_5 == K:
        carta_5 = 10
    if carta_5 == AS and carta_4 == 11:
        carta_5 = 1
    if carta_5 == AS:
        carta_5 = 11

    # Resultado.
    resultado_crupier = carta_4 + carta_5

    # Posibles resultados.
    if 17 <= resultado_crupier <= 21:
        # El puntaje es el máximo (21) y no debe volver a jugar otra carta.
        print("El puntaje es:", resultado_crupier, "PUNTOS. Se planta.")

    if resultado_crupier <= 16:
        # Debe jugar otra carta.
        palo_6 = random.choice(PALOS)
        carta_6 = random.choice(CARTAS)
        print("El puntaje es:", resultado_crupier, "PUNTOS. Debe tirar una tercera carta...")
        print("- Tercera carta:", carta_6, 'de', palo_6)
        if carta_6 == J or carta_6 == Q or carta_6 == K:
            carta_6 = 10
        if carta_6 == AS and resultado_crupier > 11:
            carta_6 = 1
        if carta_6 == AS:
            carta_6 = 11

        # Resultado.
        resultado_crupier = carta_4 + carta_5 + carta_6
        print("El puntaje TOTAL es:", resultado_crupier, "PUNTOS.")
        if resultado_crupier > 21:
            print("Se ha excedido de los 21 puntos máximos posibles.")

    return resultado_crupier, aux_4, palo_4


def determinar_el_ganador(resultado_jugador, resultado_crupier):
    """
    Determinar el ganador de la ronda.
    :param resultado_jugador: int - resultado de la mano del jugador.
    :param resultado_crupier: int - resultado de la mano del crupier.
    :return: no retorna nada.

    Determina el ganador de la ronda, crupier o jugador, dependiendo de sus resultados
    y basándose en las reglas de juego para determinar el desenlace.
    """
    print('\nRESULTADO DE LA PARTIDA')
    print('-' * 23)
    if resultado_jugador <= 21 and resultado_crupier <= 21:
        if resultado_jugador == resultado_crupier:
            print("Han obtenido el mismo puntaje. ¡Es un EMPATE! \n\n// Juego terminado //.")
        elif resultado_jugador > resultado_crupier:
            print("El jugador ha obtenido un mayor puntaje. ¡Gana el JUGADOR! \n\n// Juego terminado //")
        else:
            print("El crupier ha obtenido un mayor puntaje. ¡Gana el CRUPIER! \n\n// Juego terminado //")
    if resultado_jugador <= 21 and resultado_crupier > 21:
        print("El crupier excedió los 21 puntos. ¡Gana el jugador por PUNTAJE! \n\n// Juego terminado //")
    if resultado_jugador > 21 and resultado_crupier <= 21:
        print("El jugador excedió los 21 puntos. ¡Gana el crupier por PUNTAJE! \n\n// Juego terminado //")
    if resultado_jugador > 21 and resultado_crupier > 21:
        print("Ambos pierden, se han excedido de los 21 puntos máximos posibles. \n\n// Juego terminado //")


def comprobar_si_existe_una_figura(carta_1, carta_2, carta_4, carta_6):
    """
    Comprueba la existencia de alguna figura.
    :param carta_1: int = primera carta del jugador.
    :param carta_2: int = segunda carta del jugador.
    :param carta_4: int = primera carta del crupier.
    :param carta_6: int = segunda carta del crupier.
    :return: retorna el estado de "figura". False si no hay figura, True si la hay
    (figura está comprendido entre las letras 'J', 'Q' y 'K')

    Al comprobar la existencia, o no existencia de una figura en las cartas ingresadas como parámetros,
    retornará el estado de "figura", que será usada más adelante.
    """
    figura = False
    if (carta_1 or carta_2 or carta_4 or carta_6) == J or carta_6 == Q or carta_6 == K:
        figura = True
    return figura


def mostrar_resultados_adicionales(palo_1, palo_4, aux_1, aux_4):
    """
    Mostrar resultados adicionales.
    :param palo_1: str - palo de la primera carta del jugador.
    :param palo_4: str - palo de la primera carta del crupier.
    :param aux_1: int - valor de la primera carta del jugador.
    :param aux_4: int - valor de la primera carta del crupier.
    :return: no retorna nada.

    Retorna resultados adicionales solicitados, como indicar la existencia de una figura,
    controlar si el palo de la primera carta del jugador y el palo de la primera carta del crupier coinciden,
    y si coincidieran, corroborar si tienen el mismo valor.
    """
    print("\nInformación adicional relevante")
    print('-' * 32)
    # Comprobación de la existencia de alguna figura.
    if comprobar_si_existe_una_figura:
        print("1. Ha surgido al menos una figura.")
    else:
        print("1. No ha surgido ninguna figura.")

    # Comprobación del palo y número o figura de la primera carta del jugador y del crupier.
    if palo_1 != palo_4:
        print("2. El palo de la primera carta del jugador y del crupier NO coinciden.")
    else:
        print("2. El palo de la primera carta del jugador y del crupier coinciden: ", "'", palo_1, "'", sep="")
        if aux_1 == aux_4:
            print("3. Además, tienen el mismo número o figura:", "'", aux_1, "'", sep="")


def opcion1():
    """
    Mostrar el reglamento del juego.
    :return: no retorna nada.
    """
    # Se muestra el reglamento del juego.
    reglas_de_juego.reglamento()


def opcion2():
    """
    Lanzar la partida.
    :return: no retorna nada.

    Esta función realiza el lanzamiento de la partida, las jugadas de ambos participantes.
    """
    print('\n¡COMIENZA EL JUEGO!')
    resultado_del_jugador, aux_1, palo_1 = generar_mano_del_jugador()
    resultado_del_crupier, aux_4, palo_4 = generar_mano_del_crupier()
    determinar_el_ganador(resultado_del_jugador, resultado_del_crupier)
    mostrar_resultados_adicionales(palo_1, palo_4, aux_1, aux_4)


print('-' * 32)
print("BIENVENIDO AL JUEGO DE BLACKJACK")
print('-' * 32)

# Posibles cartas para ambos participantes.
AS, J, Q, K = "AS", "J", "Q", "K"
CARTAS = AS, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
PALOS = "TRÉBOL", "DIAMANTE", "CORAZÓN", "PICA"

# Diccionario con las opciones del menú de opciones del programa.
opciones = {
    1: opcion1,
    2: opcion2,
}

# Ciclo para controlar el menú de opciones y el flujo de ejecución.
while True:
    mostrar_menu()
    opcion = int(input('\nSu opción: '))

    if opcion == 3:
        print('\n¡GRACIAS POR JUGAR :D!')
        print('Programa finalizado.')
        break

    if opcion in opciones:
        opciones[opcion]()  # Opción del diccionario (si de las opciones elige la opción 1, entonces llamar a opcion1)
    else:
        print('\nOpción inválida.')
