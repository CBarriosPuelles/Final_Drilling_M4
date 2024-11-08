from clases import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta
from utils import guardar_datos_csv, leer_datos_csv

print("------------------------------------")
#solicito al usuario la cantidad de vehículos a ingresar
cant_vehiculos = int(input("Cuantos vehículos desea insertar: "))
print("------------------------------------")
automoviles = []
contador = 1
while contador <= cant_vehiculos:
    print(f"\nDatos del automóvil {contador}")
    try:
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte cilindraje en cc: "))
        contador += 1
        auto = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        automoviles.append(auto)
    except ValueError:
        print("Debe ingresar números")
        
print("------------------------------------")
print("\nImprimiendo por pantalla los Vehículos:\n")
print("------------------------------------")
for i, auto in enumerate(automoviles,1):
    print(f"Datos del automóvil {i}: {auto}")
print("------------------------------------")

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5) 
carga = Carga("Daft Trucks", "G 38", 10, "120", "1000", 2000)
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print("\n-------------------------------------")
print(particular)
print(carga)
print(bicicleta)
print(motocicleta)
print("\n-------------------------------------")

print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")

guardar_datos_csv([particular, carga, bicicleta, motocicleta],"vehiculos.csv")

leer_datos_csv("vehiculos.csv")
