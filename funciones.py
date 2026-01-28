from validaciones import validar_strs
from validaciones import validar_edad
from validaciones import validar_id, validar_correo,validar_telefono
from llamadas_api import api_direccion
def opc_menu():
    opciones_menu=[1,2,3,4,5,6]
    while True:
        print("Seleccione una opcion de menu\n1-Agregar usuario\n2-Modificar usuario\n3-Cargar listado de usuarios (archivo scv)\n4-Eliminar usuario\n5-Buscar contacto\n6-Salir")
        try:    
            opc=int(input())
            if opc not in opciones_menu:
                print("Invalido\n")
            else:
                break
        except ValueError:
            print("Invalido\n")
    return opc
def datos_usuario():
    print("Ingrese nombre:")
    nombre=validar_strs()
    print("Ingrese direccion:")
    direccion=validar_strs()
    edad=validar_edad()
    print("Ingrese telefono:")
    telefono=input()
    telefono=validar_telefono(telefono)
    print("Ingrese correo electronico:")
    correo=input()
    correo=validar_correo(correo)
    print("Ingrese fecha nacimiento:")
    fecha_nacimiento=validar_strs()
    return nombre,direccion,edad,telefono,correo,fecha_nacimiento
def eleccion_busqueda_usuario():
    while True:
        print("Ingrese una opcion de busqueda para el usuario:\n1-Busqueda por id\n2-Busqueda por nombre")
        opc_bsqda=int(input())
        if opc_bsqda!=1 and opc_bsqda!=2:
            print("Invalido")
        else:
            if opc_bsqda==1:
                return validar_id()
            else:
                print("Ingrese nombre:\n")
                return validar_strs()
def cargar_archivo():
    with open("lista_usuarios.csv", newline="") as archivo:
        r=archivo.readlines()
    rr=[]
    for linea in r:
        if linea.strip():
            u=linea.strip().split(";")
            rr.append(u)
    return rr
def invalid_direccion():
    while True:
        print("Direccion no valida")
        direccion=input("Ingrese una nueva direccion:\n")
        res= api_direccion(direccion)
        if res!=[]:
            return res,direccion     











