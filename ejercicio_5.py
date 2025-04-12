## Escribe un programa que intente dividir dos números. Si el segundo numero es cero, captura la excepcion ZeroDivisionError.
## Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

numero = input(f"Ingrese el 1° número: ")
numero2 = input(f"Ingrese el 2° número: ")

try:
    if numero.isnumeric() == False:
        raise ValueError("El primer valor debe ser numérico. \n\n")
    elif numero2 == "0":
        raise ZeroDivisionError("Numero2 no puede ser cero. \n\n")
    elif numero.isnumeric() and numero2.isnumeric():
        numero = int(numero)
        numero2 = int(numero2)
    numero3 = numero / numero2
    print(f"Se dividió correctamente. \n\n")
except ZeroDivisionError:
    print(f"Error de división por cero. \n\n")
except ValueError:
    print("Se ingresó un valor no numérico como primer número. \n\n")
except TypeError:
    print(f"Ambos operadores deben ser numericos.  \n\n")
except Exception as e:
    print(f"Ha ocurrido un error. {e}  \n\n")
else:
    print(f"{numero} / {numero2} == {numero3}")
finally:
    print("Fin del programa.")
