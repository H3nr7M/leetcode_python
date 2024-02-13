import os
import random

def select_random_folder_and_file():
    # Obtener la lista de carpetas en el directorio actual
    folders = [folder for folder in os.listdir('.') if os.path.isdir(folder)]
    
    # Seleccionar una carpeta al azar
    random_folder = random.choice(folders)
    
    # Obtener la lista de archivos en la carpeta seleccionada
    files_in_folder = [file for file in os.listdir(random_folder) if os.path.isfile(os.path.join(random_folder, file))]
    
    # Seleccionar un archivo al azar de la carpeta seleccionada
    random_file = random.choice(files_in_folder)
    
    return random_folder, random_file

# Llamar a la función y obtener la carpeta y el archivo seleccionados al azar
random_folder, random_file = select_random_folder_and_file()

# Imprimir la carpeta y el archivo seleccionados al azar
print("Carpeta seleccionada:", random_folder)
print("Archivo seleccionado:", random_file)
