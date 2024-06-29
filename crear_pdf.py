from fpdf import FPDF
import os
from datetime import datetime

def crear_pdf(nombre_archivo, contenido):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=contenido, ln=True, align='C')
    pdf.output(nombre_archivo)
    
    # Agregar metadatos
    fecha_creacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    os.utime(nombre_archivo, (os.path.getatime(nombre_archivo), datetime.timestamp(datetime.now())))
    
    return fecha_creacion
