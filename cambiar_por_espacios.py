import os

# Ruta del directorio donde se está ejecutando el programa
directorio_actual = os.getcwd()

# Ruta de la carpeta que contiene los archivos a renombrar
directorio = directorio_actual

# Verificar si el directorio existe
if os.path.exists(directorio):
    # Lista de archivos en el directorio
    archivos = os.listdir(directorio)
    caracter = input("¿Qué cambiamos por espacios? ")
    
    for nombre_archivo in archivos:
        # Ruta del archivo
        ruta_antigua = os.path.join(directorio, nombre_archivo)
        
        # Verificar si la extensión del archivo es ".py"
        if nombre_archivo.endswith(".py"):
            print(f"El archivo {nombre_archivo} no se renombrará porque es un archivo .py.")
            continue
                 
        if caracter in nombre_archivo:
            nombre_base, extension = os.path.splitext(nombre_archivo)
            
            # Reemplazar el caracter por espacios, excepto en la extensión
            partes = nombre_base.split(caracter)
            nombre_base_con_espacios = " ".join(partes)
            
            # Reconstruir el nombre completo del archivo
            nuevo_nombre = f"{nombre_base_con_espacios}{extension}"
            
            # Ruta completa del nuevo archivo
            ruta_nueva = os.path.join(directorio, nuevo_nombre)
            
            # Renombrar el archivo
            os.rename(ruta_antigua, ruta_nueva)
            print(f"Archivo {nombre_archivo} renombrado a {nuevo_nombre}")
            
else:
    print("El directorio especificado no existe.")

input("Presiona Enter para cerrar")