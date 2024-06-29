import os
from datetime import datetime

def obtener_info_archivo(ruta):
    info_archivo = os.stat(ruta)
    fecha_modificacion = datetime.fromtimestamp(info_archivo.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    tamano = info_archivo.st_size
    return fecha_modificacion, tamano
