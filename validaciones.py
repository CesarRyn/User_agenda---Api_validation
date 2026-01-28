from email_validator import validate_email, EmailNotValidError
import phonenumbers as pn
from phonenumbers.phonenumberutil import NumberParseException as npe
def validar_telefono(numero):
    while True:
        try:
            r=pn.parse(numero, "MX")
            if pn.is_valid_number(r):
                return numero
            else:
                print("Numero no valido, vuelva a ingresar:\n")
                numero=input()
        except npe:
            print("Numero no valido, vuelva a ingresar:\n")
            numero=input()
def validar_correo(correo):
    while True:
        try:
            r=validate_email(correo)
            return r.email
        except EmailNotValidError:
            print("Correo no valido vuelva a ingresar")
            correo=input()
def validar_strs():
    while True:
        cadena=input()
        if not cadena or len(cadena.strip())==0:
            print("No se permite, Vuelva a ingresar:")
        else:
            return cadena
def validar_edad():
    while True:
        try:
            edad=int(input("Ingrese edad:\n"))
            if edad>=18 and edad<=80:
                return edad
            else:
                print("Solo se permite edad mayor igual a 18 y menor igual a 80, Vuelva a ingresar:")
        except ValueError:
            print("Invalido, Vuelva a ingresar:")
def validar_id():
    while True:
        try:
            num=int(input("Ingrese id:\n"))
            if num<=0:
                print("No se permiten numeros menor a 1")
            else:
                return num
        except ValueError:
            print("Invalido")


