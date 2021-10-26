
#Clase donde se inicia el árbol

class Arbol:
    def __init__(self, carga=None, izq=None, der=None):
        self.carga = carga
        self.izquierda = izq
        self.derecha = der

    def __str__(self):
        return str(self.carga)




# Funciones


def si(preg):

    resp = input(preg)
    return (resp[0] == 's')




def main():
    bucle = True
    raiz = Arbol("Gato")
    while bucle:
        if not si("Estas pensando en un animal? \n "): break

        arbol = raiz
        while arbol.izquierda != None:
            if si(arbol.carga + "?  \n"):
                arbol = arbol.izquierda
            else:
                arbol = arbol.derecha

        # adivinar
        animal = arbol.carga
        if si("Es un/a " + animal + "? \n"):
            print("**************")
            print("¡Eh acertado!")
            print("**************")

            continue

        # Método para obtener información

        nuevo = input("Qué animal era? \n ")
        info = input("Qué diferencia a un/a " + animal + " de un/a " + nuevo + "? \n ")
        indicador = "Si el animal fuera un/a " + animal + " cual sería la respuesta? \n "
        arbol.carga = info
        if si(indicador):
            arbol.izquierda = Arbol(animal)
            arbol.derecha = Arbol(nuevo)
        else:
            arbol.derecha = Arbol(animal)
            arbol.izquierda = Arbol(nuevo)

    return 0


if __name__ == '__main__':
    main()