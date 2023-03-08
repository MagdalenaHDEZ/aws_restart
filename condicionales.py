userReply= input("Necesitas entrgar un paquete?").capitalize()

if userReply == "Si":
    print("podemos ayudar con la entrega")
else:
    print("vuelva pronto")
    exit() # es una funcion para salir del programa
    
    
userReply = input("Que le gustaria comprar: estampas,sobres o copias?")

if userReply == "estampas":
    print("tensmos muchas")
elif userReply == "sobre" :
    print("tenemos muchos sobres")
elif userReply == "copias":

    copias= input("cuantas requiere")
    print("Gracias vualva pronto")
    
    
    
    