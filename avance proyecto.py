import random
import time
def ImprimirLento(texto):
    for caracter in texto:
        print(caracter, end='', flush=True)
        time.sleep(0.05)

    print()
        
def mostrar_estadisticas(nombre, Vida, zombies, dias):
    print("\n--- ESTADO DE", nombre.upper(), "(Dia", dias, ") ---")
    ImprimirLento("Vida: " + str(Vida))
    ImprimirLento("Comida: " + str(comida) + " | Agua: " + str(agua))
    ImprimirLento("Municion: " + str(municion) + " | Medicinas: " + str(medicinas))
    ImprimirLento("Zombies derrotados: " + str(zombies))
    ImprimirLento("-----------------------------------")
nombre = input("Escribe tu nombre: ")
Vida = 100
estadisticas = [random.randint(10, 40) for _ in range(4)]
comida, agua, municion, medicinas = estadisticas
mostrar_estadisticas(nombre, Vida, 0, 1)
dias, zombies = (1, 0)
while Vida > 0:
    dias += 1
    mostrar_estadisticas(nombre, Vida, zombies, dias)
    Suministros = ["agua", "comida", "municion", "medicinas", "nada"]
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
    elif suministro == "nada":
        ImprimirLento("No encontraste nada...")
    time.sleep(1)
    if random.choice([True, False]):
        ImprimirLento("Un zombie te ataca!")
    atacar = input("atacar o huir? ")
    if atacar == "atacar":
        if municion > 0:
            municion -= 5
            ImprimirLento("Disparaste a un zombie! -5 municion")
            zombies += 1
        else:
            ImprimirLento("No tienes municion!")
            Vida-= 20
    elif atacar == "huir":
        Vida -= 20
        ImprimirLento("Huiste del zombie!")
    time.sleep(1)
    Vida -= 10
        
        