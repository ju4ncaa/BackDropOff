# Author: 0xJuaNc4
# Módulos
import rembg  # instalar rembg: pip install rembg
import numpy as np
import os
import sys
from PIL import Image
from colorama import init, Fore

# Paleta de colores
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
RESET = Fore.RESET

def check_path(path):
    # Comprueba que la ruta introducida sea correcta y contenga una imagen válida.
    valid_extensions = [".png", ".webp"]
    if os.path.isfile(path) and any(path.lower().endswith(ext) for ext in valid_extensions):
        return True
    else:
        print(f"\n{RED}[!]{RESET} La ruta {YELLOW}{img_path}{RESET} no es válida o no tiene una extensión de imagen WebP o PNG.\n")
        sys.exit(1)

def process_image(img_path):
    #Procesa la imagen, eliminando el fondo y guardando la nueva imagen.
    if check_path(img_path):
        # Obtener el nombre de la imagen con extensión
        img_name_ext = os.path.basename(img_path)

        # Obtener nombre de la imagen sin extensión
        img_name = os.path.splitext(os.path.basename(img_path))[0]

        # Obtener extensión de la imagen
        img_extension = os.path.splitext(img_path)[-1].lower()

        # Cargar imagen con PIL
        inp_image = Image.open(img_path)
        print(f"\n{GREEN}[*]{RESET} Imagen encontrada\n")
        print(f"\n{GREEN}[*]{RESET} Imagen {YELLOW}{img_name_ext}{RESET} cargada\n")

        # Convertir la imagen en un array de numpy
        inp_arr = np.array(inp_image)

        # Aplicar la eliminación del fondo con rembg
        out_arr = rembg.remove(inp_arr)

        # Creando imagen PIL a partir del array resultante
        out_img = Image.fromarray(out_arr)

        # Guardando la imagen resultante
        out_img.save(f'backdropoff-{img_name}{img_extension}')
        print(f"\n{GREEN}[*]{RESET} Imagen sin fondo guardada en {YELLOW}{os.getcwd()}{RESET}\n")
    else:
        print(f"\n{RED}[!]{RESET} No se ha encontrado {img_path}, saliendo...\n")

# Programa principal
if __name__ == "__main__":
    while True:
        # Solicitar al usuario que ingrese la ruta de la imagen
        img_path = input(f"\n{CYAN}[*]{RESET} Ingresa la ruta de la imagen: ")

        # Procesar la imagen
        process_image(img_path)

        # Preguntar al usuario si desea realizar otra operación
        decision = input(f"\n{CYAN}[*]{RESET} ¿Deseas procesar otra imagen? (s/n): ").lower()
        if decision != "s":
            print(f"\n{RED}[!]{RESET} Saliendo...\n")
            break
