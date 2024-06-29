import shutil
from PIL import Image
from pyzbar.pyzbar import decode

def leer_qr_y_mover(archivo_qr, nueva_ubicacion):
    # Leer el codigo QR
    datos = decode(Image.open(archivo_qr))
    if datos:
        metadatos = datos[0].data.decode('utf-8')
        print("Metadatos leídos del QR:")
        print(metadatos)
    
    else:
        print("No se pudo leer el codigo QR")
