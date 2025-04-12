## Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario.
## Sin embargo, también intenta crear el archivo si no existe.

nombreArchivo = f"archivoInexistente.txt"

try:
    archivo = open(nombreArchivo, "r")
    text = archivo.read()
    print(f"El archivo {nombreArchivo} se abrió correctamente. \n\n")
except FileNotFoundError as e:
    print(f"No existe el archivo {nombreArchivo}. Error: {e}\n\n")
    with open(nombreArchivo, "w") as archivo:
        archivo.write(f"El archivo {nombreArchivo} fue creado correctamente. \n")
        archivo.write(f"Hola Mundo! \n")
else:
    print(f"El archivo {nombreArchivo} contiene lo siguiente: \n")
    print(f"'{text}' \n")
finally:
    print(f"El archivo {nombreArchivo} fue procesado correctamente. \n\n")
    archivo.close
