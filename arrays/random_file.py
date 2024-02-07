import os
import random

def choose_random_file(folder_path):
    # Obtener la lista de archivos en la carpeta
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Eliminar el script actual de la lista (si existe)
    current_script = os.path.basename(__file__)
    files = [f for f in files if f != current_script]

    if not files:
        print("No hay archivos para elegir.")
        return None

    # Elegir aleatoriamente un archivo
    chosen_file = random.choice(files)

    return chosen_file

if __name__ == "__main__":
    folder_path = "./"  # Reemplaza con la ruta de tu carpeta
    chosen_file = choose_random_file(folder_path)

    if chosen_file:
        print(f"Archivo elegido aleatoriamente: {chosen_file}")
