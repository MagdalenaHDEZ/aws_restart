##listas
#secuencia de cualquier tipo de elementos
#permite repetidos
#es mutable (puede cambiar)
#indices positivos se cuanta desde 0 hasta el tamaño de la lista -1
#por el contrario si uso negativos se accede de atras haci aadelante -1(ultimo) -2(penultimo)

frutas= ["uva","manzana","coco"]
print(frutas)
print (frutas[0])
print (frutas[-1])
frutas [0] = True

print(f"ha cambiado el primer elemento de la lista", frutas)
print (frutas.index("coco"))

#tupla es una lista que no cambia (inmutable)
#se declara con ()

colores = ("amarillo","rojo","verde")

print(colores[1])
print("_"*30)

#diccionarios
#similitud encuentro una palabra y su valor o siginifcado asociado
##key , value
#mutable
#no admite valores repetidos
#se declara con {}, cada item se compone de key : value

#key son string(en la mayoria delos casos)
#value cualquier tipo
#           llave:valor
registros = {"luis":100,"jose":95, "irene":97}
print (registros)

print(registros["luis"])





