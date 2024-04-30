from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def cambiar_titulo_video(ruta_video, nuevo_titulo):
    # Verificar si el archivo de video existe
    if os.path.exists(ruta_video):
        # Cargar el video
        video = VideoFileClip(ruta_video)
        
        # Cambiar el título del video
        video.reader.infos['title'] = nuevo_titulo
        
        # Guardar el video con el nuevo título
        nombre_nuevo_video = f"{os.path.splitext(ruta_video)[0]}_{nuevo_titulo}"
        video.write_videofile(nombre_nuevo_video)
        
        print(f"El título del video '{ruta_video}' se ha cambiado a '{nuevo_titulo}'.")
        print(f"El video con el nuevo título se ha guardado como '{nombre_nuevo_video}'.")
    else:
        print(f"El archivo de video '{ruta_video}' no existe.")

# Obtener la ruta del directorio actual
directorio_actual = os.getcwd()

# Recorrer recursivamente el directorio actual y sus subdirectorios
for directorio_actual, subdirectorios, archivos in os.walk(directorio_actual):
    # Iterar sobre los archivos en el directorio actual
    for nombre_archivo in archivos:
        # Verificar si el archivo es un video (extensión .mp4)
        if nombre_archivo.lower().endswith((".mp4",".avi",".mkv",".wmv",".mpeg",".mpg")):
            # Ruta completa del archivo de video
            ruta_video = os.path.join(directorio_actual, nombre_archivo)
            
            # Nuevo título del video (igual al nombre del archivo sin la extensión)
            nuevo_titulo = os.path.splitext(nombre_archivo)[0]
            
            # Cambiar el título del video
            cambiar_titulo_video(ruta_video, nuevo_titulo)