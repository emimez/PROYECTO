import random
def mostrar_estadisticas(nombre, estadisticas):
    Vida, comida, agua, municion, medicinas, dias, zombies = estadisticas
    print("\n--- ESTADO DE", nombre.upper(), "(Dia", dias, ") ---")
    print("Vida:", Vida)
    print("Comida:", comida, "| Agua:", agua)
    print("Municion:", municion, "| Medicinas:", medicinas)
    print("Zombies derrotados:", zombies)
    print("-----------------------------------")
nombre = input("Escribe tu nombre: ")
mostrar_estadisticas(nombre, (100, 50, 75, 20, 3, 1, 0))
Vida, comida, agua, municion, medicinas, dias, zombies = (100, 50, 75, 20, 3, 1, 0)
while Vida > 0:
    dias += 1
    mostrar_estadisticas(nombre, (Vida, comida, agua, municion, medicinas, dias, zombies))
    Suministros = ["agua", "comida", "municion", "medicinas", "nada"]
    suministro = random.choice(Suministros)
    if suministro == "agua":
        agua += 10
        print("Encontraste agua! +10") 
    elif suministro == "comida":
        comida += 10
        print("Encontraste comida! +10")
    elif suministro == "municion":
        municion += 5
        print("Encontraste municion! +5")
    elif suministro == "medicinas":
        medicinas += 1
        print("Encontraste medicinas! +1")
    elif suministro == "nada":
        print("No encontraste nada...")
    if random.choice([True, False]):
        print("Un zombie te ataca!")
    atacar = input("atacar o huir? ")
    if atacar == "atacar":
        if municion > 0:
            municion -= 1
            print("Disparaste a un zombie! -1 municion")
            zombies += 1
        else:
            print("No tienes municion!")
            Vida-=20
    elif atacar == "huir":
        Vida -= 20
        print("Huiste del zombie!")
    Vida -= 10

        
        