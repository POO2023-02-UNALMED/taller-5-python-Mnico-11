from zooAnimales.animal import Animal

class Pez(Animal):
    salmon = 0
    bacalao = 0
    _peces = []
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas = None, cantidadAletas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._canitdadAletas = cantidadAletas
        self._peces.append(self)
        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    def getPeces(self):
        return self._peces
    
    def setPeces(self, peces):
        self._peces = peces
        
    def cantidadPeces():
        return len(Pez._peces)
    
    @staticmethod
    def crearSalmon(nombre, edad, genero):
        colorEscamas = "rojo"
        cantidadAletas = 6
        habitat = "oceano"
        Pez(nombre, edad, habitat, genero, colorEscamas, cantidadAletas)
        Pez.salmon += 1
        
    @staticmethod
    def crearBacalao(nombre, edad, genero):
        colorEscamas = "gris" 
        cantidadAletas = 6
        habitat = "oceano"
        Pez(nombre, edad, habitat, genero, colorPiel, venenoso)
        Pez.salamandras += 1