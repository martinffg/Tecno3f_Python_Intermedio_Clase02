## Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

numero = 10
nummero2 = 0

try:
    numero3 = numero / nummero2
    print(f"Se dividió correctamente.")
except ZeroDivisionError:
    print(f"Error de división por cero.")
else:
    print(numero3)
finally:
    print("Fin del programa.")
