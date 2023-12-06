# BackDropOff

<div align="center">
  <img src="https://github.com/0xJuaNc4/BackDropOff/assets/130152767/e6d309c3-9a0d-45f8-be79-c589c375b615" width="200px">
</div>

<br>

Script created in Python which uses the rembg library to remove the background of an image and saves the new image without background in WebP or PNG format.

## Important

1. Verify that you have all the necessary modules installed using the command:

```
pip3 install -r requirements.txt
```

3. Images must be in WebP or PNG format, as this script uses alpha mode transparency for background removal.

## What is alpha mode? 
The alpha mode in an image indicates how transparent a pixel is, varying from completely transparent to completely opaque. It is used to achieve transparency and soften edges.

## Usage
1. Clone this repository or download the backdropoff.py script.
```bash
git clone https://github.com/0xJuaNc4/BackDropOff
```
2. Execute the script with the command:
```bash
python backdropoff.py
```
3. The script will ask for the path to the image. Enter the full path and press Enter.

4. The backgroundless image will be saved in the current directory with the prefix "backdropoff".

## Usage Example

The example will be with the image of a tiger.

<img src="https://github.com/0xJuaNc4/BackDropOff/assets/130152767/40022d7a-c239-4b30-a4dd-8d7bf6e5bcbe" width="500px">

Download the contents of the repository.

![imagen](https://github.com/0xJuaNc4/BackDropOff/assets/130152767/7b270d63-a7e9-482b-ab0b-f955f3413b2f)

Execute the script from the terminal using the command `python backdropoff.py` or the corresponding path where the script is located.

![imagen](https://github.com/0xJuaNc4/BackDropOff/assets/130152767/0f433b53-8e4d-4679-8519-dd0003813bfc)

Specify the absolute path of a PNG image, you can also specify the name of the image if it is located in the script directory.

![imagen](https://github.com/0xJuaNc4/BackDropOff/assets/130152767/8682484c-5f6d-4471-aff2-4078c00c362e)

The script will process the image, remove the background and save the new image in the same directory with the name **backdropoff.png**.

![imagen](https://github.com/0xJuaNc4/BackDropOff/assets/130152767/85a8fdf4-2e29-4d75-8e21-b2b7df14e87b)

We obtain the image without background in the BackDropOff directory.

<img src="https://i.ibb.co/B2Xhpqv/backdropoff.webp" width="500px">
