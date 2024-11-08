import csv, ast
    
def guardar_datos_csv(vehiculos, nombre_archivo):
    try:
        with open(nombre_archivo, "w", newline="") as archivo:
            archivo_csv = csv.writer(archivo)
            for vehiculo in vehiculos:
                clase = str(vehiculo.__class__)
                atributos = str(vehiculo.__dict__)
                archivo_csv.writerow([clase, atributos])
        print("\n-------------------------------------")
        print("*** Archivo guardado exitosamente ***\n")
    except Exception as e:
        print(f"Error al guardar datos: {e}")
        
def leer_datos_csv(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            archivo_csv = csv.reader(archivo)
            for fila in archivo_csv:
                tipo_clase = fila[0].split(".")
                atributos = ast.literal_eval(fila[1])  
                print(f"\nLista de Vehiculos {tipo_clase[1][:-2]}")
                print(f"{atributos}")
        print("\n-------------------------------------")
        print("*** Archivo leido exitosamente ***\n")
    except Exception as e:
        print(f"Error al leer los datos: {e}")

