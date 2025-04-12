## Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

diccionario = {"a": "1", "b": "2", "c": "3"}
clave = "d"

try:
    valor = diccionario[clave]
    print(f"Se calculó el valor de la clave {clave} correctamente.")
except KeyError:
    print(f"Error accediendo a una clave inexistente en el Diccionario.")
else:
    print(valor)
finally:
    print("Fin del programa.")
