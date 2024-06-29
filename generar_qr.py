import qrcode

def generar_qr(datos, nombre_archivo_qr):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(datos)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo_qr)
