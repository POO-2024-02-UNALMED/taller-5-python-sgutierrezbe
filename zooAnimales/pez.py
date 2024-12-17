from zooAnimales.animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, cantidadAletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez.listado.append(self)
        Animal.totalPeces += 1

    @staticmethod
    def cantidadPeces():
        return len(Pez.listado)

    def movimiento(self):
        return "nadar"

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)

    def getColorEscamas(self):
        return self.colorEscamas

    def setColorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self.cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self.cantidadAletas = cantidadAletas