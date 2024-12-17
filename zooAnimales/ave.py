from zooAnimales.animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas
        Ave.listado.append(self)
        Animal.totalAves += 1

    @staticmethod
    def cantidadAves():
        return len(Ave.listado)

    def movimiento(self):
        return "volar"

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montañas", genero, "café glorioso")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montañas", genero, "blanco y amarillo")

    def getColorPlumas(self):
        return self.colorPlumas

    def setColorPlumas(self, colorPlumas):
        self.colorPlumas = colorPlumas