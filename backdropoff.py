#Author: 0xJuaNc4

#Módules
import os
from sys import exit
from numpy import array
from rembg import remove
from PIL import Image

# Color palette
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

#Clear console function
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

#Checks that the path entered is correct and contains a valid image.
def check_path(path):
    valid_extensions = [".png", ".webp"]
    if os.path.isfile(path) and any(path.lower().endswith(ext) for ext in valid_extensions):
        return True
    else:
        print(f"\n{Colors.RED}[!]{Colors.RESET} La ruta {Colors.YELLOW}{img_path}{Colors.RESET} no es válida o no tiene una extensión de imagen WebP o PNG.")
        exit(1)

#Processes the image, removing the background and saving the new image.
def process_image(img_path):
    if check_path(img_path):
        # Get the name of the image with extension
        img_name = os.path.basename(img_path)
        
        # Load image with PIL
        inp_image = Image.open(img_path)
        print(f"\n{Colors.GREEN}[*]{Colors.RESET} Imagen encontrada\n")
        print(f"\n{Colors.GREEN}[*]{Colors.RESET} Imagen {Colors.YELLOW}{img_name}{Colors.RESET} cargada\n")

        # Convert image to numpy array
        inp_arr = array(inp_image)

        # Apply background removal with rembg
        out_arr = remove(inp_arr)

        # Creating PIL image from the resulting array
        out_img = Image.fromarray(out_arr)

        # Saving the resulting image
        out_img.save(f'backdropoff-{img_name}')
        print(f"\n{Colors.GREEN}[*]{Colors.RESET} Imagen sin fondo guardada en {Colors.YELLOW}{os.getcwd()}{Colors.RESET}\n")
    else:
        print(f"\n{Colors.RED}[!]{Colors.RESET} No se ha encontrado {img_path}")

# Main program
if __name__ == "__main__":
    try:
        while True:
            # Clear console
            clear_console()
            # Ask the user to enter the path of the image
            img_path = input(f"\n{Colors.CYAN}[*]{Colors.RESET} Ingresa la ruta de la imagen: ")
            # Process the image
            process_image(img_path)
            #Ask the user if he/she wants to perform a different operation.
            user_choice = input(f"\n{Colors.CYAN}[*]{Colors.RESET} ¿Deseas procesar otra imagen? (s/n): ").lower()
            if user_choice != "s":
                print(f"\n{Colors.RED}[!]{Colors.RESET} Saliendo...")
                break
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[!]{Colors.RESET} Saliendo...")
