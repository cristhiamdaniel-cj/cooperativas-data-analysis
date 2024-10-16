import os
import pandas as pd
import logging
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

# Configuración de logging
log_file = 'conversion_log.log'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename=log_file, filemode='a')

# Función para estandarizar nombres de archivos
def estandarizar_nombre_archivo(nombre):
    logging.info(f"Estandarizando nombre de archivo: {nombre}")

    # Separar el nombre del archivo de su extensión
    nombre_sin_extension, extension = os.path.splitext(nombre)

    # Convertir a minúsculas el nombre sin la extensión
    nombre_sin_extension = nombre_sin_extension.lower()

    # Reemplazar espacios por guiones bajos en el nombre sin la extensión
    nombre_sin_extension = nombre_sin_extension.replace(' ', '_')

    # Eliminar caracteres especiales, pero preservar el punto de la extensión
    nombre_sin_extension = ''.join(e for e in nombre_sin_extension if e.isalnum() or e == '_')

    # Unir el nombre estandarizado con la extensión original
    nuevo_nombre = f"{nombre_sin_extension}{extension}"
    logging.info(f"Nuevo nombre de archivo estandarizado: {nuevo_nombre}")

    return nuevo_nombre

# Función para convertir archivos Excel a CSV
def convertir_excel_a_csv(archivos_excel):
    # Obtener la ruta del directorio del proyecto
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Ruta absoluta para la carpeta de salida 'output' dentro del directorio del proyecto
    output_folder = os.path.join(project_dir, 'output')

    # Verificar si la carpeta de salida existe, si no, crearla
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        logging.info(f"Carpeta de salida creada: {output_folder}")

    # Recorrer los archivos seleccionados
    for filepath in archivos_excel:
        filename = os.path.basename(filepath)
        logging.info(f"Procesando archivo: {filename}")

        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            try:
                # Leer el archivo Excel
                df = pd.read_excel(filepath)
                logging.info(f"Archivo Excel cargado exitosamente: {filename}")

                # Generar el nuevo nombre para el archivo CSV
                nuevo_nombre = estandarizar_nombre_archivo(filename.replace('.xlsx', '.csv').replace('.xls', '.csv'))

                # Ruta completa del archivo de salida (CSV)
                output_path = os.path.join(output_folder, nuevo_nombre)

                # Guardar como CSV
                df.to_csv(output_path, index=False)
                logging.info(f"Archivo convertido y guardado como CSV: {nuevo_nombre}")
            except Exception as e:
                logging.error(f"Error al procesar el archivo {filename}: {e}")
                print(f"Error al procesar el archivo {filename}. Revisa el log para más detalles.")
        else:
            logging.warning(f"Archivo no soportado: {filename}")

if __name__ == "__main__":
    # Ocultar la ventana principal de Tkinter
    root = Tk()
    root.withdraw()

    # Abrir el explorador de archivos para seleccionar archivos Excel
    logging.info("Abriendo diálogo para seleccionar archivos Excel.")
    archivos_seleccionados = askopenfilenames(title="Selecciona los archivos Excel a convertir",
                                              filetypes=[("Archivos Excel", "*.xlsx *.xls")])

    # Convertir los archivos seleccionados
    if archivos_seleccionados:
        logging.info(f"Archivos seleccionados: {archivos_seleccionados}")
        convertir_excel_a_csv(archivos_seleccionados)
    else:
        logging.info("No se seleccionaron archivos.")
        print("No se seleccionaron archivos.")
