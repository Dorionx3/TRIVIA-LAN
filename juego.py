#MENU DEL JUEGO 
#AUTOR: JOHAN DARIO AVALOS GUILCAPI
while True:
    print ("1: MULTIPLAYER")
    print ("2: SINGLEPLAYER")
    print ("3: Salir")
    
    seccion = input("Seleccione: JUGAR O SALIR: ")

    if seccion == "1":
        print ("Modo de juego seleccionado: MULTIPLAYER")

    elif seccion == "2":
        print ("Modo de juego seleccionado: SINGLEPLAYER")
        print ("Este modo aún está en construcción. Volviendo al menú..")

    elif seccion == "3":
        print ("Saliendo del juego...")
        break

    else:
        print ("Opción inválida, intente de nuevo.")


