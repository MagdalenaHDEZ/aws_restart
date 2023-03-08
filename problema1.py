"""
Se necesita un programa que calcule el precio final de un producto que cuenta con el 15% de
descuento.
Input: Precio del producto (float > 0)
Output: Precio total con descuento (float > 0)
"""
precio= float (input(" Ingresa el precio del producto:"))


if precio >0  :
    Descuento= (precio*15)/100
    Total= precio-Descuento
    print("el precio es :", Total)
else : 
    print("datos invalidos")
    

