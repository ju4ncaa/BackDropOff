#!/usr/bin/python
#Author: 0xJuaNc4

#Módulos
import os
from sys import exit
from numpy import array
from rembg import remove
from PIL import Image

#Paleta de colores
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

#Función limpiar consola
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

#Comprueba que la ruta introducida sea correcta y contenga una imagen válida.
def check_path(path):
    valid_extensions = [".png", ".webp"]
    if os.path.isfile(path) and any(path.lower().endswith(ext) for ext in valid_extensions):
        return True
    else:
        print(f"\n{Colors.RED}[!]{Colors.RESET} La ruta {Colors.YELLOW}{img_path}{Colors.RESET} no es válida o no tiene una extensión de imagen WebP o PNG.")
        exit(1)

#Procesa la imagen, eliminando el fondo y guardando la nueva imagen.
def process_image(img_path):
    if check_path(img_path):
        # Obtener el nombre de la imagen con extensión
        img_name = os.path.basename(img_path)
        
        #Cargar imagen con PIL
        inp_image = Image.open(img_path)
        print(f"\n{Colors.GREEN}[*]{Colors.RESET} Imagen encontrada\n")
        print(f"\n{Colors.GREEN}[*]{Colors.RESET} Imagen {Colors.YELLOW}{img_name}{Colors.RESET} cargada\n")

        #Convertir la imagen en un array de numpy
        inp_arr = array(inp_image)

        #Aplicar la eliminación del fondo con rembg
        out_arr = remove(inp_arr)

        #Creando imagen PIL a partir del array resultante
        out_img = Image.fromarray(out_arr)

        #Guardando la imagen resultante
        out_img.save(f'backdropoff-{img_name}')
        print(f"\n{Colors.GREEN}[*]{Colors.RESET} Imagen sin fondo guardada en {Colors.YELLOW}{os.getcwd()}{Colors.RESET}\n")
    else:
        print(f"\n{Colors.RED}[!]{Colors.RESET} No se ha encontrado {img_path}")

#Programa principal
if __name__ == "__main__":
    try:
        while True:
            #Limpiar consola
            clear_console()
            #Solicitar al usuario que ingrese la ruta de la imagen
            img_path = input(f"\n{Colors.CYAN}[*]{Colors.RESET} Ingresa la ruta de la imagen: ")
            #Procesar la imagen
            process_image(img_path)
            #Preguntar al usuario si desea realizar otra operación
            user_choice = input(f"\n{Colors.CYAN}[*]{Colors.RESET} ¿Deseas procesar otra imagen? (s/n): ").lower()
            if user_choice != "s":
                print(f"\n{Colors.RED}[!]{Colors.RESET} Saliendo...")
                break
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[!]{Colors.RESET} Saliendo...")
