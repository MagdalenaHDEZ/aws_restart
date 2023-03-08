#importa los módulos
import csv #    Manejo de archivos tipo csv
import copy # hacer copias de colecciones

#diccionario que funciona como plantilla
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

print(myVehicle.keys())
print(myVehicle.values())
print(myVehicle.items())

for key, value in myVehicle.items():
    print(key,value)
    
    
#lista de diccionarios
miInventarioList = []
#Manejo de archivos
with open('car_fleet.csv') as csv:
    csvredaer = csv.read(csv, delimiter=',')
    
    lineCount = 0
    
    for roww in csv:
        print(f"las solumnas son: {", ".join(row)}\n")
        lineCount += 1
    
    
    
    