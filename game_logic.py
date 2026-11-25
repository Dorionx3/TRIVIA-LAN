# RF-01: Inicializar menú
opcion_menu = 0

# En Raptor, el ciclo termina cuando la condición es verdadera (opcion_menu == 2)
while opcion_menu != 2:
    try:
        opcion_menu = int(input("TRIVIA LAN | 1. Jugar | 2. Salir\n"))
    except ValueError:
        opcion_menu = 0

    if opcion_menu == 1:
        # RF-02: Inicializar estado
        puntaje_j1 = 0
        puntaje_j2 = 0
        turno = 1
        ronda = 1

        # RF-03: Ciclo de turnos (termina cuando ronda > 4)
        while ronda <= 4:
            if ronda == 1:
                print("Turno J1 - P1: ¿Capital de Ecuador? 1.Lima 2.Quito 3.Bogotá 4.Cali")
                correcta = 2
            elif ronda == 2:
                print("Turno J2 - P2: ¿2 + 2 * 2? 1.8 2.4 3.6 4.2")
                correcta = 3
            elif ronda == 3:
                print("Turno J1 - P3: ¿Planeta rojo? 1.Marte 2.Venus 3.Júpiter 4.Saturno")
                correcta = 1
            else:
                print("Turno J2 - P4: ¿Protocolo con conexión? 1.UDP 2.IP 3.ICMP 4.TCP")
                correcta = 4

            # RF-04: Validar jugada
            jugada_valida = 0
            while jugada_valida != 1:
                try:
                    respuesta = int(input("Respuesta (1-4):\n"))
                except ValueError:
                    respuesta = 0

                if respuesta == 1 or respuesta == 2 or respuesta == 3 or respuesta == 4:
                    jugada_valida = 1
                else:
                    print("Opción inválida, ingrese una alternativa correcta")

            # RF-06: Actualizar puntaje
            if respuesta == correcta:
                print("¡Correcto! +10 puntos")
                if turno == 1:
                    puntaje_j1 = puntaje_j1 + 10
                else:
                    puntaje_j2 = puntaje_j2 + 10
            else:
                print("Incorrecto")

            print(f"Marcador -> J1: {puntaje_j1} | J2: {puntaje_j2}")

            # RF-07: Alternar turno
            if turno == 1:
                turno = 2
            else:
                turno = 1

            ronda = ronda + 1

        # RF-08: Decidir ganador o empate
        if puntaje_j1 > puntaje_j2:
            print("Ganador: Jugador 1")
        elif puntaje_j2 > puntaje_j1:
            print("Ganador: Jugador 2")
        else:
            print("Empate")

    elif opcion_menu == 2:
        print("Saliendo del juego...")
    else:
        print("Opción inválida")