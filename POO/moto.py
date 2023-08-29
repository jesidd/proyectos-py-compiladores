import vehiculo as v

class Moto(v.Vehiculo):

    def __init__(self,model,cylinder,color,plate,tipo,emision_level):
        super().__init__(model,cylinder,color,plate,tipo,emision_level)
    
    def start(self):
        print("Su moto Encendió con exito")
   

