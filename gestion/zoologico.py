class Zoologico:
    def __init__(self, nombre=None, ubicacion=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregarZonas(self, zona):
        zona.setZoo(self)
        self.zonas.append(zona)

    def cantidadTotalAnimales(self):
        totalAnimales = sum(zona.cantidadAnimales() for zona in self.zonas)
        return totalAnimales

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getUbicacion(self):
        return self.ubicacion

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def getZona(self):
        return self.zonas