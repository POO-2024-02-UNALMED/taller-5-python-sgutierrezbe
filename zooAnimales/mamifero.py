from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, pelaje=False, patas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)
        Animal.totalMamiferos += 1

    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero.listado)

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @staticmethod
    def crearLeon(nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)

    def isPelaje(self):
        return self.pelaje

    def setPelaje(self, pelaje):
        self.pelaje = pelaje

    def getPatas(self):
        return self.patas

    def setPatas(self, patas):
        self.patas = patas