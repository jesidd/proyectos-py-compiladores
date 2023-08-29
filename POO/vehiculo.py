class Vehiculo:

    def __init__(self,model,cylinder,color,plate,tipo,emission_level):
        self.model = model
        self.cylinder = cylinder
        self.color = color 
        self.plate = plate
        self.emission_level = emission_level
        self.tipo = tipo
    
   

    def show(self):
        print(f"Modelo: {self.model}, Cilindraje: {self.cylinder}, Color: {self.color}, placa: {self.plate}, Nivel Emisiones: {self.emission_level}, Tipo: {self.tipo} ")


    def modify(self):
        c = input("Desea modificar el cilindraje? si/no : ")
        if c.lower() == 'si':
            self.cylinder = input("Ingrese el cilindraje que desea: ")
            print("Vehiculo modificado")
        c = input("Desea Modificar el color? si/no: ")
        if c.lower() == 'si':
            self.color = input("Ingrese el color que desea: ")
            print("Vehiculo modificado")
        else:
            exit

    
    def start(self):
        pass

    def reduce_emissions(self):
        if self.emission_level == 'alto':
            self.emission_level = 'bajo'
            print(f"Nivel de Emisiones De Gases {self.emission_level} para elmodelo {self.model} ha sido reducido.")
        else:
            print(f"Nivel de Emisiones De Gases {self.emission_level} para el modelo {self.model} esta en un nivel aceptable.")




    
    