import random
import time
def ImprimirLento(texto):
    for caracter in texto:
        print(caracter, end='', flush=True)
        time.sleep(0.05)
    print()
def asegurar_no_negativo(valor):
    return max(0, valor)
def mostrar_estadisticas(nombre, vida, zombies, dias, comida, agua, municion, medicinas):
    print("\n--- ESTADO DE", nombre.upper(), "(Dia", dias, ") ---")
    ImprimirLento("Vida: " + str(vida))
    ImprimirLento("Comida: " + str(comida) + " | Agua: " + str(agua))
    ImprimirLento("Municion: " + str(municion) + " | Medicinas: " + str(medicinas))
    ImprimirLento("Zombies derrotados: " + str(zombies))
    ImprimirLento("-----------------------------------")

nombre = input("Escribe tu nombre: ")
vida = 100
estadisticas = [random.randint(10, 40) for _ in range(4)]
comida, agua, municion, medicinas = estadisticas
dias, zombies = 1, 0
Suministros = ["agua", "comida", "municion", "medicinas", "nada", "casa"]

while vida > 0:
    mostrar_estadisticas(nombre, vida, zombies, dias, comida, agua, municion, medicinas)
    suministro = random.choice(Suministros)

    if suministro == "agua":
        agua += 10
        ImprimirLento("Encontraste agua! +10")
    elif suministro == "comida":
        comida += 10
        ImprimirLento("Encontraste comida! +10")
    elif suministro == "municion":
        municion += 5
        ImprimirLento("Encontraste municion! +5")
    elif suministro == "medicinas":
        medicinas += 1
        ImprimirLento("Encontraste medicinas! +1")
    elif suministro == "casa":
        ImprimirLento("Encontraste una casa")
        decision = input("Quieres entrar o pasar de largo? ")
        while decision not in ("entrar", "pasar de largo", "pasar"):
            ImprimirLento("Opcion invalida. Escribe 'entrar' o 'pasar'.")
            decision = input("Quieres entrar o pasar de largo? ")
        if decision == "entrar":
            ImprimirLento("Entraste a la casa...")
        else:
            ImprimirLento("Decides seguir explorando")
    else:
        ImprimirLento("No encontraste nada...")

    comida = asegurar_no_negativo(comida)
    agua = asegurar_no_negativo(agua)
    municion = asegurar_no_negativo(municion)
    medicinas = asegurar_no_negativo(medicinas)

    time.sleep(1)
    if random.choice([True, False]):
        ImprimirLento("Un zombie te ataca!")
        atacar = input("Atacar o huir? ")
        while atacar not in ("atacar", "huir", "escapar"):
            ImprimirLento("Opcion invalida. Escribe 'atacar' o 'huir'.")
            atacar = input("Atacar o huir? ")

        if atacar == "atacar" and municion >= 5:
            municion -= 5
            ImprimirLento("Disparaste a un zombie! -5 municion")
            zombies += 1
        elif atacar == "atacar":
            ImprimirLento("No tienes suficiente municion! Pierdes 20 de vida.")
            vida -= 20
        else:
            vida -= 20
            ImprimirLento("Huiste del zombie!")

    municion = asegurar_no_negativo(municion)
    vida = asegurar_no_negativo(vida - 10)
    if vida > 0:
        dias += 1
        time.sleep(1)
if vida <= 0:
    ImprimirLento("Te quedaste sin vida...") 
ImprimirLento("Fin del juego. Sobreviviste " + str(dias) + " dias y derrotaste " + str(zombies) + " zombies.")
juego_reiniciar = input("deseas comenzar de nuevo? (si/no): ")
if juego_reiniciar=="si":
    exec(open(__file__).read())
elif juego_reiniciar=="no":
    ImprimirLento("Gracias por jugar! Hasta la proxima.")
