from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    _reptiles = []
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas = None, largoCola = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas 
        self._largoCola = largoCola
        self._reptiles.append(self)
        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
        
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
        
    def getReptiles(self):
        return self._reptiles
    
    def setReptiles(self, reptiles):
        self._reptiles = reptiles
        
    def cantidadReptiles():
        return len(Reptil._reptiles)
    
    @staticmethod
    def crearIguana(nombre, edad, genero):
        colorEscamas = "verde"
        largoCola = 3
        habitat = "humedal"
        Reptil(nombre, edad, habitat, genero, colorEscamas, largoCola)
        Reptil.iguanas += 1
        
    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        colorEscamas = "blanco" 
        largoCola = 1
        habitat = "jungla"
        Reptil(nombre, edad, habitat, genero, colorEscamas, largoCola)
        Reptil.serpientes += 1