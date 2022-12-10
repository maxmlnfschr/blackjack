def reglamento():
	print('')
	print('-' * 10)
	print("REGLAMENTO")
	print('-' * 10)
	print("\nEl Blackjack (también llamado veintiuno) es un juego de cartas propio de los casinos, que\n"
		  "se juega con una o más barajas inglesas de 52 cartas (sin los comodines), y que consiste en\n"
		  "sumar un valor lo más próximo a 21 pero sin pasarse. En un casino real cada jugador de la\n"
		  "mesa juega únicamente contra el crupier (o repartidor), intentando conseguir una mejor jugada\n"
		  "que este, y se aplican las siguientes reglas:\n\n"

		  "▪ El crupier no puede tomar decisiones sobre el juego: está obligado\n"
		  "a pedir carta siempre que su puntuación sume 16 o menos,\n"
		  "▪ El crupier está obligado a plantarse si suma 17 o más.\n"
		  "▪ El jugador no está obligado a seguir esas dos reglas, y puede plantarse o seguir pidiendo\n"
		  "cartas.\n\n"

		  "Las cartas numéricas suman su valor, las figuras suman 10 y el As vale 11 o 1, a elección del\n"
		  "jugador.\n"
		  "En el caso del crupier, los Ases valen 11 mientras no se pase de 21, y 1 en caso contrario.\n"
		  "La mejor jugada es conseguir 21 con solo dos cartas, esto es con un As más carta de valor 10.\n"
		  "Esta jugada se conoce como Blackjack o 21 natural. Un Blackjack gana sobre un 21 conseguido\n"
		  "con más de dos cartas.\n\n"

		  "Se juega en una mesa semicircular con capacidad normalmente de 4 a 7 jugadores, cada uno de\n"
		  "los cuales dispone de un casillero marcado en el tapete para realizar su apuesta antes de\n"
		  "recibir las 2 cartas iniciales de cada mano. Esta apuesta debe ser realizada en cada mano,\n"
		  "necesariamente antes de que se ponga en juego la primera carta.\n\n"

		  "------------------\n"
		  "Reglas específicas\n"
		  "------------------\n\n"
		  "Para simplificar un poco el juego original, planteamos las reglas que deberán seguir en el\n"
		  "desarrollo (sin considerar las reglas completas del juego en un casino real):\n\n"

		  "▪ Simular una única mano con un jugador contra el crupier.\n"
		  "▪ El ganador de la mano es quien haya alcanzado un puntaje más cercano a 21, sin pasarse.\n"
		  "A cada jugador se le pueden dar hasta 3 cartas, la tercera carta sólo dependerá del puntaje\n"
		  "alcanzado con las dos anteriores y no es opcional para el usuario.\n"
		  "▪ El AS vale 11 mientras no se pase de 21 y 1 en caso contrario.\n"
		  "▪ No se considera el Blackjack o 21 natural\n"
		  "▪ No hay apuestas en juego.\n")
