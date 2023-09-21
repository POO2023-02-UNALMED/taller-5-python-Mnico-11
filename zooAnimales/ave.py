from zooAnimales.animal import Animal

class Ave(Animal):
    halcones = 0
    aguilas = 0
    _aves = []
    
    def __init__(self, nombre, edad, habitat, genero, colorPlumas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas 
        self._aves.append(self)
        
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorPiel):
        self._colorPlumas = colorPlumas
    
    def getAves(self):
        return self._aves
    
    def setAves(self, aves):
        self._aves = aves
  
    def cantidadAves():
        return len(Ave._aves)
    
    @staticmethod
    def crearHalcon(nombre, edad, genero):
        colorPlumas = "cafe glorioso"
        habitat = "montanas"
        Ave(nombre, edad, habitat, genero, colorPiel, venenoso)
        Ave.halcones += 1
        
    @staticmethod
    def crearAguila(nombre, edad, genero):
        colorPlumas = "blanco y amarillo" 
        habitat = "montanas"
        Ave(nombre, edad, habitat, genero, colorPiel, venenoso)
        Ave.aguilas += 1