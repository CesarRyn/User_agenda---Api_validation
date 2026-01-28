import sqlite3 as sql
from funciones import datos_usuario
from funciones import eleccion_busqueda_usuario
from funciones import cargar_archivo
from llamadas_api import api_direccion
from funciones import invalid_direccion
from llamadas_api import api_direccion
from funciones import invalid_direccion
from validaciones import validar_edad
from validaciones import validar_id
from validaciones import validar_strs,validar_correo,validar_telefono
def crear_tabla():
    db=sql.connect("base de datos.db")
    cursor=db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS USUARIOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE TEXT NOT NULL,
    DIRECCION TEXT NOT NULL,
    CIUDAD TEXT NOT NULL,
    PAIS TEXT NOT NULL,
    EDAD INTEGER NOT NULL,
    TELEFONO TEXT NOT NULL,
    CORREO TEXT NOT NULL,
    FECHA_NACIMIENTO TEXT NOT NULL
    )
    """)
    db.commit()
    db.close()
def agregar_usuario_db():
    nombre,direccion,edad,telefono,correo,fecha_nacimiento=datos_usuario()
    res=api_direccion(direccion)
    if res==[]:
        res,direccion=invalid_direccion()
    ciudad=res["address"]["city"]
    pais=res["address"]["country"]
    db=sql.connect("base de datos.db")
    cursor=db.cursor()
    cursor.execute("INSERT INTO USUARIOS (NOMBRE, DIRECCION, CIUDAD, PAIS, EDAD, TELEFONO, CORREO, FECHA_NACIMIENTO) VALUES (?,?,?,?,?,?,?,?)",
        (nombre,direccion,ciudad,pais,edad,telefono,correo,fecha_nacimiento))
    db.commit()
    db.close()
def modificar_usuario():
    id_usuario=validar_id()
    z=["NOMBRE","DIRECCION","EDAD","TELEFONO","CORREO","FECHA_NACIMIENTO"]
    diccionario={}
    for k in z:
        while True:
            try:
                opc=int(input(f"Desea modificar {k}? 1-Si, 2-No\n"))
                if opc in [1,2]:
                    break
            except ValueError:
                print("Invalido")
        if opc==1:
            if k=="EDAD":
                x=validar_edad()
                diccionario[k]=x
            elif k=="CORREO":
                x=input("Ingrese correo electronico:\n")
                x=validar_correo(x)
                diccionario[k]=x
            elif k=="TELEFONO":
                x=input("Ingrese numero telefonico:\n")
                x=validar_telefono(x)
                diccionario[k]=x
            else:
                print(f"Ingrese {k}:")
                x=validar_strs()
                diccionario[k]=x
    columnas=", ".join(f"{columna} = ?" for columna in diccionario.keys())
    if "DIRECCION" in diccionario:
        direccion=diccionario["DIRECCION"]
        res=api_direccion(direccion)
        if res==[]:
            res=invalid_direccion()
        ciudad=res["address"]["city"]
        pais=res["address"]["country"]
        lm=[ciudad,pais, id_usuario]
        columnas += ", CIUDAD = ?, PAIS = ?"
    else:
        lm=[id_usuario]
    if diccionario:
        db=sql.connect("base de datos.db")
        cursor=db.cursor()
        cursor.execute(f"UPDATE USUARIOS SET {columnas} WHERE ID = ?",
                   [value for value in diccionario.values()]+lm)
        db.commit()
        db.close()
def eliminar_usuario():
    elec= eleccion_busqueda_usuario()
    if isinstance(elec,int):
        parametro="ID"
    else:
        parametro="NOMBRE"
    lm=[elec]
    db=sql.connect("base de datos.db")
    cursor=db.cursor()
    cursor.execute(f"DELETE FROM USUARIOS WHERE {parametro} = ?",
                   lm)
    db.commit()
    db.close()
def buscar_usuario():
    elec=eleccion_busqueda_usuario()
    if isinstance(elec, int):
        columna="ID"
    else:
        columna="NOMBRE"
    db=sql.connect("base de datos.db")
    cursor=db.cursor()
    cursor.execute(f"SELECT * FROM USUARIOS WHERE {columna} = ?",
                     [elec])
    usuario=cursor.fetchone()
    db.close()
    if usuario:
        z=["ID","Nombre","Direccion","Edad","Telefono","Correo","Fecha nacimiento"]
        datos_usuario={}
        for j in range(len(z)):
            datos_usuario[z[j]]=usuario[j]
        return datos_usuario
    else:
        return None
def agregar_usuarios_archivo():
    rr=cargar_archivo()
    columnas=",".join(rr[0])
    db=sql.connect("base de datos.db")
    cursor=db.cursor()
    for i in range(1, len(rr)):
        cursor.execute(f"INSERT INTO USUARIOS ({columnas}) VALUES (?,?,?,?,?,?,?,?)",
                       tuple(rr[i][0:8]))
    db.commit()
    db.close()
    
