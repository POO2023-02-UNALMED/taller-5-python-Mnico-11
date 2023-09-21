from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    _anfibios = []
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel = None, venenoso = False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel 
        self._venenoso = venenoso
        self._anfibios.append(self)
        
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
        
    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
        
    def getAnfibios(self):
        return self._anfibios
    
    def setAnfibios(self, anfibios):
        self._anfibios = anfibios
        
    def cantidadAnfibios():
        return len(Anfibio._anfibios)
    
    @staticmethod
    def crearRana(nombre, edad, genero):
        colorPiel = "rojo"
        venenoso = True
        habitat = "selva"
        Anfibio(nombre, edad, habitat, genero, colorPiel, venenoso)
        Anfibio.ranas += 1
        
    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        colorPiel = "rojo" 
        venenoso = False
        habitat = "selva"
        Anfibio(nombre, edad, habitat, genero, colorPiel, venenoso)
        Anfibio.salamandras += 1