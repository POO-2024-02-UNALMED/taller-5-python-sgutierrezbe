### Project Structure
```
taller_5_python/
│
├── zoo_animales/
│   ├── __init__.py
│   ├── animal.py
│   ├── anfibio.py
│   ├── ave.py
│   ├── mamifero.py
│   ├── pez.py
│   └── reptil.py
│
└── gestion/
    ├── __init__.py
    ├── zona.py
    └── zoologico.py
```

### Python Code

#### `zoo_animales/animal.py`
```python
class Animal:
    total_animales = 0
    total_mamiferos = 0
    total_aves = 0
    total_reptiles = 0
    total_peces = 0
    total_anfibios = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        Animal.total_animales += 1

    @classmethod
    def get_total_animales(cls):
        return cls.total_animales

    @classmethod
    def total_por_tipo(cls):
        return {
            "Mamiferos": cls.total_mamiferos,
            "Aves": cls.total_aves,
            "Reptiles": cls.total_reptiles,
            "Peces": cls.total_peces,
            "Anfibios": cls.total_anfibios
        }

    def movimiento(self):
        return "desplazarse"

    def __str__(self):
        return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}"
```

#### `zoo_animales/anfibio.py`
```python
from .animal import Animal

class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, color_piel=None, venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self.color_piel = color_piel
        self.venenoso = venenoso
        Anfibio.listado.append(self)
        Animal.total_anfibios += 1

    @classmethod
    def cantidad_anfibios(cls):
        return len(cls.listado)

    def movimiento(self):
        return "saltar"

    @classmethod
    def crear_rana(cls, nombre, edad, genero):
        cls.ranas += 1
        return cls(nombre, edad, "selva", genero, "verde", True)

    @classmethod
    def crear_salamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return cls(nombre, edad, "bosque", genero, "negro", False)
```

#### `zoo_animales/ave.py`
```python
from .animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, color_plumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self.color_plumas = color_plumas
        Ave.listado.append(self)
        Animal.total_aves += 1

    @classmethod
    def cantidad_aves(cls):
        return len(cls.listado)

    def movimiento(self):
        return "volar"

    @classmethod
    def crear_halcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return cls(nombre, edad, "montañas", genero, "café glorioso")

    @classmethod
    def crear_aguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return cls(nombre, edad, "montañas", genero, "blanco y amarillo")
```

#### `zoo_animales/mamifero.py`
```python
from .animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, pelaje=False, patas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)
        Animal.total_mamiferos += 1

    @classmethod
    def cantidad_mamiferos(cls):
        return len(cls.listado)

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def crear_caballo(cls, nombre, edad, genero):
        cls.caballos += 1
        return cls(nombre, edad, "pradera", genero, True, 4)

    @classmethod
    def crear_leon(cls, nombre, edad, genero):
        cls.leones += 1
        return cls(nombre, edad, "selva", genero, True, 4)
```

#### `zoo_animales/pez.py`
```python
from .animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, color_escamas=None, cantidad_aletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.cantidad_aletas = cantidad_aletas
        Pez.listado.append(self)
        Animal.total_peces += 1

    @classmethod
    def cantidad_peces(cls):
        return len(cls.listado)

    def movimiento(self):
        return "nadar"

    @classmethod
    def crear_salmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return cls(nombre, edad, "oceano", genero, "rojo", 6)

    @classmethod
    def crear_bacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return cls(nombre, edad, "oceano", genero, "gris", 6)
```

#### `zoo_animales/reptil.py`
```python
from .animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, color_escamas=None, largo_cola=0):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.largo_cola = largo_cola
        Reptil.listado.append(self)
        Animal.total_reptiles += 1

    @classmethod
    def cantidad_reptiles(cls):
        return len(cls.listado)

    def movimiento(self):
        return "reptar"

    @classmethod
    def crear_iguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        return cls(nombre, edad, "humedal", genero, "verde", 3)

    @classmethod
    def crear_serpiente(cls, nombre, edad, genero):
        cls.serpientes += 1
        return cls(nombre, edad, "jungla", genero, "marrón", 1)
```

#### `gestion/zona.py`
```python
from zoo_animales.animal import Animal

class Zona:
    def __init__(self, nombre=None, zoo=None):
        self.nombre = nombre
        self.animales = []
        self.zoo = zoo

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def cantidad_animales(self):
        return len(self.animales)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_animales(self):
        return self.animales

    def get_zoo(self):
        return self.zoo

    def set_zoo(self, zoo):
        self.zoo = zoo
```

#### `gestion/zoologico.py`
```python
from .zona import Zona

class Zoologico:
    def __init__(self, nombre=None, ubicacion=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregar_zona(self, zona):
        zona.set_zoo(self)
        self.zonas.append(zona)

    def cantidad_total_animales(self):
        total_animales = sum(zona.cantidad_animales() for zona in self.zonas)
        return total_animales

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_ubicacion(self):
        return self.ubicacion

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def get_zonas(self):
        return self.zonas
```

### Notes
- Each class in Python corresponds to the Java classes you provided, maintaining the same attributes and methods.
- The `__init__` method in Python serves as the constructor.
- Class methods are used to maintain static-like behavior similar to Java's static methods.
- The `__str__` method is overridden to provide a string representation of the `Animal` class, similar to the `toString()` method in Java.

You can create this project structure in your local environment and copy the provided code into the respective files. This will give you a Python project that mirrors the functionality of the original Java project.