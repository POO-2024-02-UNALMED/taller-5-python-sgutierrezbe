class Zona:
    def __init__(self, nombre=None, zoo=None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self.animales)

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getAnimales(self):
        return self.animales

    def getZoo(self):
        return self.zoo

    def setZoo(self, zoo):
        self.zoo = zoo