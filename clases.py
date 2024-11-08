from dataclasses import dataclass

@dataclass
class Vehiculo:
    marca : str
    modelo : str
    nro_ruedas : int
        
    def __repr__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"

@dataclass
class Automovil(Vehiculo):
    velocidad : int
    cilindrada : int
    
    def __repr__(self):
        return f"{super().__repr__()}, {self.velocidad} KM/h, {self.cilindrada} cc."
    
@dataclass
class Particular(Automovil):
    puestos : int
    
    def __repr__(self):
        return f"{super().__repr__()}, puestos: {self.puestos}"

@dataclass
class Carga(Automovil):
    peso_carga : int
    
    def __repr__(self):
        return f"{super().__repr__()}, Carga: {self.peso_carga} Kg."

@dataclass
class Bicicleta(Vehiculo):
    tipo_bici : str
            
    def __repr__(self):
        return f"{super().__repr__()}, Tipo: {self.tipo_bici}"

@dataclass
class Motocicleta(Bicicleta):
    nro_radios : int
    cuadro : str
    motor : str

    def __repr__(self):
        return f"{super().__repr__()}, Tipo: {self.tipo_bici}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro radios : {self.nro_radios}"
