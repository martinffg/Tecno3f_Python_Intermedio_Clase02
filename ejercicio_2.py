## Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.


numero = 10
cadena = "Hola Mundo"

try:
    suma = numero + cadena
    print(f"Se sumó correctamente.")
except TypeError:
    print(f"Error de tipo, verificar valores ingresados.")
else:
    print(suma)
finally:
    print("Fin del programa.")
