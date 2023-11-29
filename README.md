# BackDropOff

<div align="center">
  <img src="https://github.com/0xJuaNc4/BackDropOff/assets/130152767/39185e06-7daf-4942-81f1-f280cec91b19" width="300px">
</div>

Script hecho en Python el cual utiliza la biblioteca rembg para eliminar el fondo de una imagen y guarda la nueva imagen sin fondo en formato WebP o PNG.

## Requisitos
1. Asegúrate de tener Python instalado. Además, instala el módulo rembg utilizando:

```bash
pip install rembg
```
2. Las imágenes deben ser en formato WebP o PNG, ya que este script utiliza transparencia modo alfa para la eliminación del fondo.

## ¿Qué es el modo alfa?
El modo alfa en una imagen indica cuánto es transparente un píxel, variando de completamente transparente a completamente opaco. Se usa para lograr transparencia y suavizar bordes.

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

<img src="https://github.com/0xJuaNc4/BackDropOff/assets/130152767/40022d7a-c239-4b30-a4dd-8d7bf6e5bcbe" width="500px">

1. Descargar el contenido del repositorio.

![imagen](https://github.com/0xJuaNc4/BackDropOff/assets/130152767/7b270d63-a7e9-482b-ab0b-f955f3413b2f)

3. Ejecutar el script desde la terminal utilizando el comando `python backdropoff.py` o la ruta correspondiente donde se encuentre el script.

![imagen](https://github.com/0xJuaNc4/BackDropOff/assets/130152767/fb224a4b-f211-4709-af0d-0dee69cfc064)

4. Proporcionar la ruta absoluta de una imagen PNG, tambien se puede indicar el nombre de la imagen si esta se encuentra en el directorio del script.

![imagen](https://github.com/0xJuaNc4/BackDropOff/assets/130152767/28699cb7-6719-43c8-8500-9bbe6e5f745e)

5. El script procesará la imagen, eliminará el fondo y guardará la nueva imagen en el mismo directorio con el nombre **backdropoff.png**

![imagen](https://github.com/0xJuaNc4/BackDropOff/assets/130152767/8247e63a-99a0-40d1-8381-cd648978bb75)

6. Obtenemos la imagen sin fondo en el directorio BackDropOff

<img src="https://i.ibb.co/B2Xhpqv/backdropoff.webp" width="500px">
