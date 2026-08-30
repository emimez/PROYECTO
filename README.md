# PROYECTO
Repositorio para el proyecto de fundamentos de programación
Decidi como proyecto desarrollar un simulador de supervivencia en un apocalipsis zombie en el que el usuario controle a un personaje y tome decisiones durante diferentes situaciones, con eventos aleatorios que pueden o beneficiar o perjudicar al jugador dependiendo de la suerte.
El jugador debera administrar recurrsos, enfrentarse o escapar de zombies y tomar decisiones para intentar sobrevivir a la mayor cantidad de dias posibles. Al terminar el juego el programa demostrara los dias sobrevivios, los zombies eliminados y una puntuacion final.
Considero que este proyecto es de valor por que al ser hecho sobre eventos aleatorios y toma de decisiones, me obliga a usar elementos de programación que ya se me han sido instruidos como variables, condicionales, ciclos, funciones y listas
# ALGORITMO

ENTRADAS

-Nombre del jugador 
-Vida 
-Comida
-Agua 
-Municion
-Medicinas
-Dias_sobrevividos
-Zombies 
-Opciones para cada situacion:

---Pelear 
---Escapar
---Explorar
---Descansar

PROCESOS

Asignar valores a las variables:

  Asignar 100 a "vida"
  Asignar 5 a "comida"
  Asignar 5 a "agua"
  Asignar 3 a "municion"
  Asignar 2 a "medicinas"
  Asignar 0 a "dias_Sobrevividos"
  Asignar 0 a "zombies_derrotados"
  estadísticas = [vida, comida, agua, municion, medicinas, dias_sobrevividos, zombies_derrotados]
  
Mientras vida > 0:

  dias_sobrevividos = "dias_sobrevividos" + 1
  Mostras "estadisticas"
  Generar una situacion random
  Si el jugador encuentra suministros 
  Mostrar los recursos encontrados
   Si es comida entonces comida = "comida" + 1 
    Sino 
   Si es agua entonces agua = "agua" + 1
    Sino
   Si es municion entonces municion = "municion" + 1
  Si el jugador encuentra zombies:
  Mostrar las opciones pelear o escapar
  Pedir una decision
  Si decision = "pelear" entonces
  comprobar si municion >= 1 si es "true" entonces reducir municion = "municion" - 1 y aumentar zombies derrotados\
  "zombies_derrotados" + 1 Sino tiene municion entonces reducir vida vida= "vida" - 20
  Si decide escapar:
    entonces reducir vida = "vida" - 10
  Si encuentra un lugar para descansar 
  Aumentar vida vida= "vida" + 40
  reducir una cantidad de comida y agua comida= "comida"- 1 y agua= "agua" - 1
Fin Si
Estadisticas_actualizadas = [vida, comida, agua, municion, medicinas, dias_sobrevividos, zombies_derrotados]
Comprobar si algún recurso llego a 0 y Si Agua <= 0 o comida es <=0 entonces Vida= "vida" - 10
Sino entonces Comprobar si el jugador puede continuar
Si "vida" = 0
entonces desplegar "Game Over"
si no desplegar "continuar el juego"

SALIDAS
Nombre del jugador
Dias sobrevividos
Zombies derrotados
Cantidad de comida restante 
Cantidad de agua restante
Cantidad de Medicina restante
Cantidad de Municion restante
  
