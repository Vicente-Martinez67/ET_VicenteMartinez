juegos={
}
inventario={}

def menu():
    while True:
        print("===MENU PRINCIPAL===")
        print("1.-: Stock por plataforma")
        print("2.-: Busqueda de juegos por rango de precio")
        print("3.-: Actualizar precio de juego")
        print("4.-: Agregar Juego")
        print("5.-: Eliminar juego")
        print("6.-: Salir")



def leer_op():
    while True:
        try:
            op=int(input("Ingrese una opcion"))
            if op <1:
                print("opcion debe ser un numero mayor a 0 y entero")
            elif op <1 or op >6:
                print("La opcion ingresada debe ser entre 1 o 6")
            return op
        except ValueError:
            print("La opcion debe ser un numero entero o mayor a 0")





def stock_Plataforma(plataforma):
    plataforma=input("Ingrese la plataforma del videojuego")

    










def busqueda_rango():
    pass









def actualizar_precioJuego():
    pass









def agregar_juego():
    titulo=validar_titulo()
    plataforma=validar_plataforma()
    genero=validar_genero()
    clasificacion=validar_clasificacion()
    multiplayer=validar_multiplayer()
    editor=validar_editor()
    stock=validar_stock()

    juegos={
        "titulo":titulo,
        "plataforma":plataforma,
        "genero":genero,
        "clasificacion":clasificacion,
        "multiplayer":multiplayer,
        "editor":editor,
        "stock":stock
    }

    print("Juego Agregado")









def validar_titulo():
    titulo=input("Ingrese el titulo del videojuego")
    
    if titulo.strip()=="":
        print("El titulo del videojuego no puede llevar espacios en blanco y no puede estar vacio")
    else:
        return



def validar_plataforma():
    plataforma=input("ingrese la plataforma del videojuego")
    
    if plataforma.strip()=="":
        print("La plataforma del videojuego no puede llevar espacios en blanco y no puede estar vacio")
    else:
        return


def validar_genero():
    genero=input("Ingrese el genero del videojuego")

    if genero.strip()=="":
        print("El genero del videojuego no puede llevar espacios en blanco y no puede estar vacio")
    else:
        return



def validar_clasificacion():
    clasificacion=input("Ingrese la clasificacion del videojuego")

    if clasificacion =="E" or clasificacion== "T" or clasificacion =="M":
        print("Clasificacion agregada con exito")
    else:
        return
    



def validar_multiplayer():
    multiplayer=input("Ingrese si el videojuego es multijugador")

    if multiplayer=="s" or multiplayer =="n":
        if multiplayer == "s":
            multiplayer==True
            print("El videojuego es multiplayer")
        elif multiplayer =="n":
            multiplayer==False
            print("EL videojuego no es multijugador")



def validar_editor():
    editor=input("Ingrese el editor del videojuego")

    if editor.strip()=="":
        print("El editor del videojuego no puede llevar espacios y no puede estar vacio")
    else:
        return


def validar_precio():
    precio=int(input("Ingrese el precio del videojuego"))

    try:
        if precio<0:
            print("El precio debe ser un numero entero mayor que 0")
        else:
            return
    except ValueError:
        print("El precio debe ser un numero entero mayor que 0")


def validar_stock():
    stock=input("Ingrese el stock del videojuego")

    try:
        if stock<0:
            print("El stock debe ser un numero entero mayor que 0")
        else:
            return
    except ValueError:
        print("El stock debe ser un numero entero mayor que 0")



        



def eliminar_juego():
    pass
















#MAIN

while True:
    menu()
    opcion=leer_op()

    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion ==3:
        pass
    elif opcion == 4:
        agregar_juego()
    elif opcion == 5:
        pass
    elif opcion == 6:
        print("Programa Finalizado")
        break