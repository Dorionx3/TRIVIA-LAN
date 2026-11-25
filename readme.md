# Trivia LAN - Proyecto Integrador

Juego de trivia multijugador en Python (modo local y en red LAN mediante cliente-servidor) para la asignatura Lógica de Programación (UIDE), Fase 3.

## Integrantes

Joaquín Sánchez Dillon
Dario [Apellido]
Sebastian Leiva

## Cómo ejecutarlo

Tener instalado Python 3.
Abrir la terminal en la carpeta del proyecto.
Ejecutar: `python juego.py` y `python game_logic.py`

## Relación entre diagramas (Fase 2) y código

| Diagrama / Parte de la Fase 2 | Archivo y líneas | Qué cambió |
| :--- | :--- | :--- |
| Menú principal | `juego.py` (líneas 1–15 y 81–91) | Se implementó el ciclo `while True` hasta elegir Salir y se agregaron las opciones MULTIPLAYER y SINGLEPLAYER. |
| Flujo de partida | `juego.py` (líneas 16–79) | Se tradujo el ciclo de 4 rondas, el control de turnos y la acumulación de puntajes a Python. |
| Validación de jugada | `game_logic.py` (líneas X–Y) / `juego.py` (líneas 45–52) | Se tradujo el ciclo que repite la solicitud mientras la respuesta no sea válida (adaptado de opciones A–D a 1–4 en el juego). |
| Fin de partida | `game_logic.py` (líneas X–Y) / `juego.py` (líneas 71–78) | Se tradujeron las condiciones `if/elif/else` para evaluar rondas y puntajes y mostrar: gana Jugador 1, gana Jugador 2, empate o la partida continúa. |

## Video explicativo

Enlace al video (máximo 5 minutos): [Pegar aquí el enlace del video]

## Licencia

Este proyecto usa la licencia MIT. El texto completo está en el archivo `LICENSE` de este repositorio.

## Declaración de autoría y créditos

El diseño de los diagramas en RAPTOR (ubicados en `diseno/`) y la programación en Python fueron realizados por los integrantes del equipo.
Se utilizó únicamente la librería estándar de Python 3.
Uso de IA: Se utilizó Gemini como apoyo para revisar la estructura del repositorio, verificar la traducción de los diagramas a Python y redactar este `README.md`. Todo el código y las pruebas fueron revisados y adaptados por el equipo.