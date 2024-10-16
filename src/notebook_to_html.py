import subprocess

# Ruta al notebook que queremos convertir
notebook_path = '../notebooks/cooperativas_data_analysis.ipynb'

# Ruta donde guardaremos el archivo HTML generado
output_html_path = '../output/cooperativas_data_analysis.html'

# Comando para convertir el notebook a HTML usando nbconvert
command = f'jupyter nbconvert --to html {notebook_path} --output {output_html_path}'

# Ejecutar el comando
try:
    subprocess.run(command, shell=True, check=True)
    print(f"Notebook convertido exitosamente a HTML y guardado en: {output_html_path}")
except subprocess.CalledProcessError as e:
    print(f"Error al convertir el notebook: {e}")
