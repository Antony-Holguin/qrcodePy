import os
from crear_pdf import crear_pdf
from generar_qr import generar_qr
from obtener_info_archivo import obtener_info_archivo
from leer_qr_y_mover import leer_qr_y_mover

def obtener_contenido_desde_consola():
    print("Ingrese el contenido para el PDF (presione Enter dos veces para finalizar):")
    contenido = []
    while True:
        linea = input()
        if linea.strip() == "":
            break
        contenido.append(linea)
    return "\n".join(contenido)


if __name__ == "__main__":
    # Obtener el nombre del usuario logueado en Windows
    usuario_logueado = os.getlogin()
    
    # Especificar la ubicacion del archivo PDF y QR
    ruta_pdf = "D:/factura.pdf"
    ruta_qr = "D:/metadatos_qr.png"
    nueva_ubicacion_pdf = "D:/nueva_factura.pdf"

    # Paso 1: Obtener el contenido para el PDF desde la consola
    contenido = obtener_contenido_desde_consola()
    
    # Paso 2: Crear el archivo PDF con el contenido ingresado
    fecha_creacion = crear_pdf(ruta_pdf, contenido)
    
    # Obtener informacion adicional del archivo PDF creado
    fecha_modificacion, tamano = obtener_info_archivo(ruta_pdf)
    
    # Paso 3: Generar el codigo QR con los metadatos
    metadatos = (
        f"Ubicacion: {ruta_pdf}\n"
        f"Informacion relevante: Factura de compra\n"
        f"Creador: {usuario_logueado}\n"
        f"Fecha de creacion: {fecha_creacion}\n"
        f"Fecha de modificacion: {fecha_modificacion}\n"
        f"Tamaño: {tamano} bytes"
    )
    generar_qr(metadatos, ruta_qr)

    # Paso 4: Leer el codigo QR, mover el archivo y mostrar los metadatos
    leer_qr_y_mover(ruta_qr, nueva_ubicacion_pdf)
