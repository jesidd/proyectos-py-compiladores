import vehiculo as v

class Carro(v.Vehiculo):

    def __init__(self,model,cylinder,color,plate,tipo,emision_level,cargo_capacity):
        super().__init__(model,cylinder,color,plate,tipo,emision_level)
        self.cargo_capacity = cargo_capacity
    
    def start(self):
        print("Su carro Encendió con exito")

    def show(self):
        return super().show(), print(f"Capacidad Carga: {self.cargo_capacity}")
    
