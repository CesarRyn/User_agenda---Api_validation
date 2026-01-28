from funciones import opc_menu
from funciones_base_datos import crear_tabla
from funciones_base_datos import agregar_usuario_db
from funciones_base_datos import modificar_usuario
from funciones_base_datos import eliminar_usuario
from funciones_base_datos import buscar_usuario
from funciones_base_datos import agregar_usuarios_archivo
crear_tabla()
while True:
    opc=opc_menu()
    if opc==1:#Agregar usuario
        agregar_usuario_db()
    elif opc==2:#Modificar usuario
        modificar_usuario()
    elif opc==3:#Cargar listado de usuarios
        agregar_usuarios_archivo()
    elif opc==4:#Eliminar usuarios
        eliminar_usuario()
    elif opc==5:#Buscar contacto
        respuesta= buscar_usuario()
        if respuesta==None:
            print("Usuario no encontrado")
        else:
            for dato, valor in respuesta.items():
                print(f"{dato}: {valor}")
    elif opc==6:#Salir
        break
