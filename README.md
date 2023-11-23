# BackDropOff
Script hecho en Python el cual utiliza la biblioteca rembg para eliminar el fondo de una imagen y guarda la nueva imagen sin fondo en formato WebP o PNG.

## Requisitos
1. Asegúrate de tener Python instalado. Además, instala el módulo rembg utilizando:

```bash
pip install rembg
```
2. Las imágenes deben ser en formato WebP o PNG, ya que este script utiliza transparencia modo alfa para la eliminación del fondo.

## ¿Qué es el modo alfa?
El modo alfa en una imagen indica cuánto es transparente un píxel, variando de completamente transparente a completamente opaco. En el contexto de imágenes PNG, se usa para lograr transparencia y suavizar bordes.

## Uso
1. Clona este repositorio o descarga el script backdropoff.py.
```bash
git clone https://github.com/0xJuaNc4/BackDropOff.git
```
2. Ejecuta el script con el comando:
```bash
python backdropoff.py
```
3. El script solicitará la ruta de la imagen. Ingresa la ruta completa y presiona Enter.
4. La imagen sin fondo se guardará en el directorio actual con el prefijo "backdropoff".

## Ejemplo de Uso
El ejemplo será con la imagen de un tigre

<img src="https://github.com/0xJuaNc4/BackDropOff/assets/130152767/6a08df8a-e558-4ce8-8ada-589a1e404633" width="500px">

1. Descargar el contenido del repositorio.
   
![imagen](https://github.com/0xJuaNc4/BackDropOff/assets/130152767/d3c810d6-b8b1-40ae-b2df-ab42ddd19349)

3. Ejecutar el script desde la terminal utilizando el comando `python backdropoff.py` o la ruta correspondiente donde se encuentre el script.

![imagen](https://github.com/0xJuaNc4/BackDropOff/assets/130152767/72423949-9a75-476f-8810-dc184404148c)

4. Proporcionar la ruta absoluta de una imagen PNG, tambien se puede indicar el nombre de la imagen si esta se encuentra en el directorio del script.

![imagen](https://github.com/0xJuaNc4/BackDropOff/assets/130152767/aa5c7e7d-ed97-4f15-bdb2-745b64d70499)

5. El script procesará la imagen, eliminará el fondo y guardará la nueva imagen en el mismo directorio con el nombre **backdropoff.png**

![imagen](https://github.com/0xJuaNc4/BackDropOff/assets/130152767/eceea5d3-c8c5-4fa0-8329-52f3a4db40d2)

6. Obtenemos la imagen sin fondo en el directorio BackDropOff

<img src="https://i.ibb.co/B2Xhpqv/backdropoff.webp" width="500px">
