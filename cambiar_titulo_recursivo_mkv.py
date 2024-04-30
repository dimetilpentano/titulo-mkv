import os
import subprocess

# ruta del directorio actual
directorio_actual = os.getcwd()

# recorrer el directorio actual y sus subdirectorios
for directorio_actual, subdirectorios, archivos in os.walk(directorio_actual):
    # iterar sobre los archivos en el directorio actual
    for nombre_archivo in archivos:
        # Verificar si el archivo es un .mkv
        if nombre_archivo.lower().endswith(".mkv"):
            # ruta del archivo
            ruta_video = os.path.join(directorio_actual, nombre_archivo)
            
            # nuevo título (igual al nombre del archivo sin la extensión)
            nuevo_titulo = os.path.splitext(nombre_archivo)[0]
            
            # ruta completa al archivo
            ruta_archivo = directorio_actual + "\\" + nombre_archivo
        
            # cambiar el título del video
            comando = f"mkvpropedit \"{ruta_archivo}\" -e info -s title=\"{nuevo_titulo}\""
            subprocess.run(comando, shell=True)
            print("\n" + directorio_actual)
            print("El titulo del archivo " + nombre_archivo + " se ha cambiado a: " + nuevo_titulo + "\n")
input("Aporrea enter para salir")

