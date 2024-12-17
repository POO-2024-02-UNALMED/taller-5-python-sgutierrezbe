from gestion.zona import Zona

class Animal:
    totalAnimales = 0
    totalMamiferos = 0
    totalAves = 0
    totalReptiles = 0
    totalPeces = 0
    totalAnfibios = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        Animal.totalAnimales += 1

    @staticmethod
    def getTotalAnimales():
        return Animal.totalAnimales

    @staticmethod
    def totalPorTipo():
        return (f"Mamiferos : {Animal.totalMamiferos}\n"
                f"Aves : {Animal.totalAves}\n"
                f"Reptiles : {Animal.totalReptiles}\n"
                f"Peces : {Animal.totalPeces}\n"
                f"Anfibios : {Animal.totalAnfibios}")

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getHabitat(self):
        return self.habitat

    def setHabitat(self, habitat):
        self.habitat = habitat

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero

    def movimiento(self):
        return "desplazarse"

    def toString(self):
        return (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, "
                f"habito en {self.habitat} y mi genero es {self.genero}")